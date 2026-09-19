# Weighted leverage summability: deterministic bound

Let
  H = s^{-2} I + sum_i w_i x_i x_i^T,
with ||x_i|| <= R and 0 < w_i <= 1/4. Define
  l_i = x_i^T H^{-1} x_i.

## Universal leverage cap

Since H >= s^{-2} I,
  H^{-1} <= s^2 I,
hence
  0 <= l_i <= s^2 ||x_i||^2 <= s^2 R^2 =: Lmax.

Also exactly,
  sum_i w_i l_i
   = d - s^{-2} tr(H^{-1})
   <= d.

Therefore for ANY nondecreasing nonnegative function Psi on [0,Lmax],

  sum_i w_i l_i Psi(l_i)
  <= Psi(Lmax) sum_i w_i l_i
  <= d Psi(s^2 R^2).

This removes t completely whenever the dangerous correction can be expressed
as w_i l_i times a monotone function of leverage alone.

More generally, for a local H-radius r and a nondecreasing Phi,

  sum_i w_i l_i Phi(r sqrt(l_i))
  <= d Phi(r s R).

Thus the weighted summability target itself is solved deterministically.

## Important limitation

If Phi grows exponentially, e.g. Phi(q)=exp(q), the bound becomes
  d exp(r s R),
which is independent of t but may be exponential in B/R/local radius and is
not automatically poly(d,B).

So the next problem is no longer summability over history. It is controlling
the growth of the curvature-comparison function without an exponential
local-radius penalty.

## Exact logistic curvature ratio

For h''(z)=1/(4 cosh^2(z/2)),
  h''(a+u)/h''(a)
   = [cosh(a/2)/cosh((a+u)/2)]^2.

The generic log-Lipschitz bound <= exp(|u|) is sharp in saturated tails:
for a -> +infinity and negative u that moves back toward zero, the ratio is
approximately exp(|u|).

Therefore a global polynomial replacement for exp(|u|) is impossible without
additional localization/truncation.

## New frontier

We have now eliminated the T factor exactly:
  sum_i w_i l_i <= d
and
  l_i <= s^2 R^2.

The remaining issue is to avoid paying exp(r s R).

Possible route:
split examples into
1. stable-curvature set |u_i| <= q, paid by e^q d;
2. large-displacement set |u_i|>q, controlled by posterior tail probability
   in the H metric / leverage threshold.

Because |u_i| <= r sqrt(l_i), a large displacement implies
  l_i > q^2/r^2.
Weighted leverage then gives
  sum_{large} w_i <= (r^2/q^2) sum_i w_i l_i <= d r^2/q^2
only after suitable weighting; this needs careful formulation.

Status:
- history-length summability: PROVED;
- polynomial parameter dependence: NOT proved;
- next target: thresholded leverage/localization bound.
