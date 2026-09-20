# Boundary-safe denominator via an inward reference point

Let Theta=B_2(0,B), and let F be a convex smooth posterior/surrogate potential
on Theta with
  ||grad F(theta)|| <= G_t
and
  nabla^2 F(theta) <= Lambda_t I
on Theta.

For logistic history plus a bounded smooth prior term, a crude bound is
  G_t=O(tR + prior_gradient_bound),
  Lambda_t=O(tR^2 + prior_curvature_bound).

Let theta_hat minimize F over Theta; it may lie on the boundary.

## Inward point

For 0<alpha<1 define
  theta_0=(1-alpha) theta_hat.

Its distance to the boundary is at least alpha B.

Potential gap by Lipschitzness:
  F(theta_0)-F(theta_hat)
  <= G_t ||theta_0-theta_hat||
  <= G_t alpha B.

Choose
  alpha = min(1/2, 1/(B G_t))
when G_t>0.

Then
  F(theta_0)-F(theta_hat) <= 1.

The available interior radius around theta_0 is at least
  alpha B >= min(B/2,1/G_t).

This can be O(1/t) under the crude G_t=O(t), which is smaller than the desired
curvature radius O(1/sqrt(t)).

Integrating a ball of radius O(1/t) yields denominator lower bound O(t^-d),
still POLYNOMIALLY small.

This is enough for polylogarithmic accuracy requirements in fixed d.

## Local ball

Take
  r_t = c * min(B, 1/G_t, 1/sqrt(Lambda_t))
with a sufficiently small universal c.

Then B(theta_0,r_t) subset Theta.

For theta=theta_0+delta in this ball, Taylor gives

  F(theta)-F(theta_0)
  <= ||grad F(theta_0)|| r_t + (Lambda_t/2) r_t^2
  <= G_t r_t + 1/2
  <= O(1)

by r_t<=c/G_t and r_t<=c/sqrt(Lambda_t).

Together with F(theta_0)-F(theta_hat)<=1,

  F(theta)-F(theta_hat) <= C

for a universal constant C.

Hence the recentered denominator

  Zbar=int_Theta exp(-(F-F(theta_hat))) dtheta

satisfies

  Zbar >= e^{-C} Vol(B_d) r_t^d.

With G_t=O(t) and Lambda_t=O(t),

  r_t=Omega(1/t)

under fixed B,R/prior constants, giving

  Zbar >= C_d t^{-d}.

This is weaker than the interior t^{-d/2} bound but still polynomial.

## Tail/truncation implication

To make posterior tail probability <=t^{-a}, an unnormalized Gaussian/strong
convexity tail divided by a t^{-d} denominator requires only an extra d log t
in the exponent.

Thus radius
  O(s sqrt(log t))
around the constrained mode remains sufficient, up to constants, if the
strong-convexity lower bound is available along feasible directions.

## Consequence for quadrature accuracy

If Zbar>=C t^{-d}, relative denominator/numerator accuracy O(1/t) follows from
absolute integration accuracy roughly
  t^{-(d+1)}
(up to constants).

Again
  log(1/epsilon_abs)=O(log t).

Therefore the boundary does NOT destroy the polylogarithmic approximation
degree in fixed d.

## What is now closed

Under explicit derivative bounds G_t=O(t), Lambda_t=O(t):
- boundary-safe denominator lower bound is polynomial t^{-d};
- high-mass truncation radius remains O(s sqrt(log t));
- required absolute quadrature precision has logarithm O(log t).

Remaining main gap:
prove a deterministic integration/cubature rule for the actual
convexity-preserving polynomial surrogate on the O(sqrt(log t)) box with
poly_d(log t) nodes/operations, including control of complex growth or use a
real-variable quadrature theorem that avoids unstable complex continuation.

Paper gate:
reference regret CLOSED;
boundary denominator CLOSED at polynomial scale;
cubature theorem is now the principal remaining mathematical gap.
