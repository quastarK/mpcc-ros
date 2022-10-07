# Model Predictive Contouring Control

This repo contains an inprogress implementation of model predictive contouring control (MPCC) based on the ACADOS (kinematic model only) and forces PRO solver (both models).  A registered licence for forces PRO is required to run this part of the repo.

## Problem formulation
[The mathematical formulation can be found here.](media/problem_formulation/problem_formulation.pdf) The resulting controller is shown below.
![Resulting Controller](media/slider.gif)
![heatmap](media/heatmap_rel.png)

## Debug

The system equations are described using CasADi in models.py (in the function dynamic_model()). The solver is set up in acados_settings.py (in the function acados_settings_dyn())
