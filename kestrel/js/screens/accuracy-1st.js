// js/screens/accuracy-1st.js
import { lcd5 } from '../lcd.js';

const TOOLS = [
  {
    label: 'QkWind',
    render(state) {
      const ws  = (state.weather.wind || 0).toFixed(1);
      const wd  = state.target.wd || 0;
      const cw  = ((state.weather.wind||0) * Math.abs(Math.sin(wd*Math.PI/180))).toFixed(2);
      return lcd5(['QkWind', `WS: ${ws} m/s`, `WD: ${wd} deg`, `CW: ${cw} m/s`, '<->tool']);
    },
  },
  {
    label: 'WndDot',
    render(state) {
      const cw   = (state.weather.wind||0) * Math.abs(Math.sin((state.target.wd||0)*Math.PI/180));
      const dots = (cw * 0.27).toFixed(1);
      return lcd5(['WndDot (Tremor3)', `CW: ${cw.toFixed(2)} m/s`, `Dots: ${dots}`, 'Tremor3 reticle', '<->tool']);
    },
  },
  {
    label: 'SpdDrp',
    render(state) {
      const diff = (state.target.tr||600) - (state.gun.zr||100);
      const elv  = (diff * 0.003).toFixed(2);
      return lcd5(['SpdDrp', `ZR: ${state.gun.zr}m`, `Tgt: ${state.target.tr}m`, `Elv ~${elv} mil`, '<->tool']);
    },
  },
  {
    label: 'AJ=.1mil',
    render(state) {
      const cw = (state.weather.wind||0) * Math.abs(Math.sin((state.target.wd||0)*Math.PI/180));
      const aj = (cw * 0.1).toFixed(3);
      return lcd5(['AJ=.1mil', `CW: ${cw.toFixed(2)} m/s`, `AJ: ${aj} mil`, '', '<->tool']);
    },
  },
  {
    label: '12" Drill',
    render() {
      return lcd5(['12 Inch Drill', 'Aim at center', 'Fire 3 shots', 'Measure group', '<->tool']);
    },
  },
];

let toolIdx = 0;

export function registerAccuracy1st(menu) {
  menu.register('accuracy-1st', {
    onEnter() { toolIdx = 0; },
    onLeft()  { toolIdx = (toolIdx - 1 + TOOLS.length) % TOOLS.length; },
    onRight() { toolIdx = (toolIdx + 1) % TOOLS.length; },
    onUp()    { toolIdx = (toolIdx - 1 + TOOLS.length) % TOOLS.length; },
    onDown()  { toolIdx = (toolIdx + 1) % TOOLS.length; },
    render(state) { return TOOLS[toolIdx].render(state); },
  });
}
