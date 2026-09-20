# Convexity-preserving approximation of log cosh

The previous polynomial surrogate approximated
  h(z)=log cosh(z/2)
directly. Uniform function approximation does not guarantee convexity.

For curvature-adapted integration we want
  P''(z)>=0
on [-L,L].

## Curvature-first construction

Let
  w(z)=h''(z)=1/4 sech^2(z/2).

This is even, positive on the real axis, and analytic in |Im z|<pi.

Construct an even polynomial/rational approximation r_m(z) to w(z) satisfying

  sup_{|z|<=L} |r_m(z)-w(z)| <= eps_m

and enforce
  r_m(z)>=0
on [-L,L].

One simple sufficient method is:
1. approximate sqrt(w(z)) = (1/2) sech(z/2) on the real interval by a
   polynomial s_m(z);
2. set r_m(z)=s_m(z)^2.

Then r_m>=0 automatically.

Define P by integrating twice with the exact symmetry conditions

  P''(z)=r_m(z),
  P'(0)=h'(0)=0,
  P(0)=h(0)=0.

Then P is even and convex on [-L,L].

## Error propagation

If
  sup |r_m-w| <= eps,
then for |z|<=L,

  |P'(z)-h'(z)| <= L eps,

and

  |P(z)-h(z)| <= (L^2/2) eps.

Thus to obtain function error eta it suffices to approximate curvature to

  eps <= 2 eta/L^2.

For fixed L this preserves the same logarithmic-in-t degree order.

If eta_t=Theta(t^-2), curvature approximation needs eps_t=Theta(t^-2/L^2).

## Degree

sqrt(w)=1/(2 cosh(z/2)) has nearest poles at z=+-i pi, so polynomial
approximation on [-L,L] still converges geometrically with degree
  O(L log(1/eps))
up to explicit constants.

Squaring doubles the polynomial degree only by a constant factor.

Hence convexity preservation does not change the asymptotic
  O(BR log t)
degree target.

## Update-closed representation

P remains an even polynomial. Therefore
  sum_i P(theta^T x_i)
is still represented exactly by the same additive even-order symmetric moment
tensors.

So the curvature-first construction preserves:
- convexity;
- update closure;
- logarithmic degree in t for fixed B,R.

## Strong convexity

If the prior contributes ||theta||^2/(2s^2), then the surrogate potential has

  nabla^2 Fhat(theta)
    = s^{-2}I + sum_i r_m(theta^T x_i) x_i x_i^T
    >= s^{-2}I.

Thus the surrogate posterior is globally strongly log-concave.

This restores the foundation needed for mode uniqueness, concentration, and
Hessian-whitened integration.

## Remaining issue

The bounded-domain reference theorem earlier allowed a generic compactly
supported prior, while this strong-convexity statement uses a Gaussian
quadratic prior. A Gaussian truncated to ||theta||<=B has the quadratic
interior potential but a hard boundary. Alternatively use an unconstrained
Gaussian reference and control tails.

The reference-prior choice must be unified before a final theorem.

Status:
- convexity defect of direct polynomial approximation: repaired in principle;
- explicit approximation constants/construction still need formal proof/code;
- update closure retained.
