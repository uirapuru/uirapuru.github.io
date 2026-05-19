// js/lcd.js
export const LCD_COLS = 16;
export const LCD_ROWS = 5;

export function lcd5(lines) {
  const out = [];
  for (let i = 0; i < LCD_ROWS; i++) {
    const l = lines[i] ?? '';
    if (typeof l === 'string') out.push(l.slice(0, LCD_COLS));
    else out.push({ ...l, text: (l.text ?? '').slice(0, LCD_COLS) });
  }
  return out;
}

export function center(str, len = LCD_COLS) {
  const s = String(str).slice(0, len);
  const pad = Math.floor((len - s.length) / 2);
  return ' '.repeat(Math.max(0, pad)) + s;
}

export function rjust(label, val, cols = LCD_COLS) {
  const l = String(label);
  const v = String(val);
  const gap = cols - l.length - v.length;
  return l + ' '.repeat(Math.max(1, gap)) + v;
}
