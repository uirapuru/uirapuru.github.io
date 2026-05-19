// js/screens/weather.js
import { lcd5, center } from '../lcd.js';

const MEASURES = [
  { key:'datetime',  label:'Date & Time', unit:'',    fmt:()  => new Date().toLocaleTimeString('pl',{hour:'2-digit',minute:'2-digit'}) },
  { key:'direction', label:'Direction',   unit:'deg', fmt:(w) => String((w.wdir??0)|0) },
  { key:'windSpd',   label:'Wind Spd',    unit:'m/s', fmt:(w) => (w.wind??0).toFixed(1) },
  { key:'crosswnd',  label:'Crosswnd',    unit:'m/s', fmt:(w) => (Math.abs(Math.sin((w.wdir||0)*Math.PI/180))*(w.wind||0)).toFixed(1) },
  { key:'headwnd',   label:'Headwnd',     unit:'m/s', fmt:(w) => (Math.abs(Math.cos((w.wdir||0)*Math.PI/180))*(w.wind||0)).toFixed(1) },
  { key:'temp',      label:'Temperature', unit:'°C', fmt:(w) => (w.temp??0).toFixed(1) },
  { key:'windChill', label:'Wind Chill',  unit:'°C', fmt:(w) => (w.windChill??0).toFixed(1) },
  { key:'hum',       label:'Humidity',    unit:'%',   fmt:(w) => (w.hum??0).toFixed(0) },
  { key:'heatIndex', label:'Heat Index',  unit:'°C', fmt:(w) => (w.heatIndex??0).toFixed(1) },
  { key:'dewPoint',  label:'Dew Point',   unit:'°C', fmt:(w) => (w.dewPoint??0).toFixed(1) },
  { key:'wetBulb',   label:'Wet Bulb',    unit:'°C', fmt:(w) => (w.wetBulb??0).toFixed(1) },
  { key:'station',   label:'Station Pres',unit:'hPa', fmt:(w) => (w.station??0).toFixed(1) },
  { key:'baroPres',  label:'Baro Pres',   unit:'hPa', fmt:(w) => (w.pres??0).toFixed(1) },
  { key:'alt',       label:'Altitude',    unit:'m',   fmt:()  => '---' },
  { key:'densAlt',   label:'Density Alt', unit:'ft',  fmt:(w) => (w.densAlt??0).toFixed(0) },
  { key:'user1',     label:'User Scrn 1', unit:'',    fmt:(w,s) => getUserLine(s,0,w) },
  { key:'user2',     label:'User Scrn 2', unit:'',    fmt:(w,s) => getUserLine(s,1,w) },
  { key:'user3',     label:'User Scrn 3', unit:'',    fmt:(w,s) => getUserLine(s,2,w) },
];

const USER_LABELS = MEASURES.slice(0, 15).map(m => m.label);

function getUserLine(state, uIdx, w) {
  const rows = state.userScreens?.[uIdx] ?? ['Wind Spd','Temperature','Humidity'];
  return rows.map(r => {
    const m = MEASURES.find(x => x.label === r);
    return m ? m.fmt(w, state) : '---';
  }).join(' ');
}

const tracker = {};
MEASURES.forEach(m => { tracker[m.key] = { min:null, max:null, sum:0, count:0 }; });

function trackVal(key, rawVal) {
  const v = parseFloat(rawVal);
  if (isNaN(v)) return;
  const t = tracker[key];
  if (t.min === null || v < t.min) t.min = v;
  if (t.max === null || v > t.max) t.max = v;
  t.sum += v; t.count++;
}

let mIdx = 0;
let subView = 'main'; // 'main' | 'minmax' | 'datalog' | 'graph' | 'user-cfg'
let userRow = 0;

export function registerWeather(menu) {
  menu.register('weather', {
    onEnter() { subView = 'main'; },

    onUp()   { if (subView === 'main') mIdx = (mIdx - 1 + MEASURES.length) % MEASURES.length; },
    onDown() { if (subView === 'main') mIdx = (mIdx + 1) % MEASURES.length; },

    onLeft(ctx) {
      if (subView === 'main') { subView = 'minmax'; return; }
      if (subView === 'user-cfg') _cycleUserRow(ctx, -1);
    },
    onRight(ctx) {
      if (subView === 'main') { subView = 'minmax'; return; }
      if (subView === 'user-cfg') _cycleUserRow(ctx, +1);
    },

    onSelect(ctx) {
      if (subView === 'main') {
        subView = mIdx >= 15 ? 'user-cfg' : 'minmax';
        userRow = 0;
        return;
      }
      if (subView === 'minmax') { subView = 'datalog'; return; }
      if (subView === 'datalog') { subView = 'graph'; return; }
      if (subView === 'graph')   { subView = 'main'; return; }
      if (subView === 'user-cfg') {
        userRow = (userRow + 1) % 3;
        if (userRow === 0) subView = 'main';
      }
    },

    onOptions(ctx) {
      if (subView !== 'main') { subView = 'main'; return; }
      ctx.defaultOptions();
    },

    render(state) {
      const m = MEASURES[mIdx];
      const w = state.weather;
      const val = m.fmt(w, state);
      trackVal(m.key, val);
      const hdr = (m.label + ' ' + m.unit).slice(0, 16);

      if (subView === 'main') {
        const hint = mIdx >= 15 ? '<->Cfg    SEL->' : '<->MinMax SEL->';
        return lcd5([hdr, '', center(val), '', hint]);
      }

      if (subView === 'minmax') {
        const t = tracker[m.key];
        const f = v => v === null ? '---' : v.toFixed(1);
        const avg = t.count ? (t.sum / t.count).toFixed(1) : '---';
        return lcd5([hdr, `Min  ${f(t.min)}`, `Avg  ${avg}`, `Max  ${f(t.max)}`, '<-bk  SEL->log']);
      }

      if (subView === 'datalog') {
        const ts = new Date().toLocaleTimeString('pl',{hour:'2-digit',minute:'2-digit',second:'2-digit'});
        return lcd5([m.label + ' Log', ts, `${val} ${m.unit}`.slice(0,16), '', 'SEL graph <-bk']);
      }

      if (subView === 'graph') {
        return lcd5([m.label, '', center('Graph N/A'), '', 'SEL back']);
      }

      if (subView === 'user-cfg') {
        const uIdx = mIdx - 15;
        const rows = state.userScreens[uIdx];
        return lcd5([
          `User Screen ${uIdx + 1}`,
          (userRow===0?'►':' ')+'R1:'+rows[0].slice(0,12),
          (userRow===1?'►':' ')+'R2:'+rows[1].slice(0,12),
          (userRow===2?'►':' ')+'R3:'+rows[2].slice(0,12),
          '<->chg SEL next',
        ]);
      }

      return lcd5(['Weather','','','','']);
    }
  });
}

function _cycleUserRow(ctx, dir) {
  const uIdx = mIdx - 15;
  const s = ctx.state;
  const rows = [...s.userScreens[uIdx]];
  const cur = USER_LABELS.indexOf(rows[userRow]);
  rows[userRow] = USER_LABELS[(cur + dir + USER_LABELS.length) % USER_LABELS.length];
  const us = s.userScreens.map((r, i) => i === uIdx ? rows : r);
  ctx.setState({ userScreens: us });
}
