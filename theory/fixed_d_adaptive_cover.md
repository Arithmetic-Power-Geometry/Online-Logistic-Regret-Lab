# Fixed-d adaptive cover: geometric shell construction

We need cover the high-mass sublevel set

  S_A={theta in Theta:
       F(theta)-F(theta_hat)<=A},

with A=C log t, by local regions on which the analytic tube has constant
aspect ratio.

Strong convexity alpha gives
  S_A subset B(theta_hat, sqrt(2A/alpha))
so Euclidean diameter is O(sqrt(log t)).

A naive uniform cover at smallest mode scale t^-1/2 costs t^{d/2}; rejected.

## Radial dyadic shells in mode-Hessian norm

Let
  H0=nabla^2F(theta_hat),
  ||delta||_0=sqrt(delta^T H0 delta).

Define shells
  S_j={theta in S_A: 2^{j-1}<=||theta-theta_hat||_0<2^j},
with central S_0 at norm <=1.

Because H0<=alpha I+(tR^2/4)I=O(t)I and Euclidean radius of S_A is
O(sqrt(log t)), the maximum H0-radius can be
  O(sqrt(t log t)).
Thus the number of dyadic RADIAL shells is only
  O(log t).

The problem is angular covering inside a shell.

## Angular resolution from ridge geometry

At Euclidean radius r, the adaptive complex/real local scale along a
direction is at least c min(max(H0-direction scale^-1,r),1/R) in the
one-dimensional argument.

For a d-dimensional cell centered at delta, a conservative isotropic cell
radius can be chosen proportional to
  min(1/R, ||delta||_2)
away from the mode, and H0-ellipsoidal radius constant near the mode.

Cover an annulus with Euclidean radius r and cells of radius c r:
the number of cells needed is O(c^{-d}), independent of r.

This is the key fixed-d geometric fact:
a dyadic annulus can be covered by a CONSTANT number (depending on d) of
relative-radius balls.

Therefore O(log t) dyadic shells need
  O(C_d log t)
cells before the outer scale saturates.

## Outer saturated region

When r>=1/R, use cells of fixed radius c/R.

The entire high-mass set lies in radius
  D=O(s sqrt(log t)).

A uniform fixed-radius cover then needs

  O((R D)^d)
   = O((log t)^{d/2})

cells for fixed R,s,d.

Thus total cell count

  N_cells
   = O_d(log t + (log t)^{d/2})
   = poly_d(log t).

This is the desired count.

## Boundary

Intersect cells with the bounded comparator ball Theta.
For integration, boundary cells become ball-box intersections rather than
rectangles. Simpler implementation options:
- integrate over a bounding box and multiply by the indicator of Theta
  (destroys analyticity at boundary);
- partition the ball with smooth/radial coordinates;
- use a cube comparator domain instead (changes comparator geometry);
- treat boundary with radial coordinates from origin/mode.

Therefore analytic cubature on a hard Euclidean-ball boundary still needs a
clean chart/parameterization argument.

A finite atlas of smooth charts for the ball boundary exists for fixed d,
but near the sphere the indicator is not analytic in Cartesian extension.

## Better bounded domain for theorem

Use a hypercube
  Theta=[-B,B]^d
instead of an l2 ball.
Any l2 comparator ||theta||_2<=B lies inside this cube, so regret against the
l2 comparator class is still valid.

Uniform prior on the cube has even simpler local mass:
for any theta* in cube and delta<=B, an axis-aligned inward box of side
delta exists, giving prior mass at least (delta/(2B))^d up to constants.

The compressed polynomial approximation only needs
  |theta^T x| <= ||theta||_2 ||x||_2
  <= B sqrt(d) R
on the cube.

For fixed d this only changes L=BR to B sqrt(d) R.

Most importantly, the integration domain is a BOX, exactly compatible with
tensor-product/adaptive Chebyshev cells, including boundary clipping.

This appears to remove the hard spherical-boundary chart issue while retaining
regret against every l2 comparator of radius B.

## Regret with cube prior

Let pi uniform on [-B,B]^d.
For comparator theta* with ||theta*||_2<=B (hence theta* in cube), choose an
axis-aligned box of side h=delta/sqrt(d) around/inward from theta* so every
point is within Euclidean delta.

Its prior mass is at least
  (h/(2B))^d
  = (delta/(2B sqrt(d)))^d.

Then

  Regret <= TR delta
            + d log(2B sqrt(d)/delta).

Choosing delta=1/(TR):

  Regret <= 1+d log(2B sqrt(d) R T).

Still O(d log T) for fixed parameters and dimension.

## Multivariate local Chebyshev cost

Each adaptive cell is a box/ellipsoid of constant analytic aspect after local
scaling. Enclose/parameterize by a box.

If degree n=O(log t) per coordinate, tensor-product nodes per cell are

  O((log t)^d).

Multiply by cell count
  O_d(log t+(log t)^{d/2}),

giving a conservative fixed-d prediction cost

  O_d((log t)^{3d/2} + (log t)^{d+1})

function evaluations,

hence poly_d(log t).

The polynomial surrogate Fhat can be evaluated from the update-closed tensor
state in poly_d(log t) arithmetic for fixed d.

## Remaining rigor items

1. Formalize that each relative-radius cell admits a multivariate polyellipse
   inside the adaptive complex tube; raywise control suggests it, but operator
   constants must be explicit.
2. Formal C^2 perturbation transfer exact F -> surrogate Fhat.
3. Mode finding for convex polynomial surrogate on a box to inverse-poly(t)
   accuracy in poly_d(log t) arithmetic/bit complexity.
4. Aggregate all approximation errors into log-loss regret.

These now look like technical closure items rather than a new conceptual
obstruction.

## Status

The fixed-d cell COUNT is polylogarithmic.
No polynomial-in-t geometric covering obstruction appears.

A cube prior/domain is preferable for the theorem:
- contains the desired l2 comparator ball;
- preserves O(d log T) Bayesian-mixture regret;
- bounded logits;
- analytic tensor-product integration geometry.

This is the strongest positive architecture so far.
