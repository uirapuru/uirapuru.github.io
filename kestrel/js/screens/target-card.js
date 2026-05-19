// js/screens/target-card.js
import { lcd5 } from '../lcd.js';

const LETTERS = ['A','B','C','D','E','F','G','H','I','J'];
const FIELD_GROUPS = {
  'Target Inputs': [
    { key:'tr',   label:'TR',   step:10,  fmt:v=>v+'m' },
    { key:'dof',  label:'DoF',  step:30,  fmt:v=>{ const d=((Math.round(v??0)%360)+360)%360; return `${String(d).padStart(3,'0')}°`; } },
    { key:'ideg', label:'Ideg', step:1,   fmt:v=>`${v>=0?'+':''}${Math.round(v)}°` },
    { key:'ts',   label:'TS',   step:0.1, fmt:v=>parseFloat(v).toFixed(1)+'m/s' },
  ],
  'Wind Inputs': [
    { key:'windDir',  label:'WD',  step:30,  fmt:v=>{ const h=Math.round(((v??0)%360)/30)||12; return `${h}:00`; } },
    { key:'windSpd',  label:'WS1', step:0.5, fmt:v=>parseFloat(v).toFixed(1)+'m/s' },
    { key:'windSpd2', label:'WS2', step:0.5, fmt:v=>parseFloat(v).toFixed(1)+'m/s' },
  ],
};
const SUB_ITEMS = ['Target Inputs','Wind Inputs','Designator','Clear All'];

let cardIdx = 0;
let view = 'card-menu'; // 'card-menu' | 'sub-menu' | 'fields'
let subIdx = 0;
let fieldIdx = 0;
let activeGroup = null;

export function registerTargetCard(menu) {
  menu.register('target-card', {
    onEnter() { cardIdx = 0; view = 'card-menu'; subIdx = 0; fieldIdx = 0; },

    onLeft(ctx) {
      if (view === 'card-menu') { cardIdx = (cardIdx - 1 + 10) % 10; return; }
      if (view === 'fields') {
        const f = activeGroup[fieldIdx];
        const cards = [...ctx.state.targetCards];
        cards[cardIdx] = { ...cards[cardIdx], [f.key]: (cards[cardIdx][f.key]||0) - f.step };
        ctx.setState({ targetCards: cards });
      }
    },
    onRight(ctx) {
      if (view === 'card-menu') { cardIdx = (cardIdx + 1) % 10; return; }
      if (view === 'fields') {
        const f = activeGroup[fieldIdx];
        const cards = [...ctx.state.targetCards];
        cards[cardIdx] = { ...cards[cardIdx], [f.key]: (cards[cardIdx][f.key]||0) + f.step };
        ctx.setState({ targetCards: cards });
      }
    },
    onUp() {
      if (view === 'sub-menu') subIdx = Math.max(0, subIdx - 1);
      if (view === 'fields')   fieldIdx = Math.max(0, fieldIdx - 1);
    },
    onDown() {
      if (view === 'sub-menu') subIdx = Math.min(SUB_ITEMS.length - 1, subIdx + 1);
      if (view === 'fields')   fieldIdx = Math.min(activeGroup.length - 1, fieldIdx + 1);
    },

    onSelect(ctx) {
      if (view === 'card-menu') { view = 'sub-menu'; subIdx = 0; return; }
      if (view === 'sub-menu') {
        const item = SUB_ITEMS[subIdx];
        if (item === 'Clear All') {
          const cards = ctx.state.targetCards.map(() => ({
            tr:500, dof:0, ideg:0, ts:0, windDir:90, windSpd:3, windSpd2:5, designator:'',
          }));
          ctx.setState({ targetCards: cards });
          return;
        }
        if (FIELD_GROUPS[item]) {
          activeGroup = FIELD_GROUPS[item]; view = 'fields'; fieldIdx = 0;
        }
      }
    },

    onOptions(ctx) {
      if (view === 'fields')   { view = 'sub-menu'; return; }
      if (view === 'sub-menu') { view = 'card-menu'; return; }
      ctx.pop();
    },

    render(state) {
      const letter = LETTERS[cardIdx];
      const card   = state.targetCards[cardIdx] || {};
      if (view === 'card-menu') {
        const wdH = Math.round(((card.windDir??90)%360)/30)||12;
        return lcd5([
          'Target Card',
          `<-> Card: ${letter}`,
          `TR:${card.tr}m DoF:${String(((card.dof??0)%360+360)%360).padStart(3,'0')}°`,
          `WS1:${(card.windSpd||0).toFixed(1)} WD:${wdH}:00`,
          'SEL enter',
        ]);
      }
      if (view === 'sub-menu') {
        const lines = SUB_ITEMS.map((item,i) => (i===subIdx?'►':' ')+item.slice(0,15));
        return lcd5([`Card ${letter}`, ...lines]);
      }
      if (view === 'fields') {
        const item = SUB_ITEMS[subIdx];
        const lines = activeGroup.map((f,i) => {
          const val = f.fmt ? f.fmt(card[f.key]??0) : String(card[f.key]??'');
          return (i===fieldIdx?'►':' ')+(f.label.padEnd(5))+val.slice(0,10);
        });
        while (lines.length < 4) lines.push('');
        return lcd5([`Card ${letter} ${item.slice(0,8)}`, ...lines]);
      }
      return lcd5(['Target Card','','','','']);
    },
  });
}
