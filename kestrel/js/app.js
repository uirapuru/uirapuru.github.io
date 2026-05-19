// js/app.js
import { initIntro }           from './intro.js';
import { initDevice }          from './device.js';
import { initMenu }            from './menu.js';
import { initWeatherSim }      from './weather-sim.js';
import { registerWeather }     from './screens/weather.js';
import { registerBallistics }  from './screens/ballistics-mode.js';
import { registerEasy }        from './screens/easy.js';
import { registerMainMenu }    from './screens/main-menu.js';
import { registerAccuracy1st } from './screens/accuracy-1st.js';
import { registerRangeCard }   from './screens/range-card.js';
import { registerTargetCard }  from './screens/target-card.js';
import { registerSnakeScreen } from './snake.js';

function onSimStart() {
  const menu = initMenu();
  registerWeather(menu);
  registerBallistics(menu);
  registerEasy(menu);
  registerMainMenu(menu);
  registerAccuracy1st(menu);
  registerRangeCard(menu);
  registerTargetCard(menu);
  registerSnakeScreen(menu);
  const sim = initWeatherSim(menu);
  initDevice(menu);
  sim.applyDefaults();
  menu.boot();
}

initIntro(onSimStart);
