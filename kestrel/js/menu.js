// js/menu.js
const screens = {};
let stack = [];
let state = {
  mode: 'weather',
  backlightRed: false,
  weather: { temp: 15, pres: 1013, hum: 50, wind: 3, wdir: 90 },
  guns: [
    { name: 'GUN 1', mv: 800, dm: 'G1', bc: 0.447, bw: 168, bd: 7.82, bl: 150,
      zr: 100, bh: 50, zh: 0, zo: 0, rt: 12, rtd: 'right',
      eunit: 'MIL', eclk: 0.1, wunit: 'MIL', wclk: 0.1, mvTemp: 15, calDsf: 1.0 },
  ],
  gunIdx: 0,
  gun: {
    name: 'GUN 1', mv: 800, dm: 'G1', bc: 0.447, bw: 168, bd: 7.82, bl: 150,
    zr: 100, bh: 50, zh: 0, zo: 0, rt: 12, rtd: 'right',
    eunit: 'MIL', eclk: 0.1, wunit: 'MIL', wclk: 0.1, mvTemp: 15, calDsf: 1.0,
  },
  target: { tr: 600, dof: 0, ideg: 0, icos: 0, ts: 0, wd: 90, ws1: 3, ws2: 5 },
  enviro: { mode: 'lock', lat: 52, dalt: 0, spinDrift: true, wcap: 'one' },
  graphs: { windSpd: 10, temp: 10, hum: 10, pres: 10, alt: 10, densAlt: 10 },
  memory: { autoStore: false, storeRate: 1, overwrite: true },
  userScreens: [
    ['Wind Spd', 'Temperature', 'Humidity'],
    ['Wind Spd', 'Temperature', 'Humidity'],
    ['Wind Spd', 'Temperature', 'Humidity'],
  ],
  targetCards: Array.from({ length: 10 }, () => ({
    tr: 500, dof: 0, ideg: 0, ts: 0,
    windDir: 90, windSpd: 3, windSpd2: 5, designator: '',
  })),
  targetCardIdx: 0,
  bluetooth: false,
  rngIncrement: 100,
};

function escapeHtml(str) {
  return String(str).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

function renderLCD() {
  const lcd = document.getElementById('lcd-content');
  if (!stack.length) { lcd.textContent = ''; return; }
  const screen = screens[stack[stack.length - 1]];
  if (!screen) return;
  const lines = screen.render(state);
  if (lines === null) return;

  if (!Array.isArray(lines)) {
    lcd.textContent = String(lines ?? '');
    lcd.className = state.backlightRed ? 'backlight-red' : '';
    return;
  }

  lcd.innerHTML = lines.map(line => {
    if (typeof line === 'string') {
      return `<div class="lcd-line">${escapeHtml(line)}</div>`;
    }
    // {prefix, label, invert?, sep?} — only label gets invert span
    if (line.prefix !== undefined || (line.label !== undefined && line.text === undefined)) {
      const cls = ['lcd-line'];
      if (line.sep) cls.push('lcd-sep');
      const inner = escapeHtml(line.prefix ?? '') +
        (line.invert
          ? `<span class="lcd-invert">${escapeHtml(line.label ?? '')}</span>`
          : escapeHtml(line.label ?? ''));
      return `<div class="${cls.join(' ')}">${inner}</div>`;
    }
    // {text, invert?, underline?, sep?} — full-line styling
    const cls = ['lcd-line'];
    if (line.invert) cls.push('lcd-invert');
    if (line.underline) cls.push('lcd-underline');
    if (line.sep) cls.push('lcd-sep');
    return `<div class="${cls.join(' ')}">${escapeHtml(line.text ?? '')}</div>`;
  }).join('');
  lcd.className = state.backlightRed ? 'backlight-red' : '';
}

function makeCtx() {
  const ctx = {
    get state() { return state; },
    push(name) {
      if (!screens[name]) { console.warn('Unknown screen:', name); return; }
      screens[name].onEnter?.(makeCtx());
      stack.push(name);
      renderLCD();
    },
    pop() {
      if (stack.length <= 1) return;
      stack.pop();
      screens[stack[stack.length - 1]]?.onEnter?.(makeCtx());
      renderLCD();
    },
    go(name) {
      if (!screens[name]) { console.warn('Unknown screen:', name); return; }
      stack = [name];
      screens[name].onEnter?.(makeCtx());
      try { localStorage.setItem('kestrel_last_screen', name); } catch(_) {}
      renderLCD();
    },
    defaultOptions() {
      if (stack.length > 1) ctx.pop();
      else ctx.push('main-menu');
    },
    setState(patch) { Object.assign(state, patch); renderLCD(); },
    setWeather(data) { Object.assign(state.weather, data); renderLCD(); },
    setGun(patch) {
      Object.assign(state.gun, patch);
      if (state.guns[state.gunIdx]) Object.assign(state.guns[state.gunIdx], patch);
      renderLCD();
    },
    setTarget(patch) { Object.assign(state.target, patch); renderLCD(); },
    setEnviro(patch) { Object.assign(state.enviro, patch); renderLCD(); },
    render() { renderLCD(); },
  };
  return ctx;
}

export function initMenu() {
  let lastBacklight = 0;
  return {
    register(name, screen) { screens[name] = screen; },

    boot() {
      let initial = 'main-menu';
      try { initial = localStorage.getItem('kestrel_last_screen') || 'main-menu'; } catch(_) {}
      if (!screens[initial]) initial = 'main-menu';
      stack = [initial];
      screens[initial]?.onEnter?.(makeCtx());
      renderLCD();
    },

    dispatch(btn) {
      if (!stack.length) return;
      const screen = screens[stack[stack.length - 1]];
      if (!screen) return;
      const ctx = makeCtx();

      if (btn === 'power') { stack = []; renderLCD(); return; }
      if (btn === 'backlight') {
        const now = Date.now();
        if (now - lastBacklight < 400) {
          const toMode = state.mode === 'weather' ? 'ballistics' : 'weather';
          const toScreen = toMode === 'ballistics' ? 'ballistics-mode' : 'weather';
          state.mode = toMode;
          makeCtx().go(toScreen);
        } else {
          state.backlightRed = !state.backlightRed;
          renderLCD();
        }
        lastBacklight = now;
        return;
      }
      if (btn === 'options') {
        if (screen.onOptions) screen.onOptions(ctx);
        else ctx.defaultOptions();
        return;
      }

      ({
        up: () => screen.onUp?.(ctx), down: () => screen.onDown?.(ctx),
        left: () => screen.onLeft?.(ctx), right: () => screen.onRight?.(ctx),
        select: () => screen.onSelect?.(ctx), capture: () => screen.onCapture?.(ctx),
      })[btn]?.();
      renderLCD();
    },

    // public API used by weather-sim.js and device.js
    getState() { return state; },
    setState(patch) { Object.assign(state, patch); },
    go(name) { makeCtx().go(name); },
    getWeather() { return { ...state.weather }; },
    setWeather(data) { Object.assign(state.weather, data); renderLCD(); },
    getGun() { return { ...state.gun }; },
    setGun(patch) {
      Object.assign(state.gun, patch);
      if (state.guns[state.gunIdx]) Object.assign(state.guns[state.gunIdx], patch);
      renderLCD();
    },
    getTarget() { return { ...state.target }; },
    setTarget(patch) { Object.assign(state.target, patch); renderLCD(); },
    getEnviro() { return { ...state.enviro }; },
    setEnviro(patch) { Object.assign(state.enviro, patch); renderLCD(); },
  };
}
