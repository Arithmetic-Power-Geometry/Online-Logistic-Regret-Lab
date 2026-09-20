# One-dimensional whitened analytic quadrature

We analyze the EXACT 1D logistic posterior first; the compressed surrogate can
then be used only to evaluate/approximate its potential.

Let theta_hat be an interior mode and
  H0=F''(theta_hat)>0.
Define
  u=sqrt(H0)(theta-theta_hat).

The recentered integrand is
  phi(u)=exp(-(F(theta_hat+u/sqrt(H0))-F(theta_hat))).

Prediction numerator multiplies phi by
  sigma(y x (theta_hat+u/sqrt(H0))).

We integrate over the mass-bearing interval
  |u|<=U_t, U_t=C sqrt(log t).

## Complex singularity geometry improves after whitening

A logistic factor has singularities when
  y x theta = i pi(2k+1)
modulo real shifts in the complex plane.

In the u coordinate, imaginary displacement Im(u)=v corresponds to
  Im(theta)=v/sqrt(H0).

Thus a factor with |x|<=R reaches its nearest logistic singularity only when

  |v| >= pi sqrt(H0)/|x|
       >= pi sqrt(H0)/R.

Therefore the analytic strip in u has half-width at least

  a_t = pi sqrt(H0)/R.

Since H0>=alpha=s^{-2}, a_t>=pi/(sR), a positive constant.
When H0 grows with t, the strip becomes WIDER, not narrower.

This is the key resolution of the narrow-peak paradox.

## Scaled Bernstein geometry on the truncated u interval

Map
  u=U_t z, z in [-1,1].

The strip half-width in z is

  a_t/U_t >= [pi sqrt(H0)/R]/[C sqrt(log t)].

Worst case occurs at minimal H0=alpha, giving

  a_z = Omega(1/sqrt(log t)).

For a function analytic and suitably bounded in this strip, Chebyshev error
behaves like

  exp(-Omega(n a_z))
  = exp(-Omega(n/sqrt(log t))).

To obtain error t^{-p}=exp(-p log t), it suffices that

  n=O((log t)^{3/2}).

If H0 grows, required degree is smaller.

Thus the earlier heuristic O((log t)^{3/2}) degree emerges rigorously from
singularity distance, PROVIDED complex magnitude is controlled.

## Complex magnitude of logistic cumulative potential

Instead of approximating exp(-F) via F=log losses, use the unnormalized
likelihood PRODUCT directly:

  exp(-F(theta))
   = prior_factor(theta) prod_i sigma(y_i x_i theta).

Each sigma is meromorphic, not entire.

Inside a substrip staying a fixed fraction gamma<1 away from all poles, the
magnitude of each factor can exceed 1 in complex directions. A naive product
bound C^t is exponential in t, which would require n potentially
O(t sqrt(log t)) and destroy the result.

Therefore singularity distance alone is NOT sufficient.

Need exploit normalization/recentering and cancellation of product growth.

## Log-potential complex real-part route

For complex theta near the real axis,
  Re[F(theta)-F(theta_hat)]
controls |phi|.

A second-order complex Taylor estimate gives roughly

  Re(F(theta_hat+delta+i eta)-F(theta_hat))
  >= real-axis growth - (1/2) M eta^2

where M can be O(t R^2).

In u coordinates eta=v/sqrt(H0). Since H0 can be much smaller than tR^2 in
some sequences, the penalty M/H0 * v^2 can still be O(t) in worst case.

At the mode, however H0 is the ACTUAL weighted curvature, while M=tR^2/4 is
the crude unweighted maximum. Saturated observations can make M/H0 huge even
though their complex contribution may remain benign locally.

A refined bound must use the local weighted curvature, not t/4.

## Local complex curvature bound

For each logistic term, within imaginary logit displacement |Im z|<=q<pi,
the ratio of complex second derivative magnitude to real curvature at the same
real part is bounded by a function C(q), because

  g''(z)=1/[4 cosh^2(z/2)].

Specifically, for z=a+ib and |b|<=q<pi,

  |g''(a+ib)| / g''(a)
is bounded by a finite C(q) independent of a.

Therefore if
  |Im(theta)| R <= q,
then

  |F''(theta_complex)-prior_curvature|
  <= C(q) [F''(Re theta)-prior_curvature]

plus the prior term.

In whitened coordinates, choosing a CONSTANT imaginary width
  |Im u|<=q sqrt(H0)/R
keeps complex curvature tied to real weighted curvature rather than t.

This is the crucial analytic-control lemma candidate.

## Consequence if lemma is used

On the mass core |Re u|<=U_t, real curvature relative to H0 can change, but
the earlier localization envelope shows regions of severe change carry large
potential.

A fully uniform complex bound still requires combining:
- curvature-ratio lemma in imaginary direction;
- real core-tail localization.

This is close but not yet a one-line Bernstein theorem.

## Alternative: piecewise core integration

Split the u interval into O(polylog t) slabs according to potential height,
not Euclidean width. On each slab:
- posterior magnitude is at most e^{-j};
- required absolute accuracy can be relaxed proportionally;
- local analytic scale is set by local curvature.

This avoids demanding one global complex supremum.

## Status

PROVED/clear:
- whitening moves logistic poles to distance >=pi sqrt(H0)/R;
- worst-case scaled strip over U=O(sqrt(log t)) is
  Omega(1/sqrt(log t));
- absent magnitude blowup, degree O((log t)^{3/2}) suffices.

NEW remaining lemma:
control complex magnitude by local weighted curvature/potential height,
avoiding a C^t product bound.

The fixed-d paper gate has NOT fired yet.
