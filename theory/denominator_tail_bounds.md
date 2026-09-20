# Fixed-d denominator and truncation bounds

We study a convex surrogate posterior on R^d

  q_t(theta) proportional to exp(-F_t(theta)),

with unique mode theta_hat and a Gaussian quadratic prior contribution
||theta||^2/(2s^2). Assume the data/surrogate curvature is nonnegative, so

  nabla^2 F_t(theta) >= s^{-2} I.

We recenter:
  G_t(theta)=F_t(theta)-F_t(theta_hat) >= 0.

The relevant denominator is
  Zbar_t = int exp(-G_t(theta)) dtheta
(possibly times a prior normalization constant that cancels in prediction).

## Upper Hessian bound

For exact logistic curvature,
  g''(z)<=1/4.

For a convexity-preserving curvature surrogate r_m, suppose
  0 <= r_m(z) <= W_m
on the relevant real region.

Then
  nabla^2 F_t(theta)
  <= s^{-2}I + W_m sum_{i<t} x_i x_i^T.

With ||x_i||<=R,

  lambda_max(nabla^2 F_t(theta))
  <= s^{-2}+W_m t R^2
  =: Lambda_t.

If W_m is bounded by a constant (e.g. close to logistic curvature 1/4),
Lambda_t=O(t).

## Local denominator lower bound

By Taylor's theorem and the global upper Hessian bound, for
delta=theta-theta_hat,

  G_t(theta_hat+delta)
  <= (Lambda_t/2)||delta||^2.

Integrate over the Euclidean ball
  ||delta|| <= 1/sqrt(Lambda_t).

On this ball,
  G_t <= 1/2,
so

  Zbar_t
  >= e^{-1/2} Vol(B_d) Lambda_t^{-d/2}.

Therefore if Lambda_t=O(t),

  Zbar_t >= C_d t^{-d/2}

with constants depending on d,R,s and the curvature-surrogate bound.

THIS IS ONLY POLYNOMIALLY SMALL IN t for fixed d.

Hence relative integration error O(1/t) can be achieved if absolute error is

  O(t^{-(1+d/2)})

up to constants.

The logarithm of the required inverse absolute accuracy is O(log t).

## Tail truncation from strong convexity

Strong convexity at the mode gives

  G_t(theta_hat+delta)
  >= ||delta||^2/(2s^2).

This implies the unnormalized tail is bounded by a Gaussian tail:

  int_{||delta||>r} exp(-G_t) dtheta
  <= int_{||delta||>r} exp(-||delta||^2/(2s^2)) dtheta.

To convert this to posterior tail probability divide by the denominator lower
bound C_d t^{-d/2}.

A Gaussian radial tail has form polynomial(r/s)*exp(-r^2/(2s^2)).
Thus choosing

  r_t = C s sqrt(log t)

with C depending on d and desired power makes

  Q_t(||theta-theta_hat||>r_t) <= t^{-a}

for any fixed desired a, after absorbing the denominator factor t^{d/2}.

So a MODE-CENTERED ball of radius O(s sqrt(log t)) is rigorously sufficient;
we do not need a mean-mode inequality.

This closes one earlier gap.

## Box truncation

The ball is contained in the coordinate box

  K_t = theta_hat + [-r_t,r_t]^d.

Therefore tensor-product quadrature can operate on a box with side length

  O(s sqrt(log t)).

## Conditions needed for the surrogate

The proof requires a global/relevant-region upper curvature bound W_m that
does not grow polynomially/exponentially with t.

For the curvature-first construction r_m=s_m^2, uniform approximation

  |s_m - (1/2)sech(z/2)| <= eps

on the real approximation interval gives

  s_m^2 <= (1/2+eps)^2

there, hence W_m=O(1).

But if the parameter domain is unbounded, theta^T x can leave the original
[-BR,BR] approximation interval. Therefore one must either:

A. retain a bounded parameter domain ||theta||<=B; or
B. approximate curvature on the growing mode-centered truncation range,
   whose logit range may grow with sqrt(log t), changing degree constants.

This is now the main consistency issue.

## Bounded-domain option

If Theta={||theta||<=B}, then |theta^T x|<=BR globally and W_m=O(1) is easy.
The denominator lower ball may be cut by the boundary when the mode lies near
the boundary; a cone/half-ball volume argument can still give a
constant-fraction t^{-d/2} lower bound for a convex ball domain, but must be
written carefully.

## Unbounded Gaussian option

If Gaussian prior is unbounded, the required real approximation interval may
need to cover
  |theta^T x| <= R(||theta_hat||+O(s sqrt(log t))).

A bound on ||theta_hat|| is required. From first-order optimality,

  theta_hat/s^2
   = - sum_i gradient(data loss)_i,

whose crude norm bound is O(tR), too large. Better logistic saturation may
give logarithmic growth in separable directions, but this requires proof.

## Result

CLOSED:
- denominator is only polynomially small if curvature is O(t);
- strong convexity + denominator lower bound gives a mode-centered
  O(s sqrt(log t)) high-mass ball;
- mean-mode inequality is unnecessary.

OPEN:
- unify bounded comparator domain with reference EW regret, OR
- prove logarithmic/polylogarithmic mode growth for unbounded Gaussian prior.

This is now the next bottleneck.
