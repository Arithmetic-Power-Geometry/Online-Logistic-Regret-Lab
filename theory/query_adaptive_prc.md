# Query-Adaptive Predictive Coreset (QAPC), candidate 0

## Goal

At round t, x_t is known before prediction. Exact EW predicts

  p_t = E_{Q_t}[sigma(theta^T x_t)].

We do not need a globally accurate representation of Q_t if we can approximate
the one-dimensional push-forward of

  Z_t = theta^T x_t

well enough to estimate E[sigma(Z_t)].

## Exact decomposition

Write e=x/||x|| and decompose

  theta = z e + w,  w perpendicular to e.

The marginal density of z under the posterior is proportional to

  prior_z(z) *
  E_{w | z, prior}[
    product_{s<t} sigma(y_s (z e^T x_s + w^T x_s))
  ].

Thus every historical point contributes through both:
- its projection a_s=e^T x_s onto the query direction;
- its orthogonal component b_s=x_s-a_s e.

A summary retaining only scalar projections a_s is NOT exact in general,
because the orthogonal integration couples historical factors.

## Candidate 0: projection-only PRC

Approximate each historical factor by deleting its orthogonal component:

  sigma(y_s theta^T x_s)
  approximately
  sigma(y_s a_s z).

Then the query-specific approximate marginal is one-dimensional:

  qhat_t(z) proportional to
  prior_z(z) product_{s<t} sigma(y_s a_s z).

Prediction is

  q_t = integral sigma(||x_t|| z) qhat_t(z) dz.

This can be evaluated by 1D quadrature and historical projected factors can be
compressed by binning/coreset methods.

## Immediate theoretical warning

The approximation discards correlations between z and orthogonal posterior
directions. There is no reason for the resulting error to be O(t^-2) under
arbitrary adversarial sequences.

We therefore treat candidate 0 as a falsification baseline, not a proposed
theorem.

## Smallest adversarial mechanism

In d=2, let the query be x=e1. Historical vectors

  x_s = a e1 + b e2

can induce strong posterior information about theta_2. Because the same factors
couple theta_1 and theta_2, integrating theta_2 after learning it can shift the
marginal prediction for theta_1.

Projection-only compression sees only a and misses this mechanism.

A particularly sharp family is:
- many observations along e2, learning the sign/magnitude of theta_2;
- then many observations along e1+e2 or e1-e2;
- query along e1.

The learned theta_2 converts diagonal evidence into information about theta_1,
while a projection-only history cannot represent that conditional effect.

## Candidate 1 if candidate 0 fails

Retain conditional first and second orthogonal moments for each query:
- projected coefficient a_s,
- covariance coupling e^T H^{-1} b_s,
- local curvature weight.

This becomes a query-adaptive Schur-complement correction rather than a pure
projection.

But candidate 1 should be attempted ONLY after candidate 0 is quantitatively
falsified and its failure mechanism measured.

## Paper gate

No paper from candidate 0 alone.

Paper trigger:
- a query-adaptive compression with provable O(t^-2) predictive error (or a
  summable relative-to-boundary schedule) and poly(d,log T,B) resources; OR
- a rigorous lower bound proving a meaningful query-adaptive compression class
  cannot meet that schedule.

