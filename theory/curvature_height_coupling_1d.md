# Curvature-height coupling for 1D logistic potentials

Let F be a one-dimensional logistic posterior potential with quadratic prior:

  F''(theta)=alpha + sum_i w_i(theta) x_i^2,
  alpha>0,
  w_i(theta)=sigma(a_i) sigma(-a_i),
  a_i=y_i x_i theta,
  |x_i|<=R.

Let theta_hat be an interior minimizer, so F'(theta_hat)=0.
Set delta=theta-theta_hat and
  DeltaF(delta)=F(theta_hat+delta)-F(theta_hat).

## Log-Lipschitz curvature comparison

For each data curvature term,
  |d/dtheta log w_i(theta)| <= |x_i| <= R.

Hence for s between 0 and delta (take delta>=0),

  e^{-R(delta-s)} w_i(theta_hat+delta)
  <= w_i(theta_hat+s)
  <= e^{R(delta-s)} w_i(theta_hat+delta).

Summing with x_i^2 and retaining alpha gives

  F''(theta_hat+s)
  >= alpha + e^{-R(delta-s)}
       [F''(theta_hat+delta)-alpha].

## Integrate twice backward from endpoint curvature

Since F'(theta_hat)=0,

  DeltaF(delta)
   = int_0^delta (delta-s) F''(theta_hat+s) ds.

Let H_delta=F''(theta_hat+delta).
Then

  DeltaF(delta)
  >= alpha delta^2/2
     + (H_delta-alpha)
       int_0^delta (delta-s)e^{-R(delta-s)} ds.

With u=delta-s,

  J_R(delta)
   := int_0^delta u e^{-Ru} du
    = [1-(1+R delta)e^{-R delta}]/R^2.

Therefore the EXACT lower bound is

  DeltaF(delta)
  >= alpha delta^2/2
     + (H_delta-alpha) J_R(delta).

Thus

  H_delta
  <= alpha
     + [DeltaF(delta)-alpha delta^2/2]/J_R(delta)
  <= alpha + DeltaF(delta)/J_R(delta).

## Two regimes

For 0<=R delta<=1, Taylor bounds give
  J_R(delta) >= c delta^2
for a universal c>0 (e.g. a conservative c=1/6 works).

Hence

  delta^2 H_delta
  <= alpha delta^2 + C DeltaF(delta).

Since alpha delta^2/2 <= DeltaF,

  delta^2 H_delta <= C' DeltaF(delta).

So in the LOCAL regime,

  H_delta <= C DeltaF(delta)/delta^2.

For R delta>=1,
  J_R(delta) approaches 1/R^2 and is bounded below by a constant/R^2.
Thus

  H_delta <= alpha + C R^2 DeltaF(delta).

This is also a curvature-height coupling, but without delta^-2.

## What the complex contour needs

In the complex bound,

  exponent penalty = (eta^2/2) C_q H_delta.

We are free to choose the imaginary contour width eta.

Choose it adaptively relative to real displacement scale:
  |eta| <= c min(delta,1/R)
away from the mode.

Then:
- if R delta<=1, eta^2 H_delta <= c^2 delta^2 H_delta
  <= C c^2 DeltaF;
- if R delta>=1, eta^2<=c^2/R^2 and
  eta^2 H_delta <= c^2 alpha/R^2 + C c^2 DeltaF.

Thus for sufficiently small c,

  -DeltaF + C_q eta^2 H_delta/2
  <= -kappa DeltaF + C0

for some kappa>0 and constant C0 depending on alpha,R,q,c.

This means complex magnitude DECAYS with real potential height on an adaptive
tube whose imaginary width is proportional to min(|delta|,1/R).

## Problem at the mode

At delta=0 the adaptive width above collapses to zero, but near the mode we
should instead use the whitened curvature scale.

For |delta| <= c0/R, endpoint/local curvature is comparable to H0:
  F''(theta_hat+delta) <= alpha+e^{R|delta|}(H0-alpha)
  <= C H0.

Choose
  |eta| <= c/sqrt(H0).

Then
  eta^2 F'' <= C c^2,
so complex magnitude is O(1) in a fixed-width strip in whitened coordinate
u=sqrt(H0)delta.

## Combined analytic tube

A valid piecewise tube around the real integration path has half-width

  eta(delta)
   = c * max? / piecewise:
   near mode: c/sqrt(H0);
   away: c min(|delta|,1/R).

To maintain a connected tube, use a lower envelope such as

  eta(delta)
   = c min(
       1/R,
       max(1/sqrt(H0), |delta|)
     )

subject to verifying transition constants.

In whitened u coordinate, near-mode width is constant.
Away from mode the width grows with |u| until saturating at
  c sqrt(H0)/R.

This geometry is favorable for piecewise Chebyshev approximation.

## Main result

We HAVE proved the missing curvature-height inequality:

  DeltaF(delta)
  >= alpha delta^2/2
     +(F''(theta_hat+delta)-alpha)
       [1-(1+R|delta|)e^{-R|delta|}]/R^2.

This is exact under the logistic curvature log-Lipschitz property.

It yields:
- local: delta^2 F''(theta_hat+delta) <= C DeltaF(delta);
- far: F'' <= alpha + C R^2 DeltaF.

Combined with the exact complex sec^2 curvature bound, complex magnitude is
controlled on an adaptive analytic tube.

## Remaining numerical theorem

We no longer need a global fixed-width Bernstein ellipse. Need cover the
O(sqrt(log t)) whitened mass interval by O(log t) or O(polylog t) overlapping
subintervals, each with an ellipse fitting inside the adaptive tube.

If each subinterval uses O(log t) Chebyshev nodes for t^{-C} local error and
there are O(log t) intervals, total 1D nodes O(log^2 t) (or a nearby
polylog exponent).

This is now a standard-looking geometric partition argument, but constants
must be written.

Paper gate has not fired until that covering/error theorem is explicit.
