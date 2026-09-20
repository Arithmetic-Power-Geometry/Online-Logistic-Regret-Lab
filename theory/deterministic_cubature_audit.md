# Deterministic cubature audit: real-variable derivative route

We need deterministic integration of

  f_t(theta)=a(theta) exp(-(Fhat_t(theta)-Fhat_t(theta_hat)))

over a fixed-d box K_t of side width W_t=O(sqrt(log t)), where a(theta) is
either 1 or the current logistic likelihood.

Required absolute error is t^{-C_d} for a fixed C_d (e.g. d+1 plus safety).

The surrogate potential is a polynomial of degree
  q_t=O(log t)
for fixed B,R.

## Naive fixed-order derivative bounds are insufficient

For one coordinate x, derivatives of exp(-F(x)) obey Bell-polynomial/Faa di
Bruno expressions involving F',...,F^{(k)}.

Even if F^{(k)}=O(t C^k k!) on the real domain, the kth derivative of
exp(-F) can contain powers such as (F')^k exp(-F), yielding crude
  O(t^k)
bounds.

A classical n-point Gauss error involving the 2n-th derivative would then
contain t^{2n}; choosing n=O(log t) does not automatically help and crude
derivative sup bounds are useless.

Thus a direct global derivative-supremum proof is rejected.

## Localization rescales the problem

Near the mode, high gradients are suppressed by exp(-(F-Fmin)).
For the model Gaussian exp(-t x^2/2), sup_x |d^k/dx^k exp(-t x^2/2)|
scales like t^{k/2}, while the feature width is t^-1/2.

After rescaling u=sqrt(t)x, the derivative growth disappears.

Therefore quadrature must be CURVATURE/scale adapted, not applied in raw
theta coordinates with derivative sup bounds.

## Piecewise adaptive deterministic integration

In fixed dimension, partition the truncation box into cells whose side lengths
are proportional to a local inverse-curvature scale.

For a cell centered at c, let
  M(c) >= lambda_max(nabla^2 Fhat) locally.
Choose side
  h(c)=gamma/sqrt(M(c)).

On the rescaled cell u=(theta-c)/h(c), the quadratic variation is O(1).

If higher standardized derivatives are controlled, a constant/order-log
quadrature rule per cell can attain exponentially decreasing local error.

The number of cells is governed by the metric volume
  int_K sqrt(det(I+nabla^2 Fhat(theta))) dtheta
or related curvature volume.

## Potential fatal issue

Worst-case curvature can be O(t) over an O(1) region. Then in d dimensions,
cell width t^-1/2 requires O(t^{d/2}) cells: NOT polylog.

But logistic curvature O(t) over an O(1) theta region would imply the posterior
mass is concentrated in a t^-1/2 region; integrating the entire region at that
resolution is wasteful.

Need posterior-mass-adaptive refinement, not uniform curvature refinement.

## Mode-centered single-scale anisotropic integration

At the mode, use H0=nabla^2 Fhat(theta_hat). In high-curvature directions,
scale by H0^{-1/2}; in prior-dominated directions scale by s.

The earlier concern was curvature decay away from the mode. However for
integration accuracy, far regions with substantial metric distortion may
already have exponentially small posterior mass.

The missing theorem is a LOCALIZATION statement coupling:
  Hessian decay + accumulated potential increase.

For scalar logistic h, exact identity:
  h''(z)=1/(4 cosh^2(z/2))
and
  |d/dz log h''(z)|<=1.

If curvature drops by factor e^{-a}, the logit must move distance at least a.
The integrated slope/curvature along that move contributes potential increase.
This suggests curvature cannot collapse for free.

## One-dimensional saturated tail calculation

For large positive z,
  h(z) ~ z/2 - log2,
  h''(z) ~ e^{-z}.

So after leaving the quadratic core, the potential grows LINEARLY while
curvature becomes small.

This is favorable for integration: tails are exponential even when Hessian
whitening no longer reflects curvature.

Hence a hybrid core-tail quadrature may use:
- Gaussian/Hessian scaling in the core;
- exponential-tail coordinate mapping outside.

## Current conclusion

A naive standard cubature theorem is not enough.
A polylog fixed-d integration theorem remains plausible, but proving it from
scratch now requires a nontrivial localization/core-tail theorem.

This is a larger mathematical component than previously estimated.

## Paper-gate consequence

We should NOT claim the full fixed-d efficient algorithm yet.

There are now two legitimate paper options:
1. continue until the new localization/cubature theorem is proved;
2. write a paper centered on the already rigorous representation/regret
   framework, clearly presenting efficient prediction integration as an open
   theorem/conjecture -- but that would NOT solve the target computational
   problem.

Per the user's gate, choose option 1 until theorem or obstruction.

Next precise task:
prove the required localization theorem first in d=1. If even d=1 fails to
admit polylog deterministic integration under the surrogate class, kill the
positive route. If d=1 closes, tensorize/extend to fixed d.
