# Curvature-weighted local expansion of log cosh

Let
  h(z)=log cosh(z/2).

Then
  h'(z)=1/2 tanh(z/2),
  h''(z)=1/4 sech^2(z/2)=sigma(z)sigma(-z).

For a base point a and increment u, Taylor's theorem in integral form gives

  h(a+u)
   = h(a)+h'(a)u
     + u^2 int_0^1 (1-r) h''(a+r u) dr.

Define
  omega(a,u)=2 int_0^1 (1-r) h''(a+r u) dr.

Then exactly

  h(a+u)-h(a)-h'(a)u = (1/2) omega(a,u) u^2,

with 0 < omega(a,u) <= 1/4.

For observation i, take
  a_i=theta_bar^T x_i,
  u_i=(theta-theta_bar)^T x_i.

Summing,

  sum_i [h(theta^T x_i)-h(theta_bar^T x_i)]
   = g_bar^T (theta-theta_bar)
     + (1/2) sum_i omega_i(theta) u_i^2,

where
  g_bar=sum_i h'(a_i)x_i.

Thus the entire nonlinear local variation is a linear term plus a
curvature-weighted quadratic form with PATH-AVERAGED logistic curvatures.

## Comparison with base curvature

Base weights:
  w_i=h''(a_i).

The central technical question is whether omega_i(theta) can be compared to
w_i by a controlled factor inside a posterior-relevant local region.

Since
  log h''(z) = const - 2 log cosh(z/2)
and
  |d/dz log h''(z)| = |tanh(z/2)| <= 1,

we have the log-Lipschitz inequality

  exp(-|u|) h''(a)
  <= h''(a+r u)
  <= exp(|u|) h''(a)

for r in [0,1].

Therefore

  exp(-|u|) w_i <= omega_i(a,u) <= exp(|u|) w_i.

(Using 2 int_0^1(1-r)dr=1.)

Hence if |u_i|<=rho uniformly on the local region,

  e^{-rho} w_i <= omega_i <= e^{rho} w_i.

This yields

  remainder
  <= (e^rho/2)
      sum_i w_i [(theta-theta_bar)^T x_i]^2.

Let
  H=s^{-2}I+sum_i w_i x_i x_i^T.

Then
  sum_i w_i u_i^2
   <= (theta-theta_bar)^T H (theta-theta_bar).

So inside an H-ellipsoid
  ||theta-theta_bar||_H <= r,

the exact nonlinear Taylor remainder is <= (e^rho/2) r^2.

## Leverage control of rho

For each i,

  |u_i|
   <= ||theta-theta_bar||_H sqrt(x_i^T H^{-1}x_i)
   <= r sqrt(l_i),

where l_i=x_i^T H^{-1}x_i.

The problem is that UNWEIGHTED l_i can be large for saturated examples whose
w_i is tiny. But their contribution to the quadratic remainder is multiplied
by w_i.

This suggests avoiding a max-rho bound and summing an inequality that retains
w_i, rather than paying exp(max |u_i|).

## Exact weighted leverage identity

  sum_i w_i l_i
   = tr(H^{-1} sum_i w_i x_i x_i^T)
   = d-s^{-2}tr(H^{-1})
   <= d.

This is the candidate replacement for dependence on t.

## Breakthrough target

Find a summable bound for the higher-than-quadratic/local-sketch error of the
form

  sum_i w_i l_i * Psi(r sqrt(l_i))

where Psi grows slowly enough that the weighted leverage identity and bounded
features/prior control make the total poly(d,B,log T), independent of t.

If achieved, combine with a sketch of the weighted local quadratic/higher
features and the centered-local posterior stability lemma.

This note establishes the exact expansion and the curvature/leverage mechanism;
the final summability bound is still open.
