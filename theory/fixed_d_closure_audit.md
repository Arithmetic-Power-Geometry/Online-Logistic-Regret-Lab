# Fixed-d closure chain: multivariate analytic cells, surrogate transfer, mode computation, regret

This note attempts to close the remaining technical chain without opening new
architectures.

## Lemma 1: safe multivariate complex neighborhood

For real xi and complex theta=xi+i eta, every logistic ridge has imaginary
logit
  |x_i^T eta| <= ||x_i||_2 ||eta||_2 <= R ||eta||_2.

Hence if
  R ||eta||_2 <= q < pi,
all ridge factors remain away from their nearest poles.

The exact scalar identity gives termwise curvature control by sec^2(q/2).

Thus any local complex box with coordinate half-widths a_j satisfying
  sqrt(sum_j a_j^2) <= q/R
is a safe polydisc/box neighborhood.

For an axis-aligned real cell with half-widths h_j, choose complex ellipse
heights a_j=c h_j and enforce
  c ||h||_2 <= q/R.

If the adaptive real cells are chosen with Euclidean diameter <=C/R in the
outer region and relative diameter near the mode, a sufficiently small
constant c gives a t-independent polyellipse aspect ratio.

Near the mode, use H0-whitened cells. If a whitened complex displacement z
satisfies ||Im z||_2<=c, then
  eta=H0^{-1/2} Im z
and since H0>=alpha I,
  ||eta||<=c/sqrt(alpha).
Choose c<q sqrt(alpha)/R.
Thus a constant whitened polydisc is safe.

Conclusion: raywise analyticity CAN be upgraded to a safe multivariate
polyellipse by controlling Euclidean imaginary norm. This costs only
dimension-dependent constants when converting boxes/ellipsoids.

## Lemma 2: exact-potential complex magnitude on local cells

Along the complex segment xi+i s eta,

  Re F(xi+i eta)
  >= F(xi)
     -(C_q/2) eta^T H(xi) eta,

where C_q=sec^2(q/2), using termwise curvature comparison.

Adaptive cells are selected so their complex displacement obeys either:
- near mode: eta^T H0 eta <=c^2;
- local relative cell at displacement delta: ||eta||<=c min(||delta||,1/R).

The multidimensional ray curvature-height theorem applied in direction
v=delta/||delta|| controls the RADIAL quadratic form v^T H v.
But eta may have components transverse to delta.

THIS IS A REAL GAP:
ray curvature-height does not by itself bound
  eta^T H(xi) eta
for transverse eta.

A cell with isotropic complex thickness proportional to ||delta|| may see
large transverse curvature not paid for by radial potential height.

Therefore the previous adaptive isotropic-cell argument is not fully proved.

## Correct local metric

The safe complex cell should instead be shaped by the LOCAL Hessian H(xi):

  eta^T H(xi) eta <= c^2(1+DeltaF(xi)).

Then the complex magnitude exponent is
  -DeltaF + O(c^2(1+DeltaF)),
which is controlled for small c.

So local cells must be Hessian ellipsoids, not merely Euclidean relative balls.

## New covering question

Can the sublevel set DeltaF<=A=O(log t) be covered by
poly_d(log t) local Hessian ellipsoids

  E_x={delta: delta^T H(x) delta <= c^2(1+DeltaF(x))}

?

This is related to Dikin-type/Riemannian covering geometry.

The earlier Euclidean shell count does NOT prove this because transverse
curvature can be large.

Thus the paper gate cannot honestly fire yet.

## Lemma 3: surrogate C2 transfer (conditional on exact geometry)

Let h'' be exact log-cosh curvature and r_m polynomial curvature surrogate.
If uniformly on bounded logit range

  |r_m(z)-h''(z)| <= eps_c,

then for ||x_i||<=R,

  ||Hhat(theta)-H(theta)||op
  <= sum_i eps_c ||x_i||^2
  <= t eps_c R^2.

Choosing
  eps_c <= c/(t^2 R^2)
gives
  ||Hhat-H||op <= c/t.

Since H>=alpha I, for t sufficiently large this is a relative perturbation

  (1-O(1/(alpha t))) H
   <= Hhat
   <= (1+O(1/(alpha t))) H.

Similarly, if per-factor function approximation error eps_f=O(t^-2),

  sup_theta |Fhat-F - constant| <= O(1/t).

Therefore potential sublevel sets, Hessian metrics, strong convexity, and
local analytic cell shapes transfer with 1+o(1) constants.

This closure item is sound.

## Lemma 4: mode computation

Fhat is a convex polynomial potential on the box [-B,B]^d with
  Hhat>=alpha/2 I
for sufficiently accurate curvature approximation.

Its gradient is Lipschitz with
  L_t=O(t R^2 + alpha)
on the bounded box because r_m is uniformly O(1).

Condition number
  kappa_t=L_t/(alpha/2)=O(t)
under fixed parameters.

Plain gradient descent would need O(kappa log(1/eps))=O(t log t), NOT polylog.

Accelerated gradient gives O(sqrt(kappa) log(1/eps))=O(sqrt(t) log t),
still not polylog.

Newton/self-concordant methods may achieve logarithmic iteration counts if
linear systems and global convergence are controlled, but the polynomial
surrogate is not automatically standard self-concordant.

For the EXACT logistic objective, logistic loss is generalized
self-concordant; damped Newton complexity may depend on R/alpha and initial
gap rather than t polynomially. For the surrogate this requires proof.

Thus MODE COMPUTATION is a second genuine gap; it was previously understated.

## Regret accounting (conditional)

If at each round approximate predictive evidence has log error <=c/t relative
to exact bounded-domain Bayesian mixture, then

  L_alg - L_mix <= c sum_{t=1}^T 1/t
                <= c(1+log T).

Exact cube-prior mixture regret against any ||theta*||_2<=B is

  L_mix-L(theta*)
  <= 1+d log(2B sqrt(d) R T)

in the nontrivial regime.

Therefore conditional final regret is

  R_T(theta*)
  <= 1+d log(2B sqrt(d)RT)+c(1+log T)
  = O(d log(BRT)+log T).

This part is closed once prediction computation is certified.

## Honest status after closure audit

CLOSED:
- reference mixture regret;
- update-closed fixed-d polynomial state;
- convex curvature-first surrogate;
- O(1/t) posterior/potential approximation target;
- exact/surrogate C2 transfer;
- 1D adaptive quadrature;
- multidimensional ray localization;
- multivariate safe-pole neighborhood;
- final regret accounting conditional on prediction accuracy.

OPEN, and genuinely nontrivial:
G1. Hessian-ellipsoid covering number of O(log t) posterior sublevel set:
    prove poly_d(log t), or find counterexample.
G2. Compute surrogate mode / required local centers in poly_d(log t) time:
    likely requires a generalized-self-concordant Newton theorem or an
    integration scheme avoiding explicit high-accuracy mode computation.

Therefore PAPER GATE DOES NOT FIRE YET.

Next branch is forced and narrow:
attack G1 first. If Hessian metric volume/covering can grow polynomially in t
even in fixed d for logistic ridge sums, that may kill the current algorithm.
If it is polylog, then attack G2.
