# Anisotropic integration route: certified scale audit

Let F be the exact/surrogate convex logistic posterior potential with quadratic
Gaussian prior:
  F(theta) >= ||theta||^2/(2s^2) + affine/data terms.

At the mode theta_hat, let
  H=U diag(lambda_1,...,lambda_d) U^T,
with lambda_j>=s^{-2}.

We seek a coordinate transform that uses local curvature where reliable but
never assumes it globally.

## Safe prior-scale localization

For a globally alpha=s^{-2} strongly log-concave probability distribution,
standard concentration of Lipschitz functions implies each fixed unit
projection around its mean is sub-Gaussian with variance proxy s^2.

Thus, around the posterior MEAN mu (not necessarily the mode),

  P(|u_j^T(theta-mu)| > s sqrt(2 log(2d/delta)))
  <= delta/d

under standard strong-log-concavity concentration assumptions.

A union bound yields a coordinate box around mu with side half-width
  O(s sqrt(log(d/delta)))
containing probability at least 1-delta.

For fixed d and delta=t^{-c}, each Euclidean coordinate width is
  O(s sqrt(log t)).

This is already polylogarithmic in t and does NOT require Hessian whitening.

## Important correction

The original theta domain can be unbounded, but concentration truncates the
integral to a box of width O(s sqrt(log t)) around the mean.

However the mean is not directly known. The mode-mean distance for a strongly
log-concave distribution can be O(s sqrt(d)) under suitable bounds, so for
fixed d one may enlarge a mode-centered box by a constant-in-t amount.

This requires a cited/proved mean-mode inequality before final use.

## Quadrature on growing box

After truncation, each coordinate interval has length O(s sqrt(log t)).
The integrand is analytic only up to complex singularities inherited from
logistic factors at theta^T x = i pi(2k+1).

In a coordinate direction v, the nearest singularity distance can be as small
as pi/|v^T x_i| >= pi/R.

Thus the analytic strip width is constant while the REAL interval length grows
as sqrt(log t).

For Chebyshev approximation on an interval of length W=Theta(s sqrt(log t)),
the scaled strip width is Theta(1/W), giving degree roughly

  n = O(W log(1/eps))
    = O(s sqrt(log t) * log t)
    = O((log t)^{3/2})

for eps=t^{-c}, up to constants R,s.

For fixed d, tensor-product quadrature then uses

  n^d = O((log t)^{3d/2})

nodes.

THIS IS POLYLOGARITHMIC IN t FOR FIXED d.

## Concentration versus integrand normalization

We integrate numerator and denominator. To guarantee log-evidence error
O(1/t), absolute quadrature error must be controlled relative to the
denominator after a stable recentering.

Subtract F(theta_hat) before exponentiation:
  exp(-(F(theta)-F(theta_hat))).
The denominator over the localized box is not exponentially tiny merely due
to the global normalizer; local lower bounds around the mode are needed to
turn uniform/absolute cubature error into relative error.

For fixed d, strong convexity gives upper decay but not a lower local volume
without an upper Hessian bound. Logistic Hessian satisfies
  nabla^2 F <= s^{-2}I + (1/4) sum_i x_i x_i^T,
whose max eigenvalue can be O(t R^2).

Thus the mode peak can have width t^-1/2 in high-curvature directions and the
localized denominator can be as small as t^{-d/2} times constants.

This is still only POLYNOMIALLY small in t for fixed d.

Therefore to achieve relative error O(1/t), an absolute quadrature error of
roughly t^{-(1+d/2)} is sufficient in the worst crude bound.

Its logarithm is O(log t), so analytic approximation degree remains
O((log t)^{3/2}) on the sqrt(log t) box.

This is promising.

## Crude fixed-d complexity target

Per coordinate polynomial/quadrature degree:
  n = O((log t)^{3/2})
with constants depending on d,R,s and desired regret accuracy.

Tensor-product node count:
  O((log t)^{3d/2}).

Evaluation of Fhat at a node using the moment-polynomial representation costs
poly_d(log t).

Hence total prediction work remains
  poly_d(log t)
for FIXED d.

## Remaining rigor gaps before theorem

1. formal strong-log-concave coordinate concentration around a computable
   center (mode vs mean);
2. explicit analytic-strip bound for the CONVEXITY-PRESERVING polynomial
   surrogate: note a polynomial surrogate has no logistic singularities, but
   exp(-polynomial) can grow rapidly in complex directions; bounds must use
   polynomial coefficient control, not original logistic singularities;
3. lower bound on localized denominator sufficient for relative quadrature
   accuracy;
4. deterministic cubature error theorem with all constants;
5. mode computation and finite precision.

So we now have a plausible polylog fixed-d integration SCALING argument, not
yet a finished proof.

Paper gate remains closed until these are made rigorous.
