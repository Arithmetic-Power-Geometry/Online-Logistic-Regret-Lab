# Online Logistic Regret Lab

Research code and reproducibility materials for efficient online logistic regression.

## Problem setting

For rounds t=1,...,T:
- x_t in R^d with ||x_t||_2 <= R,
- the learner outputs a probability p_t in (0,1),
- y_t in {-1,+1} is revealed,
- logistic loss is ell(z_t,y_t)=log(1+exp(-y_t z_t)).

The comparator class is Theta_B={theta in R^d : ||theta||_2 <= B}.

The project studies whether near-optimal exponential-weights (EW) prediction can be represented and evaluated from an update-closed state with lightweight horizon dependence.

## Main research direction

The current architecture uses the exact decomposition

    log(1+exp(-yz)) = log 2 - yz/2 + log cosh(z/2),

which separates labels from nonlinear curvature. Approximating the even log-cosh term by an even polynomial yields an additive state

    (n, b_t, S_2,t, S_4,t, ..., S_2m,t),

with exact online updates for the polynomial surrogate.

The repository contains:
- exact score-calibration identities for special direction structures;
- counterexamples to Gaussian, low-moment, and projection-based compression routes;
- update-closed log-cosh compression;
- convexity-preserving curvature approximation;
- approximation-to-log-loss stability bounds;
- one-dimensional localization and adaptive quadrature;
- structured multidimensional Hessian-cover results;
- a precise open Hessian-metric volume/packing question for unrestricted directions.

## Experimental validation

The one-dimensional adaptive localized predictor is compared with a dense-grid EW reference over horizons T in {128,256,512,1024,2048} and random, alternating, block-reversal, and varying-feature sequences.

Across the recorded validation matrix:
- worst maximum prediction error: 5.059e-05;
- largest absolute cumulative loss tax: 2.138e-04;
- maximum selected quadrature order: 64 nodes.

These experiments validate the computational mechanism in one dimension. They do not prove that 64 nodes suffice for arbitrary horizons or that the unrestricted multidimensional covering condition holds.

## Repository structure

- software/ — executable fixed-dimensional and adaptive-localization implementations.
- tests/ — unit and property tests.
- experiments/ — falsification and stress experiments.
- theory/ — theorem derivations, audits, and open-problem reductions.
- benchmarks/ — synthetic OGD/ONS benchmark harness.
- results/ — recorded validation summaries.
- .github/workflows/ — reproducibility workflows.

## Reproduction

```bash
pip install -r requirements.txt
pip install pytest
pytest -q
python software/run_fixed_d_validation.py
python software/run_adaptive_validation.py
python benchmarks/compare_existing.py
```

## Scope

The repository does not claim that the general online-logistic-regression open problem is solved. The unrestricted multidimensional Hessian-metric volume/packing step remains open.

## License

Copyright (C) 2026 Mohammad Amir Khusru Akhtar.

Licensed under the Apache License, Version 2.0. See LICENSE and NOTICE.
