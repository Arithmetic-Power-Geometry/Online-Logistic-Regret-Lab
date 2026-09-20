# One-dimensional localization theorem skeleton

Consider a one-dimensional convex posterior potential on [-B,B]:

  F(theta)=prior(theta)+sum_i g(y_i x_i theta),

with |x_i|<=R, logistic g(z)=log(1+e^{-z}), or a convexity-preserving
surrogate uniformly close to it.

Let theta_hat be a minimizer.

## Exact convex localization facts

Because F is convex, on each side of theta_hat the derivative is monotone.

For any Delta>0 define the right secant slope
  s_+(Delta)=[F(theta_hat+Delta)-F(theta_hat)]/Delta >=0.

Convexity implies for u>=Delta,
  F(theta_hat+u)-F(theta_hat)
  >= s_+(Delta) u
up to the sharper affine continuation
  >= F(theta_hat+Delta)-F(theta_hat)
     + F'_+(theta_hat+Delta)(u-Delta).

Thus once the potential has risen by A at distance Delta, the farther tail
decays at least exponentially at rate A/Delta (or faster).

Similarly on the left.

This converts a certified finite core into exponentially small tails without
requiring curvature to remain large.

## Core radius from strong convexity

If a quadratic prior gives alpha-strong convexity,

  F(theta_hat+u)-F(theta_hat) >= alpha u^2/2

for an interior stationary mode.

For constrained boundary modes use the inward near-minimizer construction and
pay O(1).

Thus at
  Delta = sqrt(2 A/alpha),
the potential has risen by at least A.

Taking A=C log t gives
  Delta=O(sqrt(log t)).

Everything outside this core has total unnormalized mass bounded by an
exponential tail with factor e^{-C log t}=t^{-C}, times only polynomial/core
scale factors.

Therefore localization to O(sqrt(log t)) is rigorous from convexity + strong
convexity; no Hessian persistence is needed.

## Integration inside the core: remaining issue

The core width is O(sqrt(log t)). The integrand may have a very narrow peak of
width t^-1/2.

A single polynomial approximation on the whole core may still need sqrt(t)
degree to resolve that peak.

So localization alone does not solve quadrature.

## Peak-width adaptation in 1D

Let
  H0=F''(theta_hat),  alpha<=H0<=O(t).

Define local coordinate
  u=sqrt(H0)(theta-theta_hat).

The central peak has O(1) width in u.

If curvature later decays, the transformed interval may be long, but those
regions correspond to potential growth and can be treated as tails.

Need establish a core threshold q_t=O(log t) in u such that either:
A. |u|<=q_t and standardized derivatives are controlled, permitting
   O(polylog t) quadrature; or
B. F-Fmin >= C log t, making contribution negligible.

## Logistic-specific curvature-drop dichotomy

For each logistic term,
  |d log g''(z)/dz|<=1.

Along theta displacement delta,
  g'' at a factor can change by at most exp(R|delta|).

For the sum Hessian, this yields a coarse
  F''(theta_hat+delta)-alpha
  >= exp(-R|delta|)[F''(theta_hat)-alpha].

Integrating twice gives a deterministic lower envelope for potential growth:

Let K=H0-alpha >=0. For delta>=0,

  F''(theta_hat+delta)
  >= alpha + K e^{-R delta}.

Integrate:
  F'(theta_hat+delta)-F'(theta_hat)
  >= alpha delta + (K/R)(1-e^{-R delta}).

For interior mode F'(theta_hat)=0, integrate again:

  F(theta_hat+delta)-F(theta_hat)
  >= alpha delta^2/2
     + (K/R) delta
     - (K/R^2)(1-e^{-R delta}).

This is an explicit logistic core-tail lower envelope.

## Consequence

When K is large (~t), after delta exceeds O(1/R), the lower envelope contains
a LINEAR term approximately
  (K/R) delta - K/R^2,
which becomes huge.

So a high-curvature mode cannot be followed by a long flat, high-mass region:
if curvature decays, accumulated slope forces rapid potential growth.

This is exactly the localization property needed.

In whitened coordinate u=sqrt(H0) delta, the transition delta~1/R occurs at
u~sqrt(H0)/R, which can be large, but the potential by then is already
Omega(K/R^2), enormous when K is large.

The relevant mass region should therefore be captured for potential height
O(log t) at a delta much smaller than 1/R when K>>log t:
  delta=O(sqrt(log t/K)),
so
  u=O(sqrt(log t)).

Thus the posterior mass-bearing core has whitened radius O(sqrt(log t))
uniformly in t.

## Status

This establishes a strong 1D localization envelope for the EXACT logistic
potential (plus quadratic prior).

It strongly supports:
  relevant whitened radius = O(sqrt(log t)).

Still needed:
- transfer envelope to convex polynomial surrogate, or integrate exact
  potential using compressed representation approximation;
- explicit polynomial/quadrature error on whitened O(sqrt(log t)) interval;
- boundary-mode variant.

This is progress but not yet the final cubature theorem.
