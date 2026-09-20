# Exact complex curvature ratio for logistic loss

For
  g(z)=log(1+exp(-z)),
we have
  g''(z)=1/[4 cosh^2(z/2)].

Let z=a+ib with real a,b and |b|<pi.

We compare |g''(a+ib)| to g''(a).

## Exact denominator identity

Using
  |cosh((a+ib)/2)|^2
   = sinh^2(a/2)+cos^2(b/2)
   = cosh^2(a/2)-sin^2(b/2).

Therefore

  |g''(a+ib)|
   = 1/[4 |cosh((a+ib)/2)|^2]

and

  |g''(a+ib)| / g''(a)
   = cosh^2(a/2)
     / [cosh^2(a/2)-sin^2(b/2)].

Since cosh^2(a/2)>=1,

  ratio
   = 1/[1-sin^2(b/2)/cosh^2(a/2)]
   <= 1/[1-sin^2(b/2)]
   = sec^2(b/2).

Thus the exact uniform bound is

  |g''(a+ib)| <= sec^2(b/2) g''(a),
  for |b|<pi.

This is independent of a.

## Consequence for arbitrary features

For complex theta=xi+i eta in 1D, factor i has
  a_i=y_i x_i xi,
  b_i=y_i x_i eta.

If |eta| R <= q<pi, then

  |g_i''(theta)|
  <= sec^2(q/2) g_i''(xi) x_i^2
(after including x_i^2 in theta derivatives).

Summing:

  |F''(xi+i eta)-prior''|
  <= sec^2(q/2) [F''(xi)-prior''].

With quadratic prior alpha theta^2/2, prior''=alpha exactly, so

  |F''(xi+i eta)|
  <= alpha + sec^2(q/2)[F''(xi)-alpha]
  <= sec^2(q/2) F''(xi).

This replaces the fatal crude O(tR^2) complex Hessian bound by the ACTUAL
real weighted curvature.

## Integrated complex bound around a real anchor

At a real anchor xi, for imaginary displacement eta with |eta|R<=q,

  F(xi+i eta)
   = F(xi)+ i eta F'(xi)
     - eta^2 int_0^1 (1-r) F''(xi+i r eta) dr.

Taking real parts and using the magnitude bound,

  Re F(xi+i eta)
  >= F(xi)
     - (eta^2/2) sec^2(q/2) F''(xi).

Hence

  |exp(-(F(xi+i eta)-F(theta_hat)))|
  <= exp(
       -(F(xi)-F(theta_hat))
       + (eta^2/2) sec^2(q/2) F''(xi)
     ).

This is the desired weighted-curvature complex magnitude estimate.

## In whitened coordinates

Let u=sqrt(H0)(theta-theta_hat).
Imaginary displacement eta=v/sqrt(H0).

Then

  magnitude <= exp(
    -DeltaF(real u)
    + [v^2/(2H0)] sec^2(q/2) F''(real theta)
  ).

If on the mass-bearing core the ratio
  F''(real theta)/H0
is polynomially bounded in t, the complex growth contributes only
exp(polylog) for v chosen according to the scaled Bernstein ellipse.

But we can do better: logistic curvature variation from the mode obeys

  F''(theta)-alpha
  <= exp(R|theta-theta_hat|)(H0-alpha)

for exact logistic potential.

On a whitened mass core |u|<=C sqrt(log t),

  |theta-theta_hat| <= C sqrt(log t/H0).

Therefore

  F''/H0
  <= alpha/H0
     + exp(C R sqrt(log t/H0)) (1-alpha/H0).

Worst case H0>=alpha constant gives
  exp(O(sR sqrt(log t))),
which is subpolynomial in t.

Thus log of the complex supremum can be bounded by subpolynomial factors, but
to preserve polylog degree we need the LOG supremum itself to be polylog.
Since
  exp(O(sqrt(log t)))
is not polylog, this crude real-curvature variation bound is still too weak.

## Sharper potential-height relation needed

Regions where F''/H0 becomes very large may have non-negligible potential
height, and the negative -DeltaF term in the magnitude bound can compensate.

The exact magnitude exponent is

  -DeltaF + C eta^2 F''.

We need prove on the relevant real interval a relation such as

  eta^2 F''(theta)
  <= C1 DeltaF(theta)+C2 polylog(t)

for the eta used by the approximation contour.

If true, complex supremum is polynomial/subexponential enough for
polylog-degree Chebyshev approximation.

## Result

The key complex-curvature lemma is PROVED exactly:

  |g''(a+ib)| <= sec^2(b/2) g''(a).

This is a strong reusable logistic analytic inequality.

The final quadrature proof is now reduced to coupling real potential height
with real curvature on the localized interval.
