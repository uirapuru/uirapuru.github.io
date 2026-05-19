// js/screens/ballistics-mode.js
import { lcd5, rjust, center } from '../lcd.js';
import { calculateTrajectory } from './ballistics.js';

const TGT_FIELDS = [
  { key:'tr',   label:'TR...',   step:10,  min:0,    src:'target', fmt:v=>`${v}m` },
  { key:'dof',  label:'DoF...',  step:30,  src:'target',
    fmt:v=>{ const d=((Math.round(v??0)%360)+360)%360; return `${String(d).padStart(3,'0')}°`; } },
  { key:'ideg', label:'Ideg...', step:1,   src:'target',
    fmt:v=>`${v>=0?'+':''}${v}°` },
  { key:'icos', label:'Icos...', step:0.01, src:'target', fmt:v=>v.toFixed(3) },
  { key:'ts',   label:'TS...',   step:0.1, min:0,    src:'target', fmt:v=>`${v.toFixed(1)} m/s` },
];

const TGT_COUNT = 1 + TGT_FIELDS.length; // A1st Quick Set + 5 data fields

const WIND_FIELDS = [
  { key:'wd',  label:'WD',  step:30,            src:'target',
    fmt:v=>{ const h=Math.round(((v??0)%360)/30)||12; return `${h}:00`; } },
  { key:'ws1', label:'WS1', step:0.5, min:0,    src:'target', fmt:v=>v.toFixed(1)+'m/s' },
  { key:'ws2', label:'WS2', step:0.5, min:0,    src:'target', fmt:v=>v.toFixed(1)+'m/s' },
];

const GUN_FIELDS = [
  { key:'mv',    label:'MV',    step:1,     min:0,     src:'gun', fmt:v=>v+'m/s' },
  { key:'dm',    label:'DM',    toggle:['G1','G7'],               src:'gun' },
  { key:'bc',    label:'BC',    step:0.001, min:0,     src:'gun', fmt:v=>v.toFixed(3) },
  { key:'bw',    label:'BW',    step:1,     min:0,     src:'gun', fmt:v=>v+'gr' },
  { key:'bd',    label:'BD',    step:0.01,  min:0,     src:'gun', fmt:v=>v.toFixed(2)+'mm' },
  { key:'bl',    label:'BL',    step:1,     min:0,     src:'gun', fmt:v=>v+'mm' },
  { key:'zr',    label:'ZR',    step:5,     min:0,     src:'gun', fmt:v=>v+'m' },
  { key:'bh',    label:'BH',    step:1,     min:0,     src:'gun', fmt:v=>v+'mm' },
  { key:'zh',    label:'ZH',    step:0.1,              src:'gun', fmt:v=>v.toFixed(1)+'mil' },
  { key:'zo',    label:'ZO',    step:0.1,              src:'gun', fmt:v=>v.toFixed(1)+'mil' },
  { key:'rt',    label:'RT',    step:0.5,   min:0,     src:'gun', fmt:v=>v+'"' },
  { key:'rtd',   label:'RTd',   toggle:['right','left'],          src:'gun' },
  { key:'eunit', label:'Eunit', toggle:['MIL','TMOA','SMOA'],     src:'gun' },
  { key:'eclk',  label:'Eclk',  step:0.05,  min:0,     src:'gun', fmt:v=>v.toFixed(2) },
  { key:'wunit', label:'Wunit', toggle:['MIL','TMOA','SMOA'],     src:'gun' },
  { key:'wclk',  label:'Wclk',  step:0.05,  min:0,     src:'gun', fmt:v=>v.toFixed(2) },
];

const ENVIRO_FIELDS = [
  { key:'mode',      label:'Update',  toggle:['lock','live'],                    src:'enviro' },
  { key:'lat',       label:'Lat',     step:1,   min:-90,  max:90,   src:'enviro',  fmt:v=>v+'deg' },
  { key:'temp',      label:'Temp',    step:0.1,                     src:'weather', fmt:v=>v.toFixed(1)+'C' },
  { key:'pres',      label:'SP',      step:1,   min:0,              src:'weather', fmt:v=>v.toFixed(0)+'hPa' },
  { key:'hum',       label:'RH',      step:1,   min:0,    max:100,  src:'weather', fmt:v=>v.toFixed(0)+'%' },
  { key:'dalt',      label:'Dalt',    step:10,  src:'enviro',  fmt:v=>v+'ft' },
  { key:'spinDrift', label:'SpnDft',  toggle:[true,false],     src:'enviro' },
  { key:'wcap',      label:'Wcap',    toggle:['one','all'],    src:'enviro' },
];

const BAL_KEYS = ['Range','Elv','Wnd1','Wnd2','RTrns','RSubs','MaxO','AerJ',
                  'vCor','hCor','SpnD','Trce','Drop','Lead','ToF','RemV','RemE'];

// canEnter:true → invert gdy zaznaczone; tgtView:true → otwiera dedykowany widok Target
const MENU_ITEMS = [
  { id:'Tgt',         label:'Tgt...',         tgtView:true,         canEnter:true,
    quick:{ display: s => { const h=Math.round(((s.target.wd??0)%360)/30)||12; return `${h}:00 ${s.target.tr}m`; },
            key:'tr', src:'target', step:10, min:0 } },
  { id:'Wind',        label:'Wind',           fields:WIND_FIELDS,   canEnter:true,
    quick:{ display: s => { const h=Math.round(((s.target.wd??0)%360)/30)||12;
                             return `${h}:00 ${(s.target.ws1??0).toFixed(1)}m/s`; },
            key:'ws1', src:'target', step:0.5, min:0 } },
  { id:'Gun',         label:'Gun...',          fields:GUN_FIELDS,    canEnter:true,
    quick:{ type:'gun-select' } },
  { id:'Enviro',      label:'Enviro',          fields:ENVIRO_FIELDS, canEnter:true,
    quick:{ display: s => { const t=Math.round(s.weather?.temp??0);
                             const m=(s.enviro?.mode==='live')?'Live':'Lock';
                             return `${t}C ${m}`; },
            key:'mode', src:'enviro', toggle:['lock','live'] } },
  { id:'Range Card',  label:'Range Card...',   push:'range-card',    canEnter:true },
  { id:'Target Card', label:'Target Card...',  push:'target-card',   canEnter:true },
  { id:'Accrcy 1st',  label:'Accrcy 1st...',   push:'accuracy-1st',  canEnter:true,
    disabled: s => s.enviro?.mode === 'live' },
  { id:'Ballistics',  label:'Ballistics...',    view:'bal-result',    canEnter:true },
  { id:'Manage Guns', label:'Manage Guns...',  view:'manage-guns',   canEnter:true },
];

function getObj(src, state) {
  if (src === 'gun')     return state.gun;
  if (src === 'target')  return state.target;
  if (src === 'weather') return state.weather;
  if (src === 'enviro')  return state.enviro;
  return {};
}

function fieldVal(f, state) {
  const v = getObj(f.src, state)[f.key];
  if (f.toggle) return String(v ?? f.toggle[0]);
  return f.fmt ? f.fmt(v ?? 0) : String(v ?? '');
}

function adjField(f, dir, state, ctx) {
  if (f.src === 'weather' && state.enviro.mode === 'live') return;
  const obj = { ...getObj(f.src, state) };
  if (f.toggle) {
    const vals = f.toggle;
    const i = vals.indexOf(obj[f.key]);
    obj[f.key] = vals[(i + dir + vals.length) % vals.length];
  } else {
    obj[f.key] = +((obj[f.key] ?? 0) + dir * f.step).toFixed(6);
    if (f.min !== undefined) obj[f.key] = Math.max(f.min, obj[f.key]);
    if (f.max !== undefined) obj[f.key] = Math.min(f.max, obj[f.key]);
  }
  const setters = { gun:ctx.setGun, target:ctx.setTarget, weather:ctx.setWeather, enviro:ctx.setEnviro };
  setters[f.src]?.(obj);
}

function windRL(wd) {
  const a = ((wd ?? 0) % 360 + 360) % 360;
  if (a === 0 || a === 180) return '';
  return (a > 0 && a < 180) ? 'R' : 'L';
}

function quickVal(item, state) {
  if (!item.quick) return '';
  const q = item.quick;
  if (q.type === 'gun-select') return state.gun.name.replace(/\s+/g, '');
  if (q.display) return q.display(state);
  if (q.toggle) return String(getObj(q.src, state)[q.key] ?? q.toggle[0]);
  const v = getObj(q.src, state)[q.key] ?? 0;
  return q.fmt ? q.fmt(v) : String(v);
}

function adjQuick(item, dir, state, ctx) {
  if (!item.quick) return;
  const q = item.quick;
  if (q.type === 'gun-select') {
    const guns = state.guns;
    if (!guns || guns.length <= 1) return;
    const newIdx = (state.gunIdx + dir + guns.length) % guns.length;
    ctx.setState({ gunIdx: newIdx, gun: { ...guns[newIdx] } });
    return;
  }
  if (!q.key) return;
  const obj = { ...getObj(q.src, state) };
  if (q.toggle) {
    const i = q.toggle.indexOf(obj[q.key]);
    obj[q.key] = q.toggle[(i + dir + q.toggle.length) % q.toggle.length];
  } else {
    obj[q.key] = +((obj[q.key] ?? 0) + dir * q.step).toFixed(6);
    if (q.min !== undefined) obj[q.key] = Math.max(q.min, obj[q.key]);
    if (q.max !== undefined) obj[q.key] = Math.min(q.max, obj[q.key]);
  }
  const setters = { gun:ctx.setGun, target:ctx.setTarget, weather:ctx.setWeather, enviro:ctx.setEnviro };
  setters[q.src]?.(obj);
}

function calcResult(state) {
  const g = state.gun, t = state.target, w = state.weather, e = state.enviro;
  const baseParams = {
    distanceMeters: t.tr, slopeAngleDegrees: t.ideg || 0,
    windDirectionDegrees: t.wd || w.wdir || 90,
    temperatureC: w.temp || 15, pressureHpa: w.pres || 1013, humidityPercent: w.hum || 50,
    latitudeDegrees: e.lat || 52, targetAzimuthDegrees: t.dof || 0,
    zeroDistanceMeters: g.zr, scopeHeightMm: g.bh, muzzleVelocityMps: g.mv,
    bulletWeightGrains: g.bw, ballisticCoefficient: g.bc, dragModel: g.dm,
    twistRateInches: g.rt, twistDirection: g.rtd, gyroscopicStabilityFactor: 1.5,
    zeroOffsetXmm: 0, zeroOffsetYmm: g.zh || 0, zeroTemperatureC: 15,
    clickVerticalMRAD: g.eclk, clickHorizontalMRAD: g.wclk,
    horizontalWindDriftPercent: 10, considerPowderTemperature: false,
    showSMOAInsteadOfMOA: false, addTailwindHeadwindToBulletSpeed: true,
    addVerticalDeflectionOfCrosswind: true, setRelationManually: false,
    addSpinDrift: e.spinDrift !== false, addCoriolisEffect: true,
    useUDLRInsteadOfPlusMinus: true,
  };
  let r = null, r2 = null;
  try { r = calculateTrajectory({ ...baseParams, windSpeedMps: t.ws1 || w.wind || 0 }); } catch(_) {}
  try { r2 = calculateTrajectory({ ...baseParams, windSpeedMps: t.ws2 || 0 }); } catch(_) {}
  if (!r) return null;

  const sosMps = 331 + 0.6 * (w.temp || 15);
  const mvFps = g.mv * 3.281;
  const remFps = r.retainedVelocityFps || 0;
  const tr = t.tr || 1;
  const mach12Fps = sosMps * 3.281 * 1.2;
  const mach10Fps = sosMps * 3.281;
  let rTrnsM = null, rSubsM = null;
  if (mvFps > mach12Fps && remFps < mach12Fps)
    rTrnsM = Math.round(tr * (mvFps - mach12Fps) / Math.max(0.1, mvFps - remFps));
  if (mvFps > mach10Fps && remFps < mach10Fps)
    rSubsM = Math.round(tr * (mvFps - mach10Fps) / Math.max(0.1, mvFps - remFps));

  const zrM = g.zr || 100;
  const bhMil = (g.bh || 50) / 1000 / tr * 1000;
  const maxO_mil = tr < zrM ? (bhMil * tr / zrM * (1 - tr / zrM) * 4).toFixed(2) : '0.00';

  const wd_rad = ((t.wd || 0) % 360) * Math.PI / 180;
  const crossWind = Math.abs(Math.sin(wd_rad)) * (t.ws1 || 0);
  const aerJ_mil = (crossWind * 0.003 / Math.max(0.1, g.bc)).toFixed(3);

  const leadMil = ((t.ts || 0) * (r.timeOfFlightSec || 0) / tr * 1000).toFixed(2);

  r._ext = { r2, rTrnsM, rSubsM, maxO_mil, aerJ_mil, leadMil };
  return r;
}

function renderFields(fields, fi, state) {
  const start = Math.max(0, fi - 1);
  return fields.slice(start, start + 4).map((f, i) => {
    const idx = start + i;
    const sel = idx === fi;
    const isLive = f.src === 'weather' && state.enviro.mode === 'live';
    const valStr = isLive ? `~${fieldVal(f, state)}` : fieldVal(f, state);
    const text = rjust(f.label.slice(0, 7), valStr.slice(0, 8));
    if (sel) return { text, invert: true };
    return text;
  });
}

let view = 'main';
let menuIdx = 0;
let fieldIdx = 0;
let activeFields = null;
let delConfirm = false;
let windCaptureActive = false;
let windCaptureTimer = null;
let windCaptureCtx = null;
let mgSubIdx = 0;
let gunListIdx = 0;
let gunDelTarget = -1;
let trEstField = 0;
let trEstTgtSize = 0.50;
let trEstMils = 4.0;

export function registerBallistics(menu) {
  menu.register('ballistics-mode', {
    onEnter() {
      view = 'main'; menuIdx = 0; fieldIdx = 0;
      delConfirm = false; mgSubIdx = 0; gunListIdx = 0; gunDelTarget = -1;
      if (windCaptureTimer) { clearInterval(windCaptureTimer); windCaptureTimer = null; }
      windCaptureActive = false; windCaptureCtx = null;
    },

    onUp() {
      if (view === 'main')       { menuIdx = Math.max(0, menuIdx - 1); return; }
      if (view === 'tgt-fields') { fieldIdx = Math.max(-1, fieldIdx - 1); return; }
      if (view === 'tr-estimate') { trEstField = 0; return; }
      if (view === 'fields' || view === 'bal-result') { fieldIdx = Math.max(0, fieldIdx - 1); }
      if (view === 'manage-guns') { mgSubIdx = Math.max(0, mgSubIdx - 1); delConfirm = false; return; }
      if (view === 'gun-list') { gunListIdx = Math.max(0, gunListIdx - 1); gunDelTarget = -1; return; }
    },
    onDown() {
      if (view === 'main')       { menuIdx = Math.min(MENU_ITEMS.length - 1, menuIdx + 1); return; }
      if (view === 'tgt-fields') { fieldIdx = Math.min(TGT_COUNT - 1, fieldIdx + 1); return; }
      if (view === 'tr-estimate') { trEstField = 1; return; }
      if (view === 'fields')     { fieldIdx = Math.min(activeFields.length - 1, fieldIdx + 1); return; }
      if (view === 'bal-result') { fieldIdx = Math.min(BAL_KEYS.length - 1, fieldIdx + 1); }
      if (view === 'manage-guns') { mgSubIdx = Math.min(1, mgSubIdx + 1); delConfirm = false; return; }
      if (view === 'gun-list') { gunListIdx++; gunDelTarget = -1; return; }
    },
    onLeft(ctx) {
      if (view === 'main')       { adjQuick(MENU_ITEMS[menuIdx], -1, ctx.state, ctx); return; }
      if (view === 'tgt-fields') {
        if (fieldIdx === -1) {
          ctx.setState({ targetCardIdx: ((ctx.state.targetCardIdx ?? 0) - 1 + 10) % 10 });
          return;
        }
        if (fieldIdx > 0) adjField(TGT_FIELDS[fieldIdx - 1], -1, ctx.state, ctx);
        return;
      }
      if (view === 'tr-estimate') {
        if (trEstField === 0) trEstTgtSize = Math.max(0.1, +(trEstTgtSize - 0.1).toFixed(1));
        else trEstMils = Math.max(0.1, +(trEstMils - 0.1).toFixed(1));
        return;
      }
      if (view === 'gun-list') {
        const guns = ctx.state.guns;
        if (gunListIdx < guns.length && guns.length > 1) {
          gunDelTarget = (gunDelTarget === gunListIdx) ? -1 : gunListIdx;
        }
        return;
      }
      if (view === 'fields')     { adjField(activeFields[fieldIdx], -1, ctx.state, ctx); }
    },
    onRight(ctx) {
      if (view === 'main')       { adjQuick(MENU_ITEMS[menuIdx], +1, ctx.state, ctx); return; }
      if (view === 'tgt-fields') {
        if (fieldIdx === -1) {
          ctx.setState({ targetCardIdx: ((ctx.state.targetCardIdx ?? 0) + 1) % 10 });
          return;
        }
        if (fieldIdx > 0) adjField(TGT_FIELDS[fieldIdx - 1], +1, ctx.state, ctx);
        return;
      }
      if (view === 'tr-estimate') {
        if (trEstField === 0) trEstTgtSize = +(trEstTgtSize + 0.1).toFixed(1);
        else trEstMils = +(trEstMils + 0.1).toFixed(1);
        return;
      }
      if (view === 'fields')     { adjField(activeFields[fieldIdx], +1, ctx.state, ctx); }
    },

    onSelect(ctx) {
      if (view === 'main') {
        const item = MENU_ITEMS[menuIdx];
        if (item.disabled?.(ctx.state)) return;
        if (item.tgtView) { view = 'tgt-fields'; fieldIdx = -1; return; }
        if (item.push)    { ctx.push(item.push); return; }
        if (item.view)    { view = item.view; fieldIdx = 0; return; }
        if (item.fields)  { activeFields = item.fields; view = 'fields'; fieldIdx = 0; }
        return;
      }
      if (view === 'tgt-fields') {
        if (fieldIdx === -1) { fieldIdx = 0; return; }
        if (fieldIdx === 0) {
          view = 'a1st-flash';
          ctx.render();
          setTimeout(() => {
            if (view === 'a1st-flash') {
              ctx.setTarget({ dof: 0, ideg: 0, icos: 1, ws1: 0, ws2: 1.8, wd: 90 });
              ctx.setEnviro({ spinDrift: false });
              view = 'tgt-fields';
              ctx.render();
            }
          }, 1000);
          return;
        }
        if (fieldIdx === 1) {
          view = 'tr-estimate';
          trEstField = 0;
          return;
        }
        return;
      }
      if (view === 'tr-estimate') {
        const estTr = trEstMils > 0 ? Math.round(trEstTgtSize * 1000 / trEstMils) : 0;
        ctx.setTarget({ tr: estTr });
        view = 'tgt-fields';
        fieldIdx = 1;
        return;
      }
      if (view === 'manage-guns') {
        if (mgSubIdx === 0) {
          view = 'gun-list'; gunListIdx = ctx.state.gunIdx; gunDelTarget = -1;
          return;
        }
        if (delConfirm) {
          const def = { name:'GUN 1', mv:800, dm:'G1', bc:0.447, bw:168, bd:7.82, bl:150,
            zr:100, bh:50, zh:0, zo:0, rt:12, rtd:'right',
            eunit:'MIL', eclk:0.1, wunit:'MIL', wclk:0.1, mvTemp:15, calDsf:1.0 };
          ctx.setState({ guns:[def], gunIdx:0, gun:{ ...def } });
          delConfirm = false; view = 'main';
        } else { delConfirm = true; }
        return;
      }
      if (view === 'gun-list') {
        const guns = ctx.state.guns;
        const total = guns.length + (guns.length < 16 ? 1 : 0);
        gunListIdx = Math.min(gunListIdx, total - 1);
        if (gunDelTarget === gunListIdx && gunListIdx < guns.length) {
          if (guns.length <= 1) { gunDelTarget = -1; return; }
          const newGuns = guns.filter((_, i) => i !== gunListIdx);
          const newIdx = Math.min(ctx.state.gunIdx, newGuns.length - 1);
          ctx.setState({ guns: newGuns, gunIdx: newIdx, gun: { ...newGuns[newIdx] } });
          gunListIdx = Math.min(gunListIdx, newGuns.length);
          gunDelTarget = -1;
          return;
        }
        gunDelTarget = -1;
        if (gunListIdx < guns.length) {
          ctx.setState({ gunIdx: gunListIdx, gun: { ...guns[gunListIdx] } });
          return;
        }
        if (guns.length >= 16) return;
        const newGun = { name:`GUN ${guns.length + 1}`, mv:800, dm:'G1', bc:0.447, bw:168,
          bd:7.82, bl:150, zr:100, bh:50, zh:0, zo:0, rt:12, rtd:'right',
          eunit:'MIL', eclk:0.1, wunit:'MIL', wclk:0.1, mvTemp:15, calDsf:1.0 };
        const newGuns = [...guns, newGun];
        ctx.setState({ guns: newGuns });
        gunListIdx = newGuns.length - 1;
        return;
      }
    },

    onOptions(ctx) {
      if (view === 'tr-estimate') { view = 'tgt-fields'; fieldIdx = 1; return; }
      if (view === 'tgt-fields') {
        if (fieldIdx >= 0) { fieldIdx = -1; return; }
        view = 'main'; return;
      }
      if (view === 'a1st-flash') { view = 'tgt-fields'; fieldIdx = 0; return; }
      if (view === 'gun-list') { view = 'manage-guns'; gunDelTarget = -1; return; }
      if (view !== 'main') { view = 'main'; delConfirm = false; return; }
      ctx.defaultOptions();
    },

    onCapture(ctx) {
      if (view === 'tgt-fields' && fieldIdx > 0) {
        const f = TGT_FIELDS[fieldIdx - 1];
        if (f && f.key === 'dof') {
          const captured = Math.round(Math.random() * 12) * 30;
          ctx.setTarget({ dof: captured });
        }
        return;
      }
      if (view === 'main' && MENU_ITEMS[menuIdx].id === 'Wind') {
        if (windCaptureActive) {
          clearInterval(windCaptureTimer);
          windCaptureTimer = null;
          windCaptureActive = false;
          windCaptureCtx = null;
        } else {
          windCaptureActive = true;
          windCaptureCtx = ctx;
          windCaptureTimer = setInterval(() => {
            if (!windCaptureCtx) return;
            const base = windCaptureCtx.state.weather.wind || 3;
            const ws1 = Math.max(0, +(base + (Math.random() - 0.5) * 0.6).toFixed(1));
            const ws2 = +Math.max(ws1, ws1 + Math.random() * 0.4).toFixed(1);
            windCaptureCtx.setTarget({ ws1, ws2 });
          }, 1000);
        }
        ctx.render();
        return;
      }
    },

    render(state) {
      const r = calcResult(state);

      // ── Widok główny menu ballistics ──────────────────────────────────
      if (view === 'main') {
        const elv = r ? r.dropDirectionTextMRAD.slice(0, 5).padEnd(5) : '  ---';
        const bt  = state.bluetooth ? 'B' : ' ';
        const tgt = String.fromCharCode(65 + Math.min(state.targetCardIdx ?? 0, 9));
        const elvStr = `E ${elv} mil ${bt}[${tgt}]`;

        const ws1f = (state.target.ws1 ?? 0).toFixed(1);
        const ws2f = (state.target.ws2 ?? 0).toFixed(2);
        const rl   = windRL(state.target.wd);
        const wndStr = `W ${ws1f}/${ws2f}${rl}`;

        const maxStart = Math.max(0, MENU_ITEMS.length - 3);
        const start = Math.min(Math.max(0, menuIdx - 1), maxStart);
        const visible = MENU_ITEMS.slice(start, start + 3);

        const menuLines = visible.map((item, i) => {
          const idx = start + i;
          const sel = idx === menuIdx;
          const label = (item.id === 'Wind' && windCaptureActive) ? 'Wind ▶' : item.label;
          const text = rjust(label, quickVal(item, state));
          if (!sel) return text;
          if (item.disabled?.(state)) return { text, underline: true };
          return { text, invert: true };
        });
        while (menuLines.length < 3) menuLines.push('');

        // separator zawsze na nagłówku (linia 2), nie na pierwszym elemencie menu
        return lcd5([
          elvStr,
          { text: wndStr, sep: true },
          ...menuLines,
        ]);
      }

      // ── Widok Target z nagłówkiem cyklu A-J ──────────────────────────
      if (view === 'tgt-fields') {
        const tgtChar = String.fromCharCode(65 + Math.min(state.targetCardIdx ?? 0, 9));
        const wStart = fieldIdx < 1
          ? 0
          : Math.max(0, Math.min(fieldIdx - 1, TGT_COUNT - 3));

        // Nagłówek bez separatora i bez strzałek (strzałki są na wierszach pól)
        const hdrLine = { text: `Target... [${tgtChar}]`, invert: fieldIdx === -1 };

        const fieldLines = [];
        for (let i = 0; i < 3; i++) {
          const fi = wStart + i;
          const sel = fi === fieldIdx;

          // Strzałka ▲ na pierwszym wierszu pól (pod nagłówkiem), ▼ na ostatnim (nad stopką)
          const arrowChar = (i === 0 && wStart > 0)              ? '▲'
                          : (i === 2 && wStart + 3 < TGT_COUNT)  ? '▼'
                          : '';

          let text;
          if (arrowChar) {
            const l = fi === 0 ? 'A1st Quik set' : TGT_FIELDS[fi - 1].label;
            const v = String(fi === 0 ? 'Go' : fieldVal(TGT_FIELDS[fi - 1], state));
            const gap = Math.max(0, 15 - l.length - v.length);
            text = (l + ' '.repeat(gap) + v).slice(0, 15) + arrowChar;
          } else {
            text = fi === 0
              ? rjust('A1st Quik set', 'Go')
              : rjust(TGT_FIELDS[fi - 1].label, fieldVal(TGT_FIELDS[fi - 1], state));
          }

          const isLast = i === 2;
          if (sel) {
            fieldLines.push(isLast ? { text, invert: true, sep: true } : { text, invert: true });
          } else {
            fieldLines.push(isLast ? { text, sep: true } : text);
          }
        }

        const actionBar = fieldIdx === -1 ? rjust('⚙EXIT', '◄►NEXT')
                        : fieldIdx === 0   ? rjust('⚙EXIT', '↵GO')
                        :                    rjust('⚙EXIT', '◄►ADJ');

        return lcd5([hdrLine, ...fieldLines, actionBar]);
      }

      // ── TR Estimate podmenu ───────────────────────────────────────────
      if (view === 'tr-estimate') {
        const estTr = trEstMils > 0 ? Math.round(trEstTgtSize * 1000 / trEstMils) : 0;
        return lcd5([
          'TR Estimate',
          { text: rjust('TgtSz(m)', trEstTgtSize.toFixed(1)), invert: trEstField === 0 },
          { text: rjust('ObsMils', trEstMils.toFixed(1)),     invert: trEstField === 1 },
          rjust('Est TR', estTr + 'm'),
          '⚙=back  ↵=Accept',
        ]);
      }

      // ── Flash potwierdzenia A1st ──────────────────────────────────────
      if (view === 'a1st-flash') {
        return lcd5(['', '', center('Success!!!'), '', '']);
      }

      // ── Widok edycji pól (Wind / Gun / Enviro) ────────────────────────
      if (view === 'fields') {
        const item = MENU_ITEMS[menuIdx];
        const fl = renderFields(activeFields, fieldIdx, state);
        while (fl.length < 4) fl.push('');
        return lcd5([`< ${item.label.padEnd(12)}>`, ...fl]);
      }

      // ── Widok wyników balistycznych ───────────────────────────────────
      if (view === 'bal-result') {
        if (!r) return lcd5(['Ballistics', 'Error', '', '', '']);
        const ext = r._ext || {};
        const r2  = ext.r2;
        const vals = {
          Range: `${state.target.tr}m`,
          Elv:   r.dropDirectionTextMRAD,
          Wnd1:  r.windDirectionTextMRAD,
          Wnd2:  r2 ? r2.windDirectionTextMRAD : '---',
          RTrns: ext.rTrnsM != null ? `${ext.rTrnsM}m` : '>TR',
          RSubs: ext.rSubsM != null ? `${ext.rSubsM}m` : '>TR',
          MaxO:  `${ext.maxO_mil}mil`,
          AerJ:  `${ext.aerJ_mil}mil`,
          vCor:  (r.coriolisVerticalMOA || 0).toFixed(2) + 'MOA',
          hCor:  r.coriolisHorizontalMOA != null ? r.coriolisHorizontalMOA.toFixed(2) + 'MOA' : '---',
          SpnD:  r.spinDriftMOA?.toFixed(2) ?? '---',
          Trce:  r.dropInches != null ? (r.dropInches * 0.55).toFixed(1) + '"' : '---',
          Drop:  r.dropInches?.toFixed(1) + '"',
          Lead:  `${ext.leadMil}mil`,
          ToF:   r.timeOfFlightSec?.toFixed(2) + 's',
          RemV:  r.retainedVelocityFps?.toFixed(0) + 'fps',
          RemE:  r.retainedEnergyFtLb?.toFixed(0) + 'ftlb',
        };
        const bstart = Math.max(0, fieldIdx - 1);
        const lines = BAL_KEYS.slice(bstart, bstart + 4).map((k, i) => {
          const sel = (bstart + i === fieldIdx);
          const text = rjust(k.slice(0, 7), (vals[k] ?? '---').slice(0, 8));
          if (sel) return { text, invert: true };
          return text;
        });
        while (lines.length < 4) lines.push('');
        return lcd5(['Ballistics', ...lines]);
      }

      // ── Widok Manage Guns ─────────────────────────────────────────────
      if (view === 'manage-guns') {
        const items = ['Gun List...', delConfirm ? 'Delete All? ↵=YES' : 'Delete All'];
        const lines = items.map((l, i) => {
          const sel = i === mgSubIdx;
          return sel ? { text: ` ${l}`.padEnd(16), invert: true } : ` ${l}`;
        });
        return lcd5(['Manage Guns', ...lines, '', '⚙=back']);
      }

      if (view === 'gun-list') {
        const guns = state.guns;
        const hasNew = guns.length < 16;
        const total = guns.length + (hasNew ? 1 : 0);
        const clampedIdx = Math.min(gunListIdx, total - 1);
        const wStart = Math.max(0, Math.min(clampedIdx - 1, total - 3));
        const lines = [];
        for (let i = 0; i < 3; i++) {
          const fi = wStart + i;
          if (fi >= total) { lines.push(''); continue; }
          const sel = fi === clampedIdx;
          let text;
          if (fi < guns.length) {
            const isActive = fi === state.gunIdx;
            const delPending = gunDelTarget === fi;
            text = delPending
              ? 'Delete? ↵=YES'.padEnd(16)
              : `${isActive ? '[On]' : '[ ] '} ${guns[fi].name}`.slice(0, 16);
          } else {
            text = '[ New Gun ]';
          }
          lines.push(sel ? { text, invert: true } : text);
        }
        while (lines.length < 3) lines.push('');
        return lcd5(['Gun List', ...lines, hasNew ? '◄DEL ↵SEL/NEW' : '◄DEL ↵SEL']);
      }

      return lcd5(['Ballistics', '', '', '', '']);
    },
  });
}
