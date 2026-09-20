# Hessian-whitened integration theorem attempt

## Goal

For fixed d,B,R (or fixed d with controlled prior scale), evaluate

  E_Q[f(theta)]

for f=1 / logistic predictive numerator under a strongly log-concave
surrogate posterior, with log-evidence/prediction error O(1/t), using
poly(log t) arithmetic work.

Let theta_hat be the unique mode and
  H = nabla^2 F(theta_hat).

Whiten:
  theta = theta_hat + H^{-1/2}u.

Define the centered whitened potential
  Phi(u)
   = F(theta_hat+H^{-1/2}u)-F(theta_hat).

Then
  Phi(0)=0,
  grad Phi(0)=0,
  nabla^2 Phi(0)=I.

## Logistic generalized self-concordance

For scalar logistic loss g,
  |g'''(z)| <= g''(z).

Along any direction v, for the exact logistic potential,

  |D^3 F(theta)[v,v,v]|
  <= sum_i w_i(theta) |x_i^T v|^3.

Let H(theta)=prior curvature + sum_i w_i(theta)x_ix_i^T.

Using
  |x_i^T v|
   <= sqrt(x_i^T H(theta)^{-1}x_i) ||v||_{H(theta)}
   <= s R ||v||_{H(theta)}

from H(theta)>=s^{-2}I,

  |D^3 F(theta)[v,v,v]|
  <= sR ||v||_{H(theta)}
       sum_i w_i(theta)(x_i^T v)^2
  <= sR ||v||_{H(theta)}^3.

Thus the potential is generalized self-concordant with parameter at most sR
(up to convention constants), independent of t.

This is the crucial T-free local geometry statement.

## Hessian variation

Generalized self-concordance implies along a displacement delta,

  exp(-R||delta||_2) H(theta)
  <= H(theta+delta)
  <= exp(R||delta||_2) H(theta)

for the data Hessian/logistic curvature, with prior handled separately.

In whitened coordinates, Euclidean displacement obeys
  ||delta||_2
   <= ||H^{-1/2}|| ||u||
   <= s ||u||.

Hence over ||u||<=r,

  Hessian distortion is bounded by exp(sR r).

This is T-independent, but for r=Theta(sqrt(log t)) it becomes
  exp(O(sR sqrt(log t)))
  = t^{O(sR/sqrt(log t))}
which is subpolynomial in t but NOT obviously poly(log t).

Therefore generalized self-concordance alone does not immediately yield
polylog(t) quadrature constants on the entire high-probability ball.

## Strong-log-concave tail

Since F is s^{-2}-strongly convex in theta, after whitening at a mode whose H
may be much larger than s^{-2}I, a universal Gaussian tail in the H metric
does not follow solely from global strong convexity.

The local H metric can overstate curvature away from the mode when logistic
weights decay.

This is a second gap: a radius O(sqrt(log t)) in whitened coordinates is not
automatically a certified 1-1/poly(t) mass region from only local H.

## Safe Euclidean tail

Global strong convexity gives concentration on Euclidean scale
  O(s sqrt(d+log t)).
After mapping to u=H^{1/2}delta, this radius can grow with sqrt(lambda_max(H)),
potentially O(sqrt(t log t)).

That destroys polylog cubature if used naively.

## Conclusion of theorem attempt

The desired uniform theorem

  "mode-Hessian whitening + strong log-concavity => poly(log t) cubature"

does NOT follow from the currently established assumptions.

The obstacle is curvature decay away from the mode in separable/saturated
logistic directions.

This is not yet an impossibility theorem for integration; it kills the simple
proof route.

## Better structural split

Directions can be divided by Hessian eigenvalues:
- high-curvature directions: whitened concentration is strong, integration
  region remains small;
- low-curvature directions: H eigenvalues are near prior scale, so Euclidean
  region is already O(s sqrt(log t)) and does not shrink with t.

A mixed anisotropic coordinate box may avoid the bad product of local Hessian
and global tail.

Candidate scale per eigen-direction lambda_j:
  a_j = min(
    sqrt(log(t))/sqrt(lambda_j),
    s sqrt(log(t))
  )
in theta coordinates,
which after natural rescaling may keep each coordinate interval
O(sqrt(log t)).

Need prove joint mass and analytic approximation on this anisotropic box.

## Paper gate

Do NOT write the paper yet.

WRITE immediately if:
A. anisotropic integration is proved with poly_d(log T) nodes/time and the
   reference bounded-domain EW regret is closed; OR
B. a rigorous lower bound/counterexample shows fixed-d integration or
   variable-d compact representation necessarily needs super-polylog(T)
   resources for the relevant approximation class.

Current status: neither gate has fired.
