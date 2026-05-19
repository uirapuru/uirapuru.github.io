// js/device.js
export function initDevice(menu) {
  let lastBacklight = 0;
  document.querySelectorAll('.kbtn').forEach(btn => {
    btn.addEventListener('click', () => {
      const b = btn.dataset.btn;
      if (b === 'backlight') {
        const now = Date.now();
        if (now - lastBacklight < 400) {
          const mode = menu.getState().mode;
          if (mode === 'ballistics') { menu.setState({ mode: 'weather' }); menu.go('weather'); }
          else { menu.setState({ mode: 'ballistics' }); menu.go('ballistics-mode'); }
          lastBacklight = 0; return;
        }
        lastBacklight = now;
      }
      menu.dispatch(b);
    });
  });
  const keyMap = {
    'ArrowUp':'up','ArrowDown':'down','ArrowLeft':'left','ArrowRight':'right',
    'Enter':'select','Escape':'options',' ':'capture','l':'backlight','L':'backlight',
  };
  document.addEventListener('keydown', e => {
    const btn = keyMap[e.key];
    if (btn) { e.preventDefault(); menu.dispatch(btn); }
  });
}
