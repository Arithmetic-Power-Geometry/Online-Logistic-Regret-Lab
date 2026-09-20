# Hessian-metric cover audit for fixed-d logistic posteriors

We study whether the sublevel set

  S_A={theta: F(theta)-F(theta_hat)<=A}, A=O(log t),

can be covered by poly_d(log t) local Hessian ellipsoids.

The local metric is H(theta)=nabla^2F(theta).

## Global Hessian comparison

For any two real points theta,theta',

each logistic curvature weight satisfies
  w_i(theta') <= exp(|x_i^T(theta'-theta)|) w_i(theta)
              <= exp(R||theta'-theta||) w_i(theta).

Therefore in PSD order,

  H(theta')-alpha I
  <= exp(R||theta'-theta||)[H(theta)-alpha I].

Hence

  H(theta') <= exp(R||delta||) H(theta)

because alpha I <= exp(...) alpha I.

Similarly
  H(theta') >= exp(-R||delta||) H(theta)
up to the prior floor; safely
  H(theta') >= exp(-R||delta||) H(theta).

Thus the Hessian metric is generalized-self-concordant/log-Lipschitz in
Euclidean distance with parameter R.

On S_A, strong convexity gives
  ||theta-theta_hat|| <= sqrt(2A/alpha)=O(sqrt(log t)).

A crude global distortion bound is therefore
  exp(O(R sqrt(log t))),
subpolynomial but not polylog. Too crude.

## Metric volume route

A standard covering heuristic says the number of constant-radius
Hessian-metric balls is controlled by

  V_H(S_A)=int_{S_A} sqrt(det H(theta)) dtheta.

We need show this metric volume is poly_d(A), not t^{c}.

Counterexample check: pure quadratic
  F(theta)=t||theta||^2/2.
Then H=tI, S_A radius sqrt(2A/t), and
  V_H = t^{d/2} * Vol(radius sqrt(A/t))
      = C_d A^{d/2}.

The t factors cancel exactly.

This suggests potential sublevel shrinkage compensates high curvature.

## General convex change-of-variables intuition

In 1D,
  int_{F-Fmin<=A} sqrt(F''(theta)) dtheta
should be O(sqrt(A)+A) under logistic generalized self-concordance.

In d dimensions, if a comparable theorem holds,

  V_H(S_A) <= C_{d,R,alpha} poly(A),

then with A=O(log t) the desired cover follows.

## Attempt via gradient map

For strongly convex F, gradient map theta -> p=nabla F(theta) has Jacobian
det H(theta).

But metric volume uses sqrt(det H), not det H.

Cauchy-Schwarz:

  int_S sqrt(det H)
  <= sqrt( Vol(S) * int_S det H ).

And
  int_S det H(theta) dtheta
  = Vol( nabla F(S) )
if gradient map is injective (true under strong convexity).

We can bound Vol(S):
  S subset ball radius sqrt(2A/alpha),
so
  Vol(S)<=C_d (A/alpha)^{d/2}.

Need bound gradient image volume.

For theta in S_A, can ||nabla F(theta)|| be bounded polynomially in A
independently of t?

This is the key.

## Gradient-height bound

For convex F with generalized self-concordant Hessian variation, high gradient
at low potential height should be impossible.

Along direction
  v=nabla F(theta)/||nabla F(theta)||,
consider moving backward from theta toward decreasing F.

Smooth convexity alone gives
  ||grad F||^2 <= 2 L (F-Fmin),
but L can be O(t).

Need replace global L by local directional curvature and use logistic
curvature-height coupling.

At theta, let g=||nabla F(theta)|| and v=gvec/g.
The directional curvature at theta is h=v^T H(theta)v.

The ray curvature-height theorem from the MODE controls h using radial
direction from mode, not gradient direction at theta unless aligned.

So again transverse geometry matters.

## Potential counterexample search conceptually

Could F have a thin curved valley inside low sublevel set, with very large
transverse curvature t and length O(1), making metric volume ~sqrt(t)?
For generic strongly convex functions yes.

Can logistic ridge sums realize it with fixed d and bounded features?
Example in d=2:
  many observations along e2 create curvature ~t in theta2,
  while theta1 has only prior curvature.
Then
  F~alpha theta1^2/2 + t c theta2^2/2 locally.
S_A has widths sqrt(A) and sqrt(A/t).
Metric volume again ~A: t cancels.

If the high-curvature ridge bends with theta1, logistic ridge directions are
FIXED linear x_i, so valley orientation can vary only through changing
positive weights on fixed rank-one matrices.

Could many directions produce rotating high-curvature axes across a long
low-potential path? Possibly, but each direction with high curvature also
contributes potential.

No proof yet.

## Determinant expansion route

H=alpha I + sum_i w_i x_i x_i^T.

By Cauchy-Binet/mixed determinant expansion, det H is a sum over subsets of at
most d observations of products of weights times squared volumes of feature
vectors, plus alpha terms.

sqrt(det H) may be bounded by sum over subset square roots.

Then metric volume reduces to integrals like

  int_{S_A} prod_{i in I} sqrt(w_i(theta)) dtheta,
  |I|<=d.

Since
  sqrt(w_i)=1/[2 cosh(x_i^T theta/2 + shift)]
has exponential decay along its ridge coordinate.

For fixed d, each term may have an integral bounded independently of t, but
there are O(t^d) subsets -- fatal unless coefficient sums can be controlled
by potential height or determinant inequalities.

However repeated identical directions yield combinatorial t^d terms that
collapse to t^{d/2} curvature and are canceled by sublevel width. Need exploit
aggregate matrices, not enumerate subsets.

## Status

No counterexample found, but no proof of polylog Hessian-metric volume yet.

The fixed-d positive theorem now hinges on a meaningful geometric statement:

  Conjecture (Logistic sublevel metric-volume bound):
  For fixed d,R,alpha,
    int_{F-Fmin<=A} sqrt(det nabla^2F(theta)) dtheta
    <= C_{d,R,alpha} poly(A),
  uniformly over number of logistic ridge terms t.

If true, G1 closes immediately for A=O(log t).
If false, a counterexample may kill the current cubature architecture.

This conjecture is now the exact next theorem/counterexample target.
