// js/screens/main-menu.js

const MENU = [
  { label: 'Mode', lr: true },
  {
    label: 'Bluetooth', sub: [
      { label: 'Conct PC/Mobile', sub: [{ label: 'Device Connect' }, { label: 'HUD Connect' }] },
      { label: 'Status' },
      { label: 'Privacy Pin', sub: [{ label: 'Pin' }] },
    ]
  },
  { label: 'Data Port' },
  {
    label: 'Memory Options', sub: [
      { label: 'Mem Used' }, { label: 'Auto Store' }, { label: 'Store Rate' },
      { label: 'Overwrite' }, { label: 'Clear Log' },
    ]
  },
  {
    label: 'Graph Scale', sub: [
      { label: 'Wind Spd' }, { label: 'Temperature' }, { label: 'Humidity' },
      { label: 'Pressure' }, { label: 'Altitude' }, { label: 'Density Alt' },
    ]
  },
  {
    label: 'System', sub: [
      { label: 'Time & Date' }, { label: 'Compass Cal' },
      { label: 'Accuracy 1st', push: 'accuracy-1st' },
      { label: 'Measurements' }, { label: 'Units' }, { label: 'Language' },
      { label: 'Batt' }, { label: 'Humidity Cal' }, { label: 'Factory Restore' },
    ]
  },
  {
    label: 'About', sub: [
      { label: 'Version' }, { label: 'Legal' }, { label: 'Snake', push: 'snake' },
    ]
  },
];

const MODES = ['weather', 'ballistics', 'easy'];
const MODE_GO = { weather: 'weather', ballistics: 'ballistics-mode', easy: 'easy' };
const MODE_LBL = { weather: 'Weather', ballistics: 'Ballstcs', easy: 'Easy' };

let navStack = [];

function cur() { return navStack[navStack.length - 1]; }

export function registerMainMenu(menu) {
  menu.register('main-menu', {
    onEnter() { navStack = [{ list: MENU, idx: 0 }]; },

    onUp() { cur().idx = Math.max(0, cur().idx - 1); },
    onDown() { cur().idx = Math.min(cur().list.length - 1, cur().idx + 1); },

    onLeft(ctx) {
      const item = cur().list[cur().idx];
      if (!item.lr) return;
      const i = MODES.indexOf(ctx.state.mode);
      const next = MODES[(i - 1 + MODES.length) % MODES.length];
      ctx.setState({ mode: next });
      ctx.go(MODE_GO[next]);
    },

    onRight(ctx) {
      const item = cur().list[cur().idx];
      if (!item.lr) return;
      const i = MODES.indexOf(ctx.state.mode);
      const next = MODES[(i + 1) % MODES.length];
      ctx.setState({ mode: next });
      ctx.go(MODE_GO[next]);
    },

    onSelect(ctx) {
      const item = cur().list[cur().idx];
      if (item.lr) { ctx.go(MODE_GO[ctx.state.mode]); return; }
      if (item.push) { ctx.push(item.push); return; }
      if (item.sub) { navStack.push({ list: item.sub, idx: 0 }); return; }
    },

    onOptions(ctx) {
      if (navStack.length > 1) { navStack.pop(); return; }
      ctx.pop();
    },

    render(state) {
      const c = cur();
      const maxStart = Math.max(0, c.list.length - 4);
      const start = Math.min(Math.max(0, c.idx - 1), maxStart);
      const items = c.list.slice(start, start + 4);

      const lines = items.map((item, i) => {
        const idx = start + i;
        const sel = idx === c.idx;
        const lbl = item.lr ? `Mode  <${MODE_LBL[state.mode]}>` : item.label;
        if (sel) return { prefix: ' ', label: lbl, invert: true };
        return ' ' + lbl.slice(0, 15);
      });

      while (lines.length < 4) lines.push('');

      const last = lines[lines.length - 1];
      lines[lines.length - 1] = typeof last === 'string'
        ? { prefix: '', label: last, sep: true }
        : { ...last, sep: true };

      lines.push('⚙EXIT    ↵SELECT');
      return lines;
    },
  });
}
