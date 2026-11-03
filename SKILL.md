---
name: genpark-personal-agent-cutaneous-corneometry-stratum-corneum-hydration-skill
description: Evaluates stratum corneum epidermal water content and desquamation uniformity via high-frequency dielectric capacitance corneometry.
---

# Cutaneous Corneometry Stratum Corneum Hydration Skill

This skill computes epidermal stratum corneum moisture levels and spatial barrier uniformity using dielectric permittivity capacitance to diagnose xerosis and monitor barrier repair according to EEMCO guidelines.

## Core Capabilities
- Evaluates Mean Hydration in Arbitrary Units ($AU$, normal $> 40.0\text{ AU}$).
- Classifies normal hydration ($> 40\text{ AU}$), mild-to-moderate dry skin ($30 - 40\text{ AU}$), and severe barrier xerosis ($< 30\text{ AU}$).
- Computes Hydration Coefficient of Variation ($CV\%$) to detect patchy desquamation ($CV > 15\%$).
- Incorporates ambient relative humidity and temperature context.

## Zero-Mock Architecture
Standard Python standard library only with zero external dependencies.
