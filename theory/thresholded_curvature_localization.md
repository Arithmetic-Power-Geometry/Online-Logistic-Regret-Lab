# Thresholded curvature localization

We need to control curvature changes without the global factor exp(r s R).

Let
  l_i=x_i^T H^{-1}x_i,
  v=theta-theta_bar,
  ||v||_H <= r.
Then
  |u_i|=|x_i^T v| <= r sqrt(l_i).

Fix threshold q>0 and split:
  G(q)={i: r sqrt(l_i)<=q},
  B(q)={i: r sqrt(l_i)>q}.

## Good set

On G(q), the exact curvature ratio obeys
  omega_i/w_i <= exp(q).
Hence any quadratic local remainder charged as w_i u_i^2 satisfies
  sum_G omega_i u_i^2
  <= exp(q) sum_G w_i u_i^2
  <= exp(q) v^T(H-s^{-2}I)v
  <= exp(q) r^2.

Choosing q=O(log poly(d,B,T)) keeps this polynomial.

## Bad set: weighted leverage mass

For i in B(q),
  l_i > q^2/r^2.
Thus
  w_i <= (r^2/q^2) w_i l_i
after summing in the sense
  sum_B w_i
  <= (r^2/q^2) sum_B w_i l_i
  <= d r^2/q^2.

This only controls total BASE curvature weight of bad examples. It does not
control their path-averaged curvature after a large move toward the logistic
decision boundary; omega_i/w_i can be exponentially large.

So thresholding alone does NOT close the deterministic local-potential bound.

## A better observation: bounded total change of h'

Since h'(z)=1/2 tanh(z/2) lies in [-1/2,1/2],
  |h'(a+u)-h'(a)| <= 1.

And
  h(a+u)-h(a)-h'(a)u
    = integral_0^u [h'(a+s)-h'(a)] ds.

Therefore universally
  0 <= remainder <= |u|.

We also have the curvature-local bound
  remainder <= (1/2) exp(|u|) w_i u^2.

Hence
  remainder <= min{|u|, (1/2)e^{|u|}w_i u^2}.

For bad/saturated examples, use the linear cap rather than exponential
curvature comparison.

## Summing the linear cap is still problematic

sum_i |u_i|
can be O(t), and unweighted leverage does not have a dimension-only sum bound.

Thus a deterministic pointwise potential approximation over the whole local
ellipsoid still appears too strong.

## Consequence

The next route should exploit EXPECTATION under the posterior rather than
uniform-in-theta local potential error. Under a strongly log-concave posterior,
directional fluctuations have sub-Gaussian tails:
  E[(x_i^T v)^2] is controlled by x_i^T H^{-1}x_i
locally / under an appropriate covariance domination.

Then expected curvature-weighted remainders can sum through
  sum_i w_i l_i <= d,
while rare large displacements are handled probabilistically rather than by a
uniform exponential factor.

This requires replacing the previous sup-norm stability bridge with an
expectation/KL-type posterior perturbation bridge.

Status:
- thresholded deterministic sup bound: insufficient;
- exact reason: saturated factors can move toward the boundary and amplify
  curvature exponentially;
- next mathematical target: expected-potential/KL stability using weighted
  leverage.
