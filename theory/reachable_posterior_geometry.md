# Reachable posterior geometry: repeated direction

Let u=sigma(theta) for a fixed direction and let pi_u be the push-forward of
the Gaussian prior.

After n_+ positive and n_- negative observations on that SAME direction,

  q_{n_+,n_-}(u)
  proportional to
  pi_u(u) u^{n_+}(1-u)^{n_-}.

Therefore:

1. Label ORDER is irrelevant.
2. The entire reachable family is indexed by only two nonnegative integers
   (n_+,n_-).
3. Generic truncated-moment nonuniqueness for arbitrary measures on [0,1]
   cannot automatically imply nonuniqueness inside this reachable family.

This substantially weakens the proposed repeated-direction impossibility route.

## Partition-function representation

Define

  Z(a,b)=integral pi_u(u) u^a(1-u)^b du.

Then under q_{a,b},

  M_j(a,b)=E[u^j]=Z(a+j,b)/Z(a,b).

Predictions are M_1(a,b).

The exact positive update is

  M_j(a+1,b)=M_{j+1}(a,b)/M_1(a,b),

and negative update is

  M_j(a,b+1)=[M_j(a,b)-M_{j+1}(a,b)]/[1-M_1(a,b)].

Although a generic moment vector leaks one order per update, the true state
(a,b) itself has constant dimension. If (a,b) can be recovered or tracked,
there is no information-theoretic growing-state obstruction in this special
case.

Indeed the online learner already knows a,b exactly from the history.

## Consequence

Repeated-direction data CANNOT support a lower bound claiming that every exact
predictive state must grow with T. A constant-size sufficient statistic
(a,b) exists for the likelihood exponents.

The remaining difficulty is evaluating

  Z(a+1,b)/Z(a,b)

efficiently and accurately for the Gaussian-logit prior, not representing the
history.

This distinction is crucial:

  history-state complexity != integral-evaluation complexity.

## Where an obstruction could still live

For arbitrary changing x_t in R^d, the posterior is

  q_t(theta) proportional to pi(theta)
  product_{s<t} sigma(y_s theta^T x_s).

Unless the x_s repeat from a finite dictionary, there is no fixed finite count
vector analogous to (a,b). The likelihood can acquire a new ridge direction
every round.

Thus a meaningful compression lower bound must exploit changing directions,
not repeated identical directions.

## Positive route retained

For a finite dictionary of r directions, counts (n_j^+,n_j^-) give a 2r
parameter exact likelihood representation. If r=poly(d) this is compact,
though integral evaluation remains hard.

For unrestricted adversarial directions, r can grow as T.

The next target is therefore:

  Can arbitrary logistic likelihood products be approximated, for predictive
  purposes, by a coreset / spectral / low-rank representation whose size is
  poly(d,log T,B) rather than O(T)?

This is the correct bridge to efficient EW.
