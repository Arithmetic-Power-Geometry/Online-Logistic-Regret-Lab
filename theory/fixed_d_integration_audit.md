# Fixed-d integration audit: global quadrature versus curvature adaptation

We need to evaluate, for the polynomial-surrogate posterior on a bounded domain,

  I_f = int_Theta f(theta) pi(theta) exp(-Fhat_t(theta)) dtheta,

for f=1 and f(theta)=sigma(theta^T x_t), to enough relative/log accuracy.

## Why analyticity alone is insufficient

Even in one dimension, consider a strongly concentrated analytic density

  q_t(theta) proportional to exp(-t theta^2/2)

on a fixed interval containing zero.

Its mass lies in a window of width Theta(t^-1/2).

A global polynomial/quadrature rule on the original fixed interval must resolve
this shrinking feature. Standard approximation bounds depend on the size of
the analytic continuation, and exp(-t z^2/2) can grow like exp(+t Im(z)^2/2)
off the real axis. Choosing a fixed Bernstein ellipse therefore produces
constants exponential in t.

Optimizing the ellipse width gives degree/node counts typically at least on a
sqrt(t)-type scale for uniform approximation of the sharply concentrated
integrand.

Therefore:
  "analytic integrand on a compact fixed-d domain"
does NOT by itself imply poly(log t) quadrature complexity.

This kills the naive global-cubature completion of the fixed-d theorem.

## Curvature-adapted coordinates

Let theta_hat_t minimize Fhat_t and let
  H_t = nabla^2 Fhat_t(theta_hat_t)
when positive definite.

Set
  u = H_t^{1/2}(theta-theta_hat_t).

Then the local quadratic part becomes
  (1/2)||u||^2.

If the posterior is approximately Gaussian in these coordinates and the
standardized higher derivatives are controlled uniformly/polylogarithmically,
the relevant integration region has radius O(sqrt(d+log(1/epsilon))) in u,
not a radius shrinking with t.

This is the correct route for concentrated posteriors.

## Standardized derivative quantities

For original exact logistic potential,

  nabla^k F(theta)
   = prior contribution
     + sum_i g^{(k)}(y_i theta^T x_i)
         y_i^k x_i^{tensor k}.

In H-metric coordinates, dangerous terms involve contractions such as

  sum_i |g^{(k)}(a_i)|
        (x_i^T H^{-1} x_i)^{k/2}.

For k=2 the weighted leverage identity gives a dimension bound.

For k>=3, logistic derivatives are tied to curvature:
  |g^{(k)}(z)| <= C_k g''(z)
for fixed k, with constants depending on k.

Then

  sum_i |g^{(k)}(a_i)| l_i^{k/2}
  <= C_k sum_i w_i l_i * l_i^{(k-2)/2}
  <= C_k d (s^2 R^2)^{(k-2)/2}.

This is independent of t.

This is a strong signal: after Hessian whitening, standardized higher
derivatives may admit t-free bounds using the SAME weighted-leverage identity.

## Implication

The integration problem may be tractable in fixed d by:
1. find mode theta_hat_t;
2. form H_t;
3. whiten theta around the mode;
4. truncate to an H-ellipsoid carrying 1-epsilon posterior mass;
5. approximate/integrate the whitened analytic density on that O(sqrt(log
   1/epsilon)) region.

For epsilon polynomially small in t, whitened radius is O(sqrt(log t)).
If analytic approximation degree is polynomial in that radius and log
1/epsilon, this can be poly(log t) for fixed d.

## New proof obligations

A. mode computation from the moment-polynomial state in poly(log t) arithmetic
   operations for fixed d;
B. surrogate convexity: polynomial approximation to h need not preserve
   h''>=0 automatically;
C. H-metric tail bound for the surrogate posterior;
D. explicit standardized derivative/analytic continuation bound after
   whitening;
E. cubature node complexity poly(log t);
F. bit complexity.

## Important design correction

Use a convexity-preserving approximation to h, or approximate h'' first by a
nonnegative polynomial/rational function and integrate twice. Otherwise the
surrogate potential can acquire spurious nonconvexity, invalidating the
curvature-adapted argument.

Status:
- naive global analytic cubature: REJECTED;
- Hessian-whitened cubature: active;
- t-free standardized derivative mechanism: promising, theorem not yet closed.
