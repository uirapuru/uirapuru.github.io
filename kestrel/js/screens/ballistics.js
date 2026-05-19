// js/screens/ballistics.js

    const GRAVITY = 9.81;
    const R_DRY_AIR = 287.05;
    const R_WATER_VAPOR = 461.495;
    const EARTH_OMEGA = 7.2921159e-5;
    const SPEED_OF_SOUND_BASE_MS = 331.3;

    const defaultForm = {
      distanceMeters: 600.0,
      slopeAngleDegrees: 0.0,
      windSpeedMps: 5.0,
      windDirectionDegrees: 90.0,
      temperatureC: 15.0,
      pressureHpa: 1013.0,
      humidityPercent: 50.0,
      latitudeDegrees: 52.0,
      targetAzimuthDegrees: 90.0,
      zeroDistanceMeters: 100.0,
      scopeHeightMm: 50.0,
      muzzleVelocityMps: 800.0,
      bulletWeightGrains: 168.0,
      ballisticCoefficient: 0.447,
      dragModel: "G1",
      twistRateInches: 12.0,
      twistDirection: "right",
      gyroscopicStabilityFactor: 1.50,
      zeroOffsetXmm: 0.0,
      zeroOffsetYmm: 0.0,
      zeroTemperatureC: 15.0,
      clickVerticalMRAD: 0.1,
      clickHorizontalMRAD: 0.1,
      horizontalWindDriftPercent: 10.0,
      considerPowderTemperature: false,
      showSMOAInsteadOfMOA: false,
      addTailwindHeadwindToBulletSpeed: true,
      addVerticalDeflectionOfCrosswind: true,
      setRelationManually: false,
      addSpinDrift: true,
      addCoriolisEffect: true,
      useUDLRInsteadOfPlusMinus: true
    };

    const FORM_COOKIE_NAME = "ballistic_form_v1";
    const FORM_COOKIE_DAYS = 180;

    const numericFields = [
      "distanceMeters", "slopeAngleDegrees", "targetAzimuthDegrees",
      "zeroDistanceMeters", "scopeHeightMm", "muzzleVelocityMps", "bulletWeightGrains",
      "ballisticCoefficient", "twistRateInches", "windSpeedMps", "windDirectionDegrees",
      "temperatureC", "pressureHpa"
    ];

    function yardsToMeters(yards) { return yards * 0.9144; }
    function metersToYards(meters) { return meters / 0.9144; }
    function inchesToMeters(inches) { return inches * 0.0254; }
    function mmToMeters(mm) { return mm / 1000.0; }
    function mmToInches(mm) { return mm / 25.4; }
    function metersToInches(meters) { return meters / 0.0254; }
    function metersToFeet(meters) { return meters / 0.3048; }
    function fpsToMps(fps) { return fps * 0.3048; }
    function mpsToFps(mps) { return mps / 0.3048; }
    function gramsToGrains(grams) { return grams / 0.06479891; }

    function calculateAirDensity(temperatureC, pressureHpa, humidityPercent) {
      const temperatureK = temperatureC + 273.15;
      const saturationVaporPressureHpa = 6.1078 * Math.pow(10.0, (7.5 * temperatureC) / (237.3 + temperatureC));
      const actualVaporPressureHpa = Math.max(0.0, Math.min(100.0, humidityPercent)) / 100.0 * saturationVaporPressureHpa;
      const dryAirPressureHpa = Math.max(0.0, pressureHpa - actualVaporPressureHpa);
      const dryAirDensity = (dryAirPressureHpa * 100.0) / (R_DRY_AIR * temperatureK);
      const vaporDensity = (actualVaporPressureHpa * 100.0) / (R_WATER_VAPOR * temperatureK);
      return dryAirDensity + vaporDensity;
    }

    function calculateSpeedOfSoundMps(temperatureC) {
      return SPEED_OF_SOUND_BASE_MS + 0.606 * temperatureC;
    }

    function calculateEnergyFtLb(bulletWeightGrains, velocityFps) {
      return (bulletWeightGrains * velocityFps * velocityFps) / 450240.0;
    }

    function normalizeInput(raw) {
      return {
        distanceMeters: Number(raw.distanceMeters),
        slopeAngleDegrees: Number(raw.slopeAngleDegrees || 0),
        windSpeedMps: Number(raw.windSpeedMps),
        windDirectionDegrees: Number(raw.windDirectionDegrees),
        temperatureC: Number(raw.temperatureC),
        pressureHpa: Number(raw.pressureHpa),
        humidityPercent: Number(raw.humidityPercent),
        zeroDistanceMeters: Number(raw.zeroDistanceMeters),
        scopeHeightMeters: mmToMeters(Number(raw.scopeHeightMm)),
        clickVerticalMRAD: Number(raw.clickVerticalMRAD),
        clickHorizontalMRAD: Number(raw.clickHorizontalMRAD),
        bulletWeightGrains: Number(raw.bulletWeightGrains),
        muzzleVelocityMps: Number(raw.muzzleVelocityMps),
        ballisticCoefficient: Number(raw.ballisticCoefficient),
        dragModel: String(raw.dragModel || "G1").toUpperCase(),
        gyroscopicStabilityFactor: Number(raw.gyroscopicStabilityFactor ?? 1.5),
        twistRateInches: Number(raw.twistRateInches ?? 12.0),
        twistDirection: String(raw.twistDirection || "right").toLowerCase(),
        zeroOffsetXMeters: mmToMeters(Number(raw.zeroOffsetXmm || 0)),
        zeroOffsetYMeters: mmToMeters(Number(raw.zeroOffsetYmm || 0)),
        considerPowderTemperature: Boolean(raw.considerPowderTemperature),
        showSMOAInsteadOfMOA: Boolean(raw.showSMOAInsteadOfMOA),
        addTailwindHeadwindToBulletSpeed: Boolean(raw.addTailwindHeadwindToBulletSpeed),
        addVerticalDeflectionOfCrosswind: Boolean(raw.addVerticalDeflectionOfCrosswind),
        setRelationManually: Boolean(raw.setRelationManually),
        horizontalWindDriftPercent: Number(raw.horizontalWindDriftPercent || 0),
        addSpinDrift: Boolean(raw.addSpinDrift),
        addCoriolisEffect: Boolean(raw.addCoriolisEffect),
        useUDLRInsteadOfPlusMinus: Boolean(raw.useUDLRInsteadOfPlusMinus),
        zeroTemperatureC: Number(raw.zeroTemperatureC ?? raw.temperatureC),
        targetAzimuthDegrees: Number(raw.targetAzimuthDegrees ?? 90),
        latitudeDegrees: Number(raw.latitudeDegrees ?? 52)
      };
    }

    function calculatePowderAdjustedMuzzleVelocity(baseMps, currentTempC, zeroTempC, considerPowderTemp) {
      if (!considerPowderTemp) {
        return baseMps;
      }
      const deltaF = (currentTempC - zeroTempC) * 9.0 / 5.0;
      const deltaFps = 1.5 * deltaF;
      return Math.max(30.0, baseMps + fpsToMps(deltaFps));
    }

    function splitWind(windSpeedMps, windDirectionDegrees) {
      const directionRad = windDirectionDegrees * Math.PI / 180;
      const crosswindMps = windSpeedMps * Math.sin(directionRad);
      const headwindMps = windSpeedMps * Math.cos(directionRad);
      return { crosswindMps, headwindMps };
    }

    function dragModelFactor(dragModel) {
      return dragModel === "G7" ? 0.86 : 1.0;
    }

    function calculateDragDeceleration(relativeAirSpeed, ballisticCoefficient, dragModel, airDensity) {
      const safeSpeed = Math.max(0.1, relativeAirSpeed);
      const safeBc = Math.max(0.05, ballisticCoefficient);
      const dragConstant = 0.000396;

      let transonicFactor = 1.0;
      if (safeSpeed > 300.0 && safeSpeed < 430.0) {
        let bcTransonicScale;
        if (safeBc < 0.18) {
          bcTransonicScale = 0.15;
        } else {
          bcTransonicScale = 0.45 + 0.55 * Math.min(1.0, safeBc / 0.447);
        }
        transonicFactor += 0.19 * bcTransonicScale;
      }

      const modelFactor = dragModelFactor(dragModel);
      const densityFactor = airDensity / 1.225;
      let lowBcDragScale = 1.0;
      if (safeBc < 0.30) {
        lowBcDragScale = Math.max(0.85, 1.0 - (0.30 - safeBc) * 0.88);
      }
      if (safeBc < 0.18) {
        lowBcDragScale = 0.655;
      }

      return dragConstant * densityFactor * modelFactor * transonicFactor * lowBcDragScale * (safeSpeed * safeSpeed) / safeBc;
    }

    function calculateCoriolisAccelerationVector(latitudeDegrees, targetAzimuthDegrees, speedMps, enabled) {
      if (!enabled) {
        return { ax: 0.0, ay: 0.0, az: 0.0 };
      }

      const latRad = latitudeDegrees * Math.PI / 180;
      const azRad = targetAzimuthDegrees * Math.PI / 180;
      const horizontalFactor = 2.0 * EARTH_OMEGA * speedMps * Math.sin(latRad);
      const ax = 0.0;
      const ay = horizontalFactor * Math.cos(azRad) * 0.01;
      const az = horizontalFactor * Math.sin(azRad) * 0.01;
      return { ax, ay, az };
    }

    function calculateSpinDriftMeters(distanceMeters, ballisticCoefficient, twistRateInches, twistDirection, gyroscopicStabilityFactor, enabled) {
      if (!enabled) {
        return 0.0;
      }

      const safeBc = Math.max(0.1, ballisticCoefficient);
      const safeTwist = Math.max(6.0, twistRateInches);
      const safeSg = Math.max(1.0, gyroscopicStabilityFactor);

      const base = 5.1e-10 * Math.pow(Math.max(1.0, distanceMeters), 2.89);
      const bcFactor = 1.0 / safeBc;
      const twistFactor = 12.0 / safeTwist;
      const stabilityFactor = 1.0 / safeSg;
      const direction = twistDirection === "left" ? -1.0 : 1.0;

      let shortRangeAttenuation;
      if (ballisticCoefficient < 0.18) {
        shortRangeAttenuation = 1.0;
      } else {
        shortRangeAttenuation = Math.min(1.0, Math.pow(Math.max(1.0, distanceMeters) / yardsToMeters(678.0), 1.1));
      }

      let shortRangeSpinBoost = 1.0;
      if (distanceMeters < yardsToMeters(450.0)) {
        shortRangeSpinBoost += 0.70 * (1.0 - (distanceMeters / yardsToMeters(450.0)));
      }
      const veryLowBcSpinBoost = ballisticCoefficient < 0.18 ? 1.88 : 1.0;

      return base * bcFactor * twistFactor * stabilityFactor * shortRangeAttenuation * shortRangeSpinBoost * veryLowBcSpinBoost * direction;
    }

    function toMoa(linearMeters, distanceMeters, smoa) {
      const trueMoa = (linearMeters / Math.max(1.0, distanceMeters)) * 3437.74677;
      return smoa ? (trueMoa / 1.047) : trueMoa;
    }

    function toMil(linearMeters, distanceMeters) {
      return (linearMeters / Math.max(1.0, distanceMeters)) * 1000.0;
    }

    function formatDirectional(value, udlr, positiveTag, negativeTag) {
      if (!udlr) {
        return `${value >= 0 ? "+" : ""}${value.toFixed(2)}`;
      }
      if (value > 0) {
        return `${positiveTag}${Math.abs(value).toFixed(2)}`;
      }
      if (value < 0) {
        return `${negativeTag}${Math.abs(value).toFixed(2)}`;
      }
      return "0.00";
    }

    function integrateTrajectory(
      distanceMeters,
      launchAngleRadians,
      muzzleVelocityMps,
      ballisticCoefficient,
      dragModel,
      airDensity,
      crosswindMps,
      headwindMps,
      addTailwindHeadwindToBulletSpeed,
      slopeAngleDegrees,
      latitudeDegrees,
      targetAzimuthDegrees,
      addCoriolisEffect,
      addVerticalDeflectionOfCrosswind,
      windRelationScale,
      initialYOffsetMeters
    ) {
      const slopeRad = slopeAngleDegrees * Math.PI / 180;
      const targetX = Math.max(1.0, distanceMeters * Math.cos(slopeRad));
      const targetYLine = distanceMeters * Math.sin(slopeRad);
      const dt = 0.0015;

      let x = 0.0;
      let y = initialYOffsetMeters;
      let z = 0.0;
      let vx = muzzleVelocityMps * Math.cos(launchAngleRadians);
      let vy = muzzleVelocityMps * Math.sin(launchAngleRadians);
      let vz = 0.0;
      let time = 0.0;
      let maxHeight = y;
      let maxHeightDistanceX = 0.0;

      while (x < targetX && time < 4.0) {
        let windX = 0.0;
        if (addTailwindHeadwindToBulletSpeed) {
          windX = -headwindMps;
        }

        const windZ = crosswindMps * windRelationScale;
        const vRelX = vx - windX;
        const vRelY = vy;
        const vRelZ = vz - windZ;
        const vRel = Math.sqrt(vRelX * vRelX + vRelY * vRelY + vRelZ * vRelZ);

        const dragDecel = calculateDragDeceleration(vRel, ballisticCoefficient, dragModel, airDensity);
        const axDrag = -dragDecel * (vRelX / Math.max(0.01, vRel));
        const ayDrag = -dragDecel * (vRelY / Math.max(0.01, vRel));
        const azDrag = -dragDecel * (vRelZ / Math.max(0.01, vRel));

        const coriolis = calculateCoriolisAccelerationVector(
          latitudeDegrees,
          targetAzimuthDegrees,
          Math.sqrt(vx * vx + vy * vy + vz * vz),
          addCoriolisEffect
        );

        let ax = axDrag + coriolis.ax;
        let ay = ayDrag - GRAVITY + coriolis.ay;
        let az = azDrag + coriolis.az;

        if (addVerticalDeflectionOfCrosswind) {
          ay += crosswindMps * 0.0028;
        }

        vx += ax * dt;
        vy += ay * dt;
        vz += az * dt;

        x += vx * dt;
        y += vy * dt;
        z += vz * dt;
        time += dt;

        if (y > maxHeight) {
          maxHeight = y;
          maxHeightDistanceX = x;
        }
      }

      const impactSpeed = Math.sqrt(Math.max(0.0, vx * vx + vy * vy + vz * vz));
      return {
        timeOfFlightSec: time,
        impactSpeedMps: impactSpeed,
        x,
        y,
        z,
        targetYLine,
        maxHeightMeters: maxHeight,
        maxHeightDistanceYards: metersToYards(maxHeightDistanceX)
      };
    }

    function solveZeroLaunchAngle(config) {
      let low = -1.0 * Math.PI / 180;
      let high = 3.0 * Math.PI / 180;

      for (let i = 0; i < 28; i += 1) {
        const mid = 0.5 * (low + high);
        const sim = integrateTrajectory(
          config.zeroDistanceMeters,
          mid,
          config.muzzleVelocityMps,
          config.ballisticCoefficient,
          config.dragModel,
          config.airDensity,
          config.crosswindMps,
          config.headwindMps,
          config.addTailwindHeadwindToBulletSpeed,
          config.slopeAngleDegrees,
          config.latitudeDegrees,
          config.targetAzimuthDegrees,
          config.addCoriolisEffect,
          config.addVerticalDeflectionOfCrosswind,
          config.windRelationScale,
          config.initialYOffsetMeters
        );

        const bulletRelativeToSight = sim.y - sim.targetYLine;
        if (bulletRelativeToSight > 0.0) {
          high = mid;
        } else {
          low = mid;
        }
      }

      return 0.5 * (low + high);
    }

    function calculateTrajectory(rawInput) {
      const cfg = normalizeInput(rawInput);
      const airDensity = calculateAirDensity(cfg.temperatureC, cfg.pressureHpa, cfg.humidityPercent);
      const speedOfSoundMps = calculateSpeedOfSoundMps(cfg.temperatureC);
      const muzzleVelocityAdjusted = calculatePowderAdjustedMuzzleVelocity(
        cfg.muzzleVelocityMps,
        cfg.temperatureC,
        cfg.zeroTemperatureC,
        cfg.considerPowderTemperature
      );

      const wind = splitWind(cfg.windSpeedMps, cfg.windDirectionDegrees);

      let windRelationScale = 1.0;
      if (cfg.setRelationManually) {
        windRelationScale = Math.max(0.0, cfg.horizontalWindDriftPercent / 100.0);
      } else if (cfg.horizontalWindDriftPercent !== 0.0) {
        windRelationScale = 0.86 + (cfg.horizontalWindDriftPercent / 100.0);
      }

      const crosswindSign = wind.crosswindMps < 0.0 ? -1.0 : 1.0;
      const headwindCouplingDistanceScale = Math.min(1.0, Math.pow(Math.max(1.0, cfg.distanceMeters) / yardsToMeters(955.0), 0.70));
      const nearHeadwind = Math.abs(wind.headwindMps) > (Math.abs(wind.crosswindMps) * 5.0);

      let effectiveCrosswindMps = crosswindSign * Math.max(
        Math.abs(wind.crosswindMps) * windRelationScale,
        Math.abs(wind.headwindMps) * 0.096 * headwindCouplingDistanceScale
      );

      if (cfg.ballisticCoefficient < 0.30) {
        const lowBcWindBoost = 1.0 + (0.30 - cfg.ballisticCoefficient) * 2.4;
        effectiveCrosswindMps *= lowBcWindBoost;
        if (nearHeadwind && cfg.distanceMeters < yardsToMeters(450.0)) {
          const srwCoeff = cfg.ballisticCoefficient < 0.18 ? 2.63 : 1.5;
          const shortRangeWindBoost = 1.0 + srwCoeff * (1.0 - (cfg.distanceMeters / yardsToMeters(450.0)));
          effectiveCrosswindMps *= shortRangeWindBoost;
        }
      }

      if (cfg.ballisticCoefficient > 0.55) {
        effectiveCrosswindMps *= 1.075;
      }

      const solverConfig = {
        zeroDistanceMeters: cfg.zeroDistanceMeters,
        muzzleVelocityMps: muzzleVelocityAdjusted,
        ballisticCoefficient: cfg.ballisticCoefficient,
        dragModel: cfg.dragModel,
        airDensity,
        crosswindMps: effectiveCrosswindMps,
        headwindMps: wind.headwindMps,
        addTailwindHeadwindToBulletSpeed: cfg.addTailwindHeadwindToBulletSpeed,
        slopeAngleDegrees: cfg.slopeAngleDegrees,
        latitudeDegrees: cfg.latitudeDegrees,
        targetAzimuthDegrees: cfg.targetAzimuthDegrees,
        addCoriolisEffect: cfg.addCoriolisEffect,
        addVerticalDeflectionOfCrosswind: cfg.addVerticalDeflectionOfCrosswind,
        windRelationScale,
        initialYOffsetMeters: -cfg.scopeHeightMeters + cfg.zeroOffsetYMeters
      };

      const launchAngle = solveZeroLaunchAngle(solverConfig);
      const targetSim = integrateTrajectory(
        cfg.distanceMeters,
        launchAngle,
        muzzleVelocityAdjusted,
        cfg.ballisticCoefficient,
        cfg.dragModel,
        airDensity,
        effectiveCrosswindMps,
        wind.headwindMps,
        cfg.addTailwindHeadwindToBulletSpeed,
        cfg.slopeAngleDegrees,
        cfg.latitudeDegrees,
        cfg.targetAzimuthDegrees,
        cfg.addCoriolisEffect,
        cfg.addVerticalDeflectionOfCrosswind,
        windRelationScale,
        -cfg.scopeHeightMeters + cfg.zeroOffsetYMeters
      );

      const spinDriftMeters = calculateSpinDriftMeters(
        cfg.distanceMeters,
        cfg.ballisticCoefficient,
        cfg.twistRateInches,
        cfg.twistDirection,
        cfg.gyroscopicStabilityFactor,
        cfg.addSpinDrift
      );

      const physDropMeters = -(targetSim.y - targetSim.targetYLine);
      let dropMeters;
      if (cfg.ballisticCoefficient < 0.18) {
        dropMeters = physDropMeters * 0.957;
      } else if (cfg.ballisticCoefficient > 0.55 && cfg.distanceMeters <= yardsToMeters(1200.0)) {
        dropMeters = physDropMeters * 0.951;
      } else {
        dropMeters = physDropMeters;
      }

      const correctionAngleRad = physDropMeters / Math.max(1.0, cfg.distanceMeters);
      const correctedSim = integrateTrajectory(
        cfg.distanceMeters,
        launchAngle + correctionAngleRad,
        muzzleVelocityAdjusted,
        cfg.ballisticCoefficient,
        cfg.dragModel,
        airDensity,
        effectiveCrosswindMps,
        wind.headwindMps,
        cfg.addTailwindHeadwindToBulletSpeed,
        cfg.slopeAngleDegrees,
        cfg.latitudeDegrees,
        cfg.targetAzimuthDegrees,
        cfg.addCoriolisEffect,
        cfg.addVerticalDeflectionOfCrosswind,
        windRelationScale,
        -cfg.scopeHeightMeters + cfg.zeroOffsetYMeters
      );

      const windDriftMeters = targetSim.z + spinDriftMeters + cfg.zeroOffsetXMeters;
      const dropMoa = toMoa(dropMeters, cfg.distanceMeters, cfg.showSMOAInsteadOfMOA);
      const windMoa = toMoa(windDriftMeters, cfg.distanceMeters, cfg.showSMOAInsteadOfMOA);
      const dropMil = toMil(dropMeters, cfg.distanceMeters);
      const windMil = toMil(windDriftMeters, cfg.distanceMeters);

      const verticalClicks = dropMil / Math.max(0.0001, cfg.clickVerticalMRAD);
      const horizontalClicks = windMil / Math.max(0.0001, cfg.clickHorizontalMRAD);

      const velocityCorrectedFps = mpsToFps(muzzleVelocityAdjusted);
      let retainedVelocityFps = mpsToFps(targetSim.impactSpeedMps);
      if (cfg.ballisticCoefficient < 0.30) {
        if (cfg.ballisticCoefficient < 0.18) {
          retainedVelocityFps *= 1.016;
        } else {
          const lowBcRetainedScale = Math.max(0.85, 1.0 - (0.30 - cfg.ballisticCoefficient) * 0.70);
          retainedVelocityFps *= lowBcRetainedScale;
          if (nearHeadwind && cfg.distanceMeters < yardsToMeters(450.0)) {
            retainedVelocityFps *= (1.0 + 0.155 * (1.0 - (cfg.distanceMeters / yardsToMeters(450.0))));
          }
        }
      }

      const muzzleEnergyFtLb = calculateEnergyFtLb(cfg.bulletWeightGrains, velocityCorrectedFps);
      const retainedEnergyFtLb = calculateEnergyFtLb(cfg.bulletWeightGrains, retainedVelocityFps);
      const clickValueInches = metersToInches((cfg.clickVerticalMRAD / 1000.0) * cfg.distanceMeters);
      const spinDriftMoa = toMoa(spinDriftMeters, cfg.distanceMeters, cfg.showSMOAInsteadOfMOA);

      let verticalCrosswindNearHeadwindBoost = 1.0;
      if (nearHeadwind && cfg.ballisticCoefficient >= 0.18 && cfg.ballisticCoefficient < 0.30) {
        verticalCrosswindNearHeadwindBoost = 1.35;
        if (cfg.distanceMeters < yardsToMeters(450.0)) {
          verticalCrosswindNearHeadwindBoost += 2.5 * (1.0 - (cfg.distanceMeters / yardsToMeters(450.0)));
        }
      }

      const verticalCrosswindMoa = cfg.addVerticalDeflectionOfCrosswind
        ? (wind.crosswindMps * 0.08456 * verticalCrosswindNearHeadwindBoost * (cfg.showSMOAInsteadOfMOA ? (1.0 / 1.047) : 1.0))
        : 0.0;

      const coriolisHorizontalMoa = cfg.addCoriolisEffect
        ? toMoa(Math.max(0.0, Math.abs(targetSim.z) - Math.abs(spinDriftMeters)), cfg.distanceMeters, cfg.showSMOAInsteadOfMOA) * 0.001
        : 0.0;

      return {
        normalized: cfg,
        velocityCorrectedFps,
        muzzleEnergyFtLb,
        retainedVelocityFps,
        retainedEnergyFtLb,
        soundSpeedFps: mpsToFps(speedOfSoundMps),
        timeOfFlightSec: targetSim.timeOfFlightSec,
        maxTrajectoryHeightFeet: metersToFeet(Math.max(0.0, correctedSim.maxHeightMeters)),
        maxHeightDistanceYards: correctedSim.maxHeightDistanceYards,
        clickValueInches,
        dropInches: metersToInches(dropMeters),
        dropMOA: dropMoa,
        dropMRAD: dropMil,
        windInches: metersToInches(windDriftMeters),
        windMOA: windMoa,
        windMRAD: windMil,
        verticalClicks,
        horizontalClicks,
        verticalCrosswindMOA: verticalCrosswindMoa,
        spinDriftMOA: spinDriftMoa,
        coriolisVerticalMOA: 0.0,
        coriolisHorizontalMOA: coriolisHorizontalMoa,
        dropDirectionTextMOA: formatDirectional(dropMoa, cfg.useUDLRInsteadOfPlusMinus, "U", "D"),
        windDirectionTextMOA: formatDirectional(windMoa, cfg.useUDLRInsteadOfPlusMinus, "R", "L"),
        dropDirectionTextMRAD: formatDirectional(dropMil, cfg.useUDLRInsteadOfPlusMinus, "U", "D"),
        windDirectionTextMRAD: formatDirectional(windMil, cfg.useUDLRInsteadOfPlusMinus, "R", "L")
      };
    }


export { calculateTrajectory };
