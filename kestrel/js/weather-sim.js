// js/weather-sim.js
export function initWeatherSim(menu) {
  let liveInterval = null;
  function readPanel() {
    return {
      temp: parseFloat(document.getElementById('p-temp').value) || 15,
      pres: parseFloat(document.getElementById('p-pres').value) || 1013,
      hum:  parseFloat(document.getElementById('p-hum').value)  || 50,
      wind: parseFloat(document.getElementById('p-wind').value) || 0,
      wdir: parseFloat(document.getElementById('p-wdir').value) || 0,
    };
  }
  function computeDerived(d) {
    const T=d.temp, V=d.wind*3.6, RH=d.hum, P=d.pres;
    let windChill=T;
    if (T<=10 && V>4.8) windChill=13.12+0.6215*T-11.37*Math.pow(V,.16)+0.3965*T*Math.pow(V,.16);
    const a=17.625,b=243.04,alpha=Math.log(RH/100)+(a*T)/(b+T);
    const dewPoint=(b*alpha)/(a-alpha);
    const wetBulb=T*Math.atan(0.151977*Math.pow(RH+8.313659,.5))+Math.atan(T+RH)-Math.atan(RH-1.676331)+0.00391838*Math.pow(RH,1.5)*Math.atan(0.023101*RH)-4.686035;
    let heatIndex=T;
    if (T>27 && RH>40) { const Tf=T*9/5+32; const HI=-42.379+2.04901523*Tf+10.14333127*RH-0.22475541*Tf*RH-6.83783e-3*Tf*Tf-5.481717e-2*RH*RH+1.22874e-3*Tf*Tf*RH+8.5282e-4*Tf*RH*RH-1.99e-6*Tf*Tf*RH*RH; heatIndex=(HI-32)*5/9; }
    const densAlt=(1-Math.pow(P/1013.25,.190284))*44307.7;
    return { windChill, dewPoint, wetBulb, heatIndex, densAlt, station:P };
  }
  function applyData(data) { menu.setWeather({ ...data, ...computeDerived(data) }); }
  function addNoise(d) {
    return { temp:d.temp+(Math.random()-.5)*.4, pres:d.pres+(Math.random()-.5)*1, hum:Math.min(100,Math.max(0,d.hum+(Math.random()-.5)*2)), wind:Math.max(0,d.wind+(Math.random()-.5)*.6), wdir:(d.wdir+(Math.random()-.5)*5+360)%360 };
  }
  function stopLive() { if (liveInterval) { clearInterval(liveInterval); liveInterval=null; } }
  function startLive(base) { stopLive(); liveInterval=setInterval(()=>applyData(addNoise(base)),4000); }
  document.getElementById('p-apply').addEventListener('click', () => {
    const d=readPanel(); applyData(d);
    if (document.getElementById('p-live').checked) startLive(d); else stopLive();
  });
  document.getElementById('p-live').addEventListener('change', e => {
    if (e.target.checked) startLive(readPanel()); else stopLive();
  });
  return { applyDefaults() { applyData(readPanel()); } };
}
