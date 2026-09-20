# Final Adaptive-Quadrature Validation — EXPERIMENTS FROZEN

Copyright (C) 2026 Mohammad Amir Khusru Akhtar  
Licensed under the Apache License, Version 2.0.

## Decision

This is the final synthetic validation stage before manuscript writing.
No additional architecture search is authorized by the convergence plan.
The experiment validates the mechanism; it does not by itself prove an asymptotic complexity theorem.

## Protocol

Comparator: dense bounded-grid exponential weights (EW) oracle in 1D.

Compressed predictor:
- degree-18 even log-cosh polynomial surrogate;
- additive update-closed state (n, b, S2, S4, ..., S18);
- posterior sublevel localization at height 18;
- Gauss-Legendre orders 8,16,32,64,128,256;
- stop when consecutive predictions differ by <= 0.05/(t+1)^2.

Horizons: T = 128, 256, 512, 1024, 2048.
Sequences: random, alternating, 16-round block reversals, varying x.

## Verified results

| T | sequence | max pred. error | cumulative loss tax | mean nodes | max nodes | mean interval width |
|---:|---|---:|---:|---:|---:|---:|
|128|random|5.059e-05|-2.066e-04|34.75|64|6.460|
|128|alternating|4.596e-05|-1.958e-04|24.38|64|4.150|
|128|blocks|4.596e-05|-1.474e-04|29.38|32|3.977|
|128|varying|5.059e-05|-2.083e-04|32.75|64|6.463|
|256|random|5.059e-05|-2.138e-04|35.88|64|4.787|
|256|alternating|4.596e-05|-1.634e-04|24.19|64|2.980|
|256|blocks|4.596e-05|-9.992e-05|30.38|32|2.894|
|256|varying|5.059e-05|-1.751e-04|34.06|64|4.790|
|512|random|5.059e-05|-1.646e-04|36.34|64|3.472|
|512|alternating|4.596e-05|-1.277e-04|24.78|64|2.127|
|512|blocks|4.596e-05|-5.570e-05|32.38|64|2.085|
|512|varying|5.059e-05|-1.554e-04|36.00|64|3.485|
|1024|random|5.059e-05|1.846e-06|39.64|64|2.500|
|1024|alternating|4.596e-05|-9.013e-05|31.08|64|1.515|
|1024|blocks|4.596e-05|-1.366e-05|41.50|64|1.494|
|1024|varying|5.059e-05|-8.242e-05|41.03|64|2.516|
|2048|random|5.059e-05|-3.970e-05|45.38|64|1.801|
|2048|alternating|4.596e-05|-5.165e-05|35.54|64|1.079|
|2048|blocks|4.596e-05|2.712e-05|50.72|64|1.068|
|2048|varying|5.059e-05|-1.703e-04|47.60|64|1.808|

## Aggregate audit

Worst max prediction error over all cases:
5.059e-05.

Largest absolute cumulative loss tax over all cases:
2.138e-04.

Maximum quadrature order actually selected:
64 nodes.

Random-sequence mean node count:
34.75 (T=128) -> 45.38 (T=2048).

The active interval contracts strongly as T grows, consistent with posterior localization.

## Interpretation

The earlier fixed-global-quadrature degradation is removed in these tested cases by localization plus adaptive order selection. This is strong numerical support for the 1D computational mechanism.

It is NOT evidence that:
1. the unrestricted multidimensional Hessian-volume conjecture is proved;
2. 64 nodes suffice for arbitrary T/adversarial sequences;
3. the empirical scaling establishes an asymptotic polylogarithmic theorem.

Those claims remain governed by the manuscript's proved/conditional theorem statements.

## Gate

FINAL SYNTHETIC EXPERIMENT GATE: PASSED.
EXPERIMENTAL ARCHITECTURE SEARCH: FROZEN.
NEXT STAGE: PAPER.
