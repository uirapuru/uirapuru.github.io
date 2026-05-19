// js/intro.js
const COMPASS_CAL_CHANCE = 0.3;
const SWIPE_MIN_PX = 80;

export function initIntro(onComplete) {
  const introScreen = document.getElementById('intro-screen');
  const simScreen = document.getElementById('sim-screen');
  const hotspot = document.getElementById('power-hotspot');

  function startSim() {
    const lcd = document.getElementById('lcd-content');
    lcd.className = '';
    lcd.innerHTML = '';
    if (Math.random() < COMPASS_CAL_CHANCE) runCompassCal(onComplete);
    else onComplete();
  }

  function activate() {
    introScreen.classList.add('zooming');
    simScreen.removeAttribute('hidden');
    renderBootScreen1();
    setTimeout(() => { introScreen.style.display = 'none'; }, 480);
    setTimeout(renderBootScreen2, 1000);
    setTimeout(startSim, 2000);
  }

  hotspot.addEventListener('click', activate);
  document.addEventListener('keydown', (e) => {
    if ((e.key === 'Enter' || e.key === ' ') && introScreen.style.display !== 'none') activate();
  });
}

function renderBootScreen1() {
  const lcd = document.getElementById('lcd-content');
  lcd.className = 'boot';
  lcd.innerHTML = `
    <div style="display:flex;align-items:center;justify-content:center;gap:5px;margin-bottom:1px">
      <span style="font-size:0.8em">ᛒ</span>
      <span style="font-size:2em;font-weight:bold;letter-spacing:-1px;line-height:1.1">5700</span>
    </div>
    <div style="letter-spacing:3px;font-size:0.9em;margin-top:-3px">ELITE</div>
    <div style="height:5px"></div>
    <div style="font-size:0.8em;text-align:left">Ver&nbsp;&nbsp;1.58</div>
    <div style="font-size:0.8em;text-align:left">Battery &#x25ae;&#x2588;&#x2588;&#x2588;&#x2591;&#x25ae;</div>
  `;
}

function renderBootScreen2() {
  const lcd = document.getElementById('lcd-content');
  lcd.className = 'boot';
  lcd.innerHTML = `
    <div style="font-style:italic;font-size:0.78em;text-align:left;margin-bottom:2px">with</div>
    <div style="font-size:2.2em;font-weight:bold;font-style:italic;line-height:1.05">A<span style="font-size:0.6em;font-style:normal">&#x2014;&#x2022;</span></div>
    <div style="font-size:0.82em;letter-spacing:1px">APPLIED&nbsp;BALLISTICS</div>
    <div style="height:5px"></div>
    <div style="font-size:0.8em;text-align:left">Battery &#x25ae;&#x2588;&#x2588;&#x2588;&#x2591;&#x25ae;</div>
  `;
}

function runCompassCal(onComplete) {
  const lcd = document.getElementById('lcd-content');
  const body = document.getElementById('kestrel-photo');
  let rotations = 0;
  let startX = null;

  function renderCal() {
    lcd.textContent = 'COMPASS CAL\nRotate device\n' + rotations + '/3 complete\nswipe right →';
  }
  renderCal();

  function handleSwipeEnd(endX) {
    if (startX === null) return;
    const delta = endX - startX;
    startX = null;
    if (delta < SWIPE_MIN_PX) return;
    rotations++;
    renderCal();
    body.classList.remove('rotating');
    void body.offsetWidth;
    body.classList.add('rotating');
    body.addEventListener('animationend', () => {
      body.classList.remove('rotating');
      if (rotations >= 3) finish();
    }, { once: true });
  }

  const target = document.getElementById('kestrel');
  function onMouseDown(e) { startX = e.clientX; e.preventDefault(); }
  function onMouseUp(e) { handleSwipeEnd(e.clientX); }
  function onTouchStart(e) { startX = e.touches[0].clientX; }
  function onTouchEnd(e) { handleSwipeEnd(e.changedTouches[0].clientX); }

  target.addEventListener('mousedown', onMouseDown);
  document.addEventListener('mouseup', onMouseUp);
  target.addEventListener('touchstart', onTouchStart, { passive: true });
  document.addEventListener('touchend', onTouchEnd);

  function teardown() {
    target.removeEventListener('mousedown', onMouseDown);
    document.removeEventListener('mouseup', onMouseUp);
    target.removeEventListener('touchstart', onTouchStart);
    document.removeEventListener('touchend', onTouchEnd);
  }

  function finish() {
    teardown();
    lcd.textContent = 'COMPASS CAL\n   COMPLETE\n\n   ✓';
    setTimeout(onComplete, 1500);
  }
}
