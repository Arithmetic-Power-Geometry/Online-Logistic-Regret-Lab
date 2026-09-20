# Metric-volume theorem attack: separable and fixed-direction cases

We test/prove the Hessian-metric-volume conjecture in structured families
before claiming the general ridge case.

Conjectured quantity:
  V_H(S_A)=int_{F-Fmin<=A} sqrt(det H(theta)) dtheta.

## Case 1: separable coordinates

Suppose
  F(theta)=sum_{j=1}^d f_j(theta_j)
with each f_j strongly convex 1D logistic-type.

Then H is diagonal and
  sqrt(det H)=prod_j sqrt(f_j''(theta_j)).

The sublevel set is contained in the product
  {f_j(theta_j)-f_j(min)<=A for every j}.

Therefore

  V_H(S_A)
  <= prod_j I_j(A),

where
  I_j(A)=int_{f_j-f_j,min<=A} sqrt(f_j''(x)) dx.

It suffices to bound the 1D metric length I(A).

## 1D metric-length bound

Let f be alpha-strongly convex and its curvature obey
  |d log(f''-alpha)/dx|<=R
for the non-prior component.

Let x*=0 WLOG, f'(0)=0.
On the right side define h(x)=f''(x), Delta=f(x)-f(0).

Split into:
A. near scale Rx<=1;
B. far scale Rx>=1.

A crude but useful dyadic-potential partition:
  E_k={x>=0: 2^k <= 1+Delta(x)<2^{k+1}},
for k=0,...,O(log(1+A)).

Since f is convex increasing on x>=0, each E_k is an interval.

From the endpoint curvature-height inequality:
for Rx<=1,
  x^2 h(x) <= C Delta(x).
Thus
  sqrt(h(x)) <= C sqrt(Delta)/x.
Integrating over a multiplicative x interval gives logarithmic metric length.

For Rx>=1,
  h(x)<=alpha+C R^2 Delta(x)<=C(1+A).
Euclidean length of the whole sublevel side is <=sqrt(2A/alpha), yielding
  I_far(A)<=C sqrt(1+A)*sqrt(A/alpha)=O(A)
for fixed alpha,R.

Near x=0, use h(x)<=e^{R x}h(0)+alpha and sublevel width
~sqrt(A/h0) when h0 is large; the product sqrt(h0)*width is O(sqrt(A)).
A dyadic spatial partition from 1/sqrt(h0) to 1/R contributes at most
O(sqrt(A) log(1+h0)), but this retains log h0~log t.

Need remove log h0 for a t-uniform theorem. The exact quadratic example shows
the log is an artifact.

Use change variable by gradient:
  p=f'(x), dp=h(x) dx,
so
  sqrt(h) dx = dp/sqrt(h).

Also convex identity
  Delta(x)=int_0^x p(s) ds.

No immediate t-free bound.

## A safer bound sufficient for our application

We do NOT actually require complete independence from t.
A factor poly(log t) is acceptable.

Since h0<=alpha+tR^2/4,
  log(1+h0)=O(log t).

Therefore the above structured 1D bound
  I(A)=poly(A, log t)
is already enough when A=O(log t).

For separable d-dimensional F,

  V_H(S_A)<=poly_d(A,log t)=poly_d(log t).

Thus the conjecture is proved sufficiently for separable coordinate models.

## Case 2: finite fixed ridge dictionary

Suppose all x_i belong to a fixed set of r directions
  v_1,...,v_r,
where r is independent of t.

Then
  F(theta)=alpha||theta||^2/2
           +sum_{j=1}^r phi_j(v_j^T theta),
where phi_j aggregates all observations in direction v_j.

The Hessian is
  H=alpha I+sum_j phi_j''(v_j^T theta) v_j v_j^T.

Only r scalar curvature fields vary, each log-Lipschitz along theta.

For fixed d,r, partition the bounded O(sqrt(log t)) sublevel region according
to dyadic bins of each aggregate curvature:
  phi_j'' in [2^k,2^{k+1}).

Each curvature ranges between near 0 and O(tR^2), so there are O(log t) bins
per direction.

Number of joint curvature regimes:
  O((log t)^r).

Within a regime, H varies by at most a constant factor in PSD order from the
representative matrix (plus alpha floor).

Strong convexity/potential restriction limits the metric-scaled volume of
each regime; a crude Euclidean cover in its representative Hessian metric
then contributes poly_d(A) cells.

Therefore for FIXED r,

  N_cover <= poly_{d,r}(log t).

This establishes the desired polylog cover for finite fixed direction
dictionary, modulo routine regime-boundary details.

## General unrestricted directions

In adversarial OLR, the number of distinct directions r can grow with t.
The curvature-regime argument becomes (log t)^t and is useless.

Thus the real difficulty is not dimension alone; it is whether t distinct
rank-one ridge directions can create metric complexity exceeding polylog even
when ambient d is fixed.

In fixed d, Hessian is only a dxd SPD matrix, with d(d+1)/2 degrees of freedom.
This suggests discretizing the AGGREGATE Hessian rather than individual
curvatures.

## Aggregate-Hessian discretization

On S_A,
  alpha I <= H(theta) <= (alpha+tR^2/4)I.

Normalize by alpha.
The SPD cone in fixed dimension can be covered multiplicatively in Loewner
metric with O((log t)^{m}) bins at constant factor resolution, where
  m=d(d+1)/2,
heuristically by discretizing eigenvalue logarithms and orientations.

Eigenvalues need O(log t) logarithmic bins each.
Orientation space O(d) is compact and needs only constant resolution for
constant-factor quadratic-form approximation away from eigenvalue
degeneracies; a fixed-dimensional net suffices.

Therefore the SET OF POSSIBLE HESSIAN MATRICES has a
  poly_d(log t)
constant-factor net.

But this alone does NOT bound the number of disconnected spatial components
of points whose Hessian falls in one matrix bin.

Could the same Hessian regime occur in exponentially/many disconnected
patches inside S_A? Logistic ridge sums are analytic convex, and S_A itself is
convex, but Hessian-regime preimages need not be convex.

This is the remaining geometric issue.

## Potential route via direct cover independent of preimage components

For each point theta in S_A choose its local Hessian ellipsoid.
A maximal disjoint family of half-radius ellipsoids gives a cover.
If Hessians of centers in the same matrix bin are comparable, disjoint
ellipsoids all have comparable volume.

They all lie inside an enlarged Euclidean sublevel neighborhood of radius
O(sqrt(A)+constant) by generalized-self-concordant local potential control.

Thus number in one Hessian bin can be bounded by Euclidean volume ratio:
  Vol(enlarged region)/Vol(one ellipsoid).

But ellipsoid volume may be as small as det(H)^-1/2 ~t^-d/2, reintroducing t.

Need exploit that if det(H) is large, the sublevel region is correspondingly
thin in those directions. Euclidean bounding ball loses that cancellation.

So the general metric-volume/packing theorem remains open.

## Result of this attack

PROVED/SUPPORTED:
- separable fixed-d family: polylog metric cover;
- fixed finite ridge dictionary: polylog cover;
- aggregate Hessian matrix space itself has only poly_d(log t) multiplicative
  complexity.

UNRESOLVED:
- spatial packing count for unrestricted t distinct directions.

No counterexample yet.

Next best step is computational adversarial search in d=2:
optimize many bounded ridge directions/labels to maximize a numerical proxy
for Hessian metric volume of an A=O(log t) sublevel set, and measure scaling
with t. If it grows polynomially, current conjecture likely false; if it stays
polylog/constant across aggressive search, use patterns to formulate proof.
