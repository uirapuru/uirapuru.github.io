// js/screens/easy.js
import { lcd5, center } from '../lcd.js';

const ITEMS = ['Tgt Range','Target Setup','Profile Name','Cal MV Guide','Compass Cal','Latitude'];
const W_TARGET = ['Capture Enviro','Capture DoF','Capture Wind'];
const W_CALMV  = ['Confirm Lat','Capture Enviro','Enter Range','Capture DoF','Capture Wind','Adjust Elev','Accept new MV'];

let view = 'menu'; // 'menu'|'edit-tr'|'edit-lat'|'wiz-target'|'wiz-calmv'|'compass'
let menuIdx = 0;
let wizStep = 0;

export function registerEasy(menu) {
  menu.register('easy', {
    onEnter() { view = 'menu'; menuIdx = 0; wizStep = 0; },

    onUp()   { if (view === 'menu') menuIdx = Math.max(0, menuIdx - 1); },
    onDown() { if (view === 'menu') menuIdx = Math.min(ITEMS.length - 1, menuIdx + 1); },

    onLeft(ctx)  {
      if (view === 'edit-tr')  ctx.setTarget({ tr:  Math.max(0, ctx.state.target.tr  - 10) });
      if (view === 'edit-lat') ctx.setEnviro({ lat: ctx.state.enviro.lat - 1 });
    },
    onRight(ctx) {
      if (view === 'edit-tr')  ctx.setTarget({ tr:  ctx.state.target.tr  + 10 });
      if (view === 'edit-lat') ctx.setEnviro({ lat: ctx.state.enviro.lat + 1 });
    },

    onSelect(ctx) {
      if (view === 'menu') {
        const item = ITEMS[menuIdx];
        if (item === 'Tgt Range')    { view = 'edit-tr'; return; }
        if (item === 'Latitude')     { view = 'edit-lat'; return; }
        if (item === 'Target Setup') { view = 'wiz-target'; wizStep = 0; return; }
        if (item === 'Cal MV Guide') { view = 'wiz-calmv';  wizStep = 0; return; }
        if (item === 'Compass Cal')  { view = 'compass'; return; }
        return;
      }
      if (view === 'wiz-target') {
        wizStep < W_TARGET.length - 1 ? wizStep++ : (view = 'menu');
        return;
      }
      if (view === 'wiz-calmv') {
        wizStep < W_CALMV.length - 1 ? wizStep++ : (view = 'menu');
        return;
      }
    },

    onOptions(ctx) {
      if (view !== 'menu') { view = 'menu'; return; }
      ctx.defaultOptions();
    },

    render(state) {
      if (view === 'menu') {
        const start = Math.max(0, menuIdx - 1);
        const lines = ITEMS.slice(start, start + 4).map((item, i) =>
          (start+i===menuIdx?'►':' ')+item.slice(0,15));
        while (lines.length < 4) lines.push('');
        return lcd5(['EASY MODE', ...lines]);
      }
      if (view === 'edit-tr') {
        return lcd5(['Tgt Range','',center(state.target.tr+'m'),'','<->adj  OPT bk']);
      }
      if (view === 'edit-lat') {
        return lcd5(['Latitude','',center(state.enviro.lat+'deg'),'','<->adj  OPT bk']);
      }
      if (view === 'wiz-target') {
        const steps = W_TARGET;
        return lcd5(['Target Setup',`Step ${wizStep+1}/${steps.length}`,steps[wizStep],'','SEL next OPT bk']);
      }
      if (view === 'wiz-calmv') {
        const steps = W_CALMV;
        return lcd5(['Cal MV Guide',`Step ${wizStep+1}/${steps.length}`,steps[wizStep].slice(0,16),'','SEL next OPT bk']);
      }
      if (view === 'compass') {
        return lcd5(['Compass Cal','Rotate device','slowly 360deg','','OPT back']);
      }
      return lcd5(['Easy Mode','','','','']);
    },
  });
}
