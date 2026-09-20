# Final convergence decision: metric-volume proof attempt

## Target

We attempted to prove, uniformly over arbitrary bounded logistic ridge
sequences in fixed dimension,

  V_H(S_A)
  = int_{F-Fmin<=A} sqrt(det nabla^2F(theta)) dtheta
  <= C_{d,R,alpha} poly(A).

The sharper empirical candidate was O(A^{d/2}).

## What can be proved from current ingredients

1. Strong convexity gives Euclidean sublevel radius O(sqrt(A)).
2. Logistic ridge curvature is log-Lipschitz in Euclidean displacement.
3. Along every ray from the mode, endpoint directional curvature is bounded
   by potential height.
4. Fixed finite ridge dictionaries and separable objectives admit polylog
   covers.
5. The aggregate SPD Hessian matrix space has only poly_d(log t)
   multiplicative resolution over eigenvalues in [alpha,O(t)].
6. d=2 adversarial numerical search strongly supports V_H=Theta(A)-scale
   behavior for A=Theta(log t), with V_H/log t approximately flat over the
   tested horizon range.

## Why the general proof does NOT close

The ray theorem controls the Hessian in the radial direction from the mode.
It does not control all transverse eigenvalues at the same point by the same
potential-height quantity.

A gradient-map argument gives
  int_S det H = Vol(nabla F(S)),
but our metric volume contains sqrt(det H). Cauchy-Schwarz then requires a
uniform bound on the gradient-image volume. The available smoothness bound
reintroduces O(t) curvature and does not yield a poly(A) estimate.

Discretizing the SPD Hessian cone gives only polylog many Hessian SHAPES, but
does not bound how many spatially separated local-Hessian cells of the same
shape can be packed inside the sublevel set. Bounding this packing by
Euclidean volume loses the exact curvature/sublevel cancellation and can
reintroduce polynomial t.

Classical standard self-concordant Dikin-ellipsoid theorems cannot simply be
imported: regularized logistic loss is naturally generalized/quasi
self-concordant rather than a standard self-concordant barrier with the exact
uniform metric-volume statement needed here.

Therefore the unrestricted-direction metric-volume conjecture remains
UNPROVED.

## No-go on claiming the Google target solved

Because this covering theorem is required for the proposed deterministic
fixed-d integration algorithm, we do NOT currently have a complete rigorous
algorithm with certified polylog(T) prediction time for arbitrary adversarial
directions.

The numerical evidence is not a theorem.

Therefore the full Google/open-problem target must NOT be claimed solved.

## Convergence rule applied

Research exploration stops here rather than opening another branch.

The paper should be written NOW as a rigorous partial-theory paper.

The manuscript should separate:

### Proved results
- exact score-calibration identities and their finite-dictionary extension;
- counterexamples to Gaussian/covariance/skew-only compression;
- exact log-cosh decomposition and update-closed tensor representation;
- convexity-preserving curvature-first polynomial surrogate;
- approximation-to-adversarial-log-loss bridge;
- bounded-domain/cube Bayesian-mixture regret O(d log(BRT));
- exact complex logistic curvature lemma;
- 1D curvature-height theorem;
- 1D adaptive deterministic polylog quadrature skeleton, after formalizing
  constants/perturbation assumptions;
- multidimensional ray localization;
- structured-family polylog Hessian covers;
- empirical d=2 metric-volume evidence.

### Explicit open theorem
For unrestricted adversarial directions, prove or disprove a fixed-d
polylogarithmic Hessian-metric covering/volume bound for O(log T) posterior
sublevel sets.

### Claim discipline
Do not say the 2012 Google problem is solved.
Do not call the metric-volume conjecture a theorem.
Do not turn numerical scaling into a proof.
Present the work as a reduction: the practical fixed-d near-optimal route is
reduced to a precise geometric/computational bottleneck, with several major
candidate architectures rigorously eliminated.

## Paper gate

PARTIAL-THEORY PAPER GATE: FIRED NOW.

No further exploratory experiment is required before drafting.
