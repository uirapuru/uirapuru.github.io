// js/screens/range-card.js
import { lcd5 } from '../lcd.js';
import { calculateTrajectory } from './ballistics.js';

const INCREMENTS = [25, 50, 100, 200, 300];
let incIdx = 2;
let rowOffset = 0;
let table = [];

function buildTable(state) {
  const g = state.gun, w = state.weather, t = state.target, e = state.enviro;
  const inc = INCREMENTS[incIdx];
  const rows = [];
  for (let d = inc; d <= 2000; d += inc) {
    try {
      const r = calculateTrajectory({
        distanceMeters:d, slopeAngleDegrees:0,
        windSpeedMps:t.ws1||w.wind||0, windDirectionDegrees:t.wd||90,
        temperatureC:w.temp||15, pressureHpa:w.pres||1013, humidityPercent:w.hum||50,
        latitudeDegrees:e.lat||52, targetAzimuthDegrees:0,
        zeroDistanceMeters:g.zr, scopeHeightMm:g.bh, muzzleVelocityMps:g.mv,
        bulletWeightGrains:g.bw, ballisticCoefficient:g.bc, dragModel:g.dm,
        twistRateInches:g.rt, twistDirection:g.rtd, gyroscopicStabilityFactor:1.5,
        zeroOffsetXmm:0, zeroOffsetYmm:g.zh||0, zeroTemperatureC:15,
        clickVerticalMRAD:g.eclk, clickHorizontalMRAD:g.wclk,
        horizontalWindDriftPercent:10, considerPowderTemperature:false,
        showSMOAInsteadOfMOA:false, addTailwindHeadwindToBulletSpeed:true,
        addVerticalDeflectionOfCrosswind:true, setRelationManually:false,
        addSpinDrift:true, addCoriolisEffect:true, useUDLRInsteadOfPlusMinus:true,
      });
      rows.push({ d, elv:r.dropDirectionTextMRAD, wnd:r.windDirectionTextMRAD });
    } catch(ex) { rows.push({ d, elv:'---', wnd:'---' }); }
  }
  return rows;
}

export function registerRangeCard(menu) {
  menu.register('range-card', {
    onEnter(ctx) { incIdx = 2; rowOffset = 0; table = buildTable(ctx.state); },
    onUp()    { rowOffset = Math.max(0, rowOffset - 1); },
    onDown()  { rowOffset = Math.min(Math.max(0, table.length - 3), rowOffset + 1); },
    onLeft(ctx)  { incIdx = Math.max(0, incIdx - 1); table = buildTable(ctx.state); rowOffset = 0; },
    onRight(ctx) { incIdx = Math.min(INCREMENTS.length - 1, incIdx + 1); table = buildTable(ctx.state); rowOffset = 0; },
    render() {
      const inc = INCREMENTS[incIdx];
      const hdr = `RngCard +${inc}m`;
      const col = 'Rng  Elv    Wnd ';
      const rows = table.slice(rowOffset, rowOffset + 3).map(r =>
        String(r.d).padStart(4)+'  '+r.elv.padEnd(5)+'  '+r.wnd
      );
      while (rows.length < 3) rows.push('');
      return lcd5([hdr, col, ...rows]);
    },
  });
}
