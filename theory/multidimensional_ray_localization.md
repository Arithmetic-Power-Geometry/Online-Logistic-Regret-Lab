# Multidimensional ray localization for logistic posterior potentials

Let

  F(theta)=alpha ||theta||^2/2 + sum_i g(y_i x_i^T theta),

where g(z)=log(1+exp(-z)), ||x_i||_2<=R, alpha>0.

Let theta_hat be an interior minimizer.

Fix any unit vector v and define the one-dimensional ray restriction

  f_v(r)=F(theta_hat+r v).

Then

  f_v'(0)=0

and

  f_v''(r)
   = alpha + sum_i w_i(theta_hat+r v) (x_i^T v)^2,

where
  w_i(theta)=sigma(y_i x_i^T theta)sigma(-y_i x_i^T theta).

## Directional curvature is log-Lipschitz termwise

For each nonzero directional term,

  d/dr log w_i(theta_hat+r v)
   = (d/dz log w_i(z)) y_i x_i^T v.

Since
  |d/dz log w_i(z)|<=1
and
  |x_i^T v|<=||x_i||<=R,

  |d/dr log w_i|<=R.

The multiplier (x_i^T v)^2 is constant along the ray.

Therefore every directional curvature contribution obeys the SAME
log-Lipschitz bound as in 1D.

## Endpoint directional-curvature versus ray potential height

For delta>=0,

  f_v''(s)
  >= alpha + e^{-R(delta-s)}
       [f_v''(delta)-alpha],
  0<=s<=delta.

Integrating twice and using f_v'(0)=0:

  f_v(delta)-f_v(0)
  >= alpha delta^2/2
     +(f_v''(delta)-alpha)
       J_R(delta),

where

  J_R(delta)
   =[1-(1+R delta)e^{-R delta}]/R^2.

Thus for EVERY unit v,

  Delta_v(delta)
  :=F(theta_hat+delta v)-F(theta_hat)

satisfies

  Delta_v(delta)
  >= alpha delta^2/2
     +(v^T nabla^2F(theta_hat+delta v)v-alpha) J_R(delta).

This is dimension-free except through the geometry of v.

Consequences:
- if R delta<=1,
    delta^2 v^T H(theta_hat+delta v)v <= C Delta_v(delta);
- if R delta>=1,
    v^T H(theta_hat+delta v)v
      <= alpha + C R^2 Delta_v(delta).

## Complex displacement along the same ray

Let theta=theta_hat+(r+i eta)v.

Each complex logit has imaginary part
  eta y_i x_i^T v,
whose magnitude <=R|eta|.

The exact scalar complex-curvature ratio therefore gives, for R|eta|<=q<pi,

  |v^T nabla^2F(theta_hat+(r+i eta)v)v|
  <= sec^2(q/2)
      v^T nabla^2F(theta_hat+r v)v.

So the entire 1D adaptive analytic-tube proof applies on EVERY real ray.

This is a rigorous multidimensional ray theorem.

## What it does NOT yet give

A d-dimensional integral is not a sum of independent ray integrals in a
Cartesian product without accounting for angular variables/Jacobian.

Two possible deterministic fixed-d constructions:

A. Spherical/radial:
   theta=theta_hat+r omega, omega in S^{d-1}.
   For each fixed omega, radial integral has the 1D adaptive structure.
   Need deterministic angular cubature for a function of omega whose
   complexity may grow with t.

B. Recursive coordinate integration:
   condition on d-1 coordinates and integrate the remaining coordinate.
   Each conditional slice is logistic-convex, but its slice minimizer depends
   on the fixed coordinates. Need control of how slice geometry varies.

C. Full multivariate analytic boxes:
   derive a polytube bound for imaginary vector eta using all directional
   Hessian quadratic forms. This may support tensor-product Chebyshev on
   adaptively whitened boxes.

## Multivariate complex Hessian bound

For real xi and complex displacement i eta, each logit imaginary part obeys

  |x_i^T eta| <= R ||eta||.

If R||eta||<=q<pi, the scalar sec^2 bound termwise yields, for any real v,

  |v^T [nabla^2F(xi+i eta)-alpha I] v|
  <= sec^2(q/2)
      v^T [nabla^2F(xi)-alpha I] v.

Hence in quadratic-form/operator sense,

  complex Hessian magnitude is controlled by
  sec^2(q/2) times the real Hessian,

interpreted termwise/bilinearly with a constant-factor extension.

For a complex line xi+i s eta,

  d^2/ds^2 F(xi+i s eta)
   = - eta^T nabla^2F(xi+i s eta) eta.

Therefore

  Re F(xi+i eta)
  >= F(xi)
     - (sec^2(q/2)/2)
       eta^T nabla^2F(xi) eta

provided R||eta||<=q and using the termwise curvature comparison.

This is the multivariate analogue of the 1D complex-magnitude inequality.

## Mode whitening

Let H0=nabla^2F(theta_hat), and u=H0^{1/2}(theta-theta_hat).

Near the mode, imaginary ellipsoids
  eta^T H0 eta <= c^2
give O(1) complex growth.

Along any real ray, if the local Hessian becomes large relative to the mode
metric, the ray curvature-height theorem forces corresponding potential
growth.

This strongly suggests an adaptive ellipsoidal cover of the
O(sqrt(log t))-potential sublevel set.

## Status

CLOSED:
- 1D curvature-height theorem extends exactly to EVERY direction v in R^d;
- complex sec^2 curvature control extends to complex displacement vectors;
- near-mode H0-whitened complex ellipsoid has constant analytic aspect.

OPEN:
- construct/count a deterministic adaptive ellipsoidal/box cover of the
  high-mass sublevel set in fixed d with poly_d(log t) cells;
- show each cell supports constant-aspect multivariate Bernstein/polyellipse;
- then tensor Chebyshev degree O(log t) per dimension gives poly_d(log t)
  nodes.

This is now a geometric covering problem, not a new logistic-analysis problem.
