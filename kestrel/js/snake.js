// js/snake.js — Nokia 3210-style Snake
const SCORE_H = 13;                        // px reserved for score bar
const TARGET_COLS = 14;                    // target column count (determines cell size)
const BASE_MS  = { 1: 500, 2: 300, 3: 150 };
const ACCEL_MS = 10;
const MIN_MS   = 80;

const C_BG = '#c8d8a8';
const C_FG = '#1a2e0a';

export function registerSnakeScreen(menu) {
  let canvas, ctx2d, cols, rows, cell;
  let snake, dir, nextDir, food, score, timer, phase, level, tickMs;

  function initCanvas() {
    const content = document.getElementById('lcd-content');
    const lcdEl   = document.getElementById('lcd');

    content.innerHTML = '';
    content.style.position = 'relative';
    content.style.padding  = '0';

    canvas        = document.createElement('canvas');
    canvas.width  = lcdEl.offsetWidth;
    canvas.height = lcdEl.offsetHeight - 30;
    canvas.style.display = 'block';
    content.appendChild(canvas);

    ctx2d = canvas.getContext('2d');

    cell  = Math.max(5, Math.floor((canvas.width - 2) / TARGET_COLS));
    cols  = Math.max(6,  Math.floor((canvas.width  - 2) / cell));
    rows  = Math.max(4,  Math.floor((canvas.height - SCORE_H - 2) / cell));
  }

  function dropCanvas() {
    clearInterval(timer);
    timer = null;
    const content = document.getElementById('lcd-content');
    if (content) {
      content.innerHTML     = '';
      content.style.position = '';
      content.style.padding  = '';
    }
    canvas = ctx2d = null;
  }

  function rndFood() {
    let p;
    do {
      p = { x: Math.floor(Math.random() * cols),
            y: Math.floor(Math.random() * rows) };
    } while (snake.some(s => s.x === p.x && s.y === p.y));
    return p;
  }

  function startGame() {
    clearInterval(timer);
    const mx = Math.floor(cols / 2), my = Math.floor(rows / 2);
    snake   = [{ x: mx, y: my }, { x: mx - 1, y: my }, { x: mx - 2, y: my }];
    dir     = { x: 1, y: 0 };
    nextDir = { x: 1, y: 0 };
    food    = rndFood();
    score   = 0;
    tickMs  = BASE_MS[level];
    phase   = 'playing';
    timer   = setInterval(tick, tickMs);
    draw();
  }

  function tick() {
    dir = { ...nextDir };
    const h = { x: snake[0].x + dir.x, y: snake[0].y + dir.y };

    if (h.x < 0 || h.x >= cols || h.y < 0 || h.y >= rows ||
        snake.some(s => s.x === h.x && s.y === h.y)) {
      clearInterval(timer);
      phase = 'game-over';
      draw();
      return;
    }

    snake.unshift(h);
    if (h.x === food.x && h.y === food.y) {
      score++;
      food   = rndFood();
      tickMs = Math.max(MIN_MS, tickMs - ACCEL_MS);
      clearInterval(timer);
      timer  = setInterval(tick, tickMs);
    } else {
      snake.pop();
    }
    draw();
  }

  // top-left pixel of grid cell (c, r)
  function cx(c) { return 1 + c * cell; }
  function cy(r) { return SCORE_H + 1 + r * cell; }

  function drawText(text, x, y) {
    ctx2d.fillText(text, x, y);
  }

  function draw() {
    if (!ctx2d) return;
    const W = canvas.width, H = canvas.height;

    ctx2d.clearRect(0, 0, W, H);

    // Score bar (inverted)
    ctx2d.fillStyle = C_FG;
    ctx2d.fillRect(0, 0, W, SCORE_H);
    ctx2d.fillStyle = C_BG;
    ctx2d.font = 'bold 10px monospace';
    ctx2d.textAlign    = 'center';
    ctx2d.textBaseline = 'middle';

    if (phase === 'level-select') {
      drawText('SNAKE', W / 2, SCORE_H / 2);
      ctx2d.fillStyle = C_FG;
      ctx2d.font = '10px monospace';
      const my = SCORE_H + (H - SCORE_H) / 2;
      drawText(`< Level ${level} >`, W / 2, my - 10);
      drawText('SELECT = start',     W / 2, my + 5);
      return;
    }

    if (phase === 'game-over') {
      drawText('GAME OVER', W / 2, SCORE_H / 2);
      ctx2d.fillStyle = C_FG;
      ctx2d.font = '10px monospace';
      const my = SCORE_H + (H - SCORE_H) / 2;
      drawText(`Score: ${score}`, W / 2, my - 12);
      drawText('SELECT=retry',   W / 2, my + 2);
      drawText('OPT=exit',       W / 2, my + 16);
      return;
    }

    // playing — score bar
    drawText(`Score: ${score}`, W / 2, SCORE_H / 2);

    // game area border
    ctx2d.strokeStyle = C_FG;
    ctx2d.lineWidth   = 1;
    ctx2d.strokeRect(0.5, SCORE_H + 0.5, W - 1, H - SCORE_H - 1);

    // food: small filled square
    ctx2d.fillStyle = C_FG;
    ctx2d.fillRect(cx(food.x) + 1, cy(food.y) + 1, cell - 2, cell - 2);

    // snake: head = full cell, body = inset by 1px
    snake.forEach((s, i) => {
      if (i === 0) {
        ctx2d.fillRect(cx(s.x),     cy(s.y),     cell,     cell);
      } else {
        ctx2d.fillRect(cx(s.x) + 1, cy(s.y) + 1, cell - 2, cell - 2);
      }
    });
  }

  menu.register('snake', {
    onEnter() {
      initCanvas();
      phase = 'level-select';
      level = 1;
      draw();
    },

    render() { return null; },

    onUp()    { if (phase === 'playing' && dir.y === 0) nextDir = { x: 0, y: -1 }; },
    onDown()  { if (phase === 'playing' && dir.y === 0) nextDir = { x: 0, y:  1 }; },

    onLeft()  {
      if (phase === 'playing'      && dir.x === 0) { nextDir = { x: -1, y: 0 }; return; }
      if (phase === 'level-select') { level = (level > 1) ? level - 1 : 3; draw(); }
    },
    onRight() {
      if (phase === 'playing'      && dir.x === 0) { nextDir = { x: 1, y: 0 }; return; }
      if (phase === 'level-select') { level = (level < 3) ? level + 1 : 1; draw(); }
    },

    onSelect() {
      if (phase === 'level-select') startGame();
      if (phase === 'game-over')    { phase = 'level-select'; draw(); }
    },

    onOptions(ctx) {
      dropCanvas();
      ctx.pop();
    },
  });
}
