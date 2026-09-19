# Oracle mean-covariance PRC: decisive counterexample

The exact-grid experiment oracle_mean_cov_prc_2d.py gives the approximation
the TRUE EW posterior mean and covariance before replacing the queried marginal
by the matched Gaussian. Thus updater error is zero; only representation error
remains.

For the adversary:
1. n positive observations along e2;
2. n negative observations along e1 + s e2;
3. query e1,

two regimes appear.

For s=+1 the matched Gaussian error decreases strongly; at n=64 (t=129):
  absolute error = 2.5083e-5,
  t^2 error = 0.4174.

For s=-1 it does not achieve the required t^-2 scale; at n=64:
  absolute error = 2.6164e-3,
  t^2 error = 43.5392.

Across n=4,8,16,32,64 the s=-1 t^2 error grows:
  0.2227, 0.8311, 3.1639, 12.0298, 43.5392.

Therefore exact posterior mean + covariance are NOT uniformly sufficient for
the predictive accuracy schedule required by our log-loss bridge.

This kills the pure Gaussian / Laplace / covariance-only / Schur-only
representation route as a uniform solution strategy.

It does NOT prove every O(d^2)-memory algorithm fails: another O(d^2)
representation could encode different information.

Next test: add exact directional third central moment and use a first Edgeworth
correction. If this still fails at t^-2 scale, move to a hierarchy/lower-bound
question rather than tuning Gaussian updates.
