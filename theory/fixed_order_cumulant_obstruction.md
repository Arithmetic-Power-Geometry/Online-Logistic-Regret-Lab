# Fixed-order cumulant compression: obstruction program

## Empirical gate

Oracle tests give the compressor exact moments of the true EW posterior.

Mean+covariance already fail to reach the required O(t^-2) predictive error on
the 2D sequence:
  n times (x=e2,y=+1),
  n times (x=e1-e2,y=-1),
  query x=e1.

Adding the exact directional third central moment through a first Edgeworth
correction improves constants but still fails the scale. At n=64 (t=129),
the third-order prediction error is about 1.99e-3, so t^2 error is about 33,
not O(1).

Therefore we stop adding moments one at a time.

## Why finite cumulants are not update-closed

Let Z=theta^T x be a queried projection. A posterior update by a new example
(v,y) multiplies the density by

  L(theta)=sigma(y theta^T v).

The updated raw directional moment is

  E_new[Z^j] = E[Z^j L(theta)] / E[L(theta)].

Unless v is collinear with x and the posterior has special structure, the
numerator depends on joint expectations between Z^j and a nonlinear function
of another projection theta^T v.

Consequently the first r directional moments/cumulants of Z do not algebraically
determine their own next update for arbitrary changing directions.

This is an algebraic non-closure statement, NOT yet an impossibility theorem.

## Precise theorem target: reachable fixed-order insufficiency

For every fixed r, seek two finite online histories H,H' in fixed low dimension
(e.g. d=2 or 3), under the same prior, such that at a chosen query x:

  |E_H[Z^j]-E_H'[Z^j]| <= eta,  j=1,...,r,

but

  |E_H[sigma(Z)]-E_H'[sigma(Z)]| >= Delta,

with Delta large compared with the O(t^-2) accuracy required by the
approximation-to-regret bridge.

Stronger version: match a complete tensor of posterior moments through total
degree r, not merely moments along x.

If eta can be made zero (or sufficiently smaller than Delta) for reachable
logistic posteriors, any compressor whose state is only those moments cannot
guarantee the required predictive accuracy.

## Computational search formulation

Parameterize two histories using a small dictionary of 2D directions and
integer label counts. For each history compute an exact-grid posterior.

Optimize

  objective =
    prediction_separation
    - lambda * moment_mismatch,

where moment_mismatch compares all monomials theta1^a theta2^b with a+b<=r.

Search first for r=2 and r=3. Existing oracle examples show failure of a
specific Gaussian/Edgeworth reconstruction but do NOT yet give matched-moment
pairs; this search aims at the stronger representation-level counterexample.

## If found

1. refine grid;
2. verify stability under larger integration radius/resolution;
3. turn numerical pair into a symbolic/continuity existence argument;
4. generalize from r=2,3 to arbitrary fixed r if possible;
5. only then perform novelty search and consider an obstruction paper.

## If not found

Do not infer sufficiency. Expand history dictionary/dimension once. If still
absent, return to a positive representation such as adaptive basis/coreset
rather than endlessly searching.

## Paper gate

The current oracle failures alone are useful evidence but are not enough for
the main paper.

Start writing an obstruction paper when a reachable matched-state/separated-
prediction theorem is rigorous and prior-art checked.

Start writing an algorithm paper if a compact adaptive representation instead
achieves a summable predictive error schedule and hence O(log T) approximation
tax.
