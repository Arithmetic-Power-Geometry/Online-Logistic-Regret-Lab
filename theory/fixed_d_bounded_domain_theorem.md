# Fixed-d bounded-domain log-cosh moment theorem

## Setting

Parameter domain:
  Theta = {theta in R^d : ||theta||_2 <= B}.

Features satisfy
  ||x_t||_2 <= R.

Binary labels y_t in {+-1}. Let the reference Bayesian/EW posterior use a
prior density pi(theta) supported on Theta and bounded/regular enough for the
chosen deterministic integration scheme.

Logistic loss:
  g_y(z)=log(1+exp(-y z))
        = log 2 - y z/2 + h(z),
  h(z)=log cosh(z/2).

For every theta in Theta,
  |theta^T x_t| <= L := BR.

## Polynomial surrogate

Let P_m be an even polynomial satisfying
  sup_{|z|<=L} |h(z)-P_m(z)| <= eta_m.

Write
  P_m(z)=sum_{j=1}^m c_{2j} z^{2j} + c_0.

After n=t-1 observations, exact historical potential (up to prior term) is

  F_t(theta)
   = n log 2 -(1/2) theta^T b_t
     + sum_{i<t} h(theta^T x_i),

where
  b_t=sum_{i<t} y_i x_i.

Surrogate potential:

  Fhat_t(theta)
   = n(log2+c_0) -(1/2)theta^T b_t
     + sum_{j=1}^m c_{2j}
         <theta^{tensor 2j}, S_{2j,t}>,

with
  S_{2j,t}=sum_{i<t} x_i^{tensor 2j}.

The theta-independent n c_0 may be dropped.

## Exact update closure

State:
  C_t=(n,b_t,S_2,t,...,S_2m,t).

Updates are additive:
  b_{t+1}=b_t+y_t x_t,
  S_{2j,t+1}=S_{2j,t}+x_t^{tensor 2j}.

Thus no historical examples need be stored.

## Potential and density-ratio error

Uniformly over Theta,

  |F_t(theta)-Fhat_t(theta)| <= n eta_m.

Hence the oscillation of the potential difference is at most

  osc(Fhat_t-F_t) <= 2 n eta_m.

Normalized posterior density-ratio oscillation is identical, since
normalization adds only a constant.

Therefore if
  eta_m <= c/(2 t^2),
then at round t
  osc(Qhat_t,Q_t) <= c/t.

For every nonnegative current likelihood L_t,

  |log E_Qhat_t L_t - log E_Qt L_t| <= c/t.

Summing:
  L_T(Qhat)-L_T(Q)
   <= c(1+log T).

This is a valid approximation-tax theorem relative to the bounded-domain
reference EW predictor, provided predictions under Qhat_t are evaluated to
sufficient additional numerical accuracy.

## Polynomial degree

h(z)=log cosh(z/2) is analytic in the strip |Im z|<pi, with nearest
singularities at +-i pi.

Standard Chebyshev/Bernstein approximation on [-L,L] therefore gives
geometric convergence. For fixed L (or with explicit L dependence),
achieving eta_m=O(t^-2) requires

  m = O(L log t)

up to constants/prefactors that must be made explicit in a final proof.

For fixed B,R:
  m=O(log t).

## State dimension

A symmetric order-k tensor in d dimensions has
  N(d,k)=binom(d+k-1,k)
independent entries.

State size is
  d + sum_{j=1}^m binom(d+2j-1,2j).

For FIXED d,
  binom(d+2m-1,2m)=Theta(m^{d-1}),
so the cumulative even-tensor state is polynomial in m, hence

  state size = O(poly_d(log t)).

The polynomial exponent depends on d. This is NOT poly(d,log t) uniformly in d.

## Update cost

If symmetric monomials are explicitly enumerated, one update computes all
monomials x_t^alpha through total degree 2m. For fixed d this is likewise
poly_d(m)=poly_d(log t).

Thus representation and update are poly(log t) for fixed d,B,R.

## Prediction/integration issue

The surrogate posterior density is

  qhat_t(theta) proportional to
  pi(theta) exp(-Fhat_t(theta)) 1[theta in Theta].

Prediction requires the ratio of d-dimensional integrals

  int_Theta sigma(theta^T x_t) pi(theta)e^{-Fhat_t(theta)} dtheta
  ----------------------------------------------------------------
  int_Theta pi(theta)e^{-Fhat_t(theta)} dtheta.

The compact moment state alone does NOT evaluate these integrals.

For fixed d on a compact domain, deterministic cubature/quadrature may be used.
To claim poly(log t) total prediction time, one needs a theorem giving
sufficiently accurate integration with node count polynomial in log t for this
analytic family, with constants controlled uniformly over the evolving
surrogate potential.

This uniform quadrature statement is NOT yet proved here.

## Theorem status

PROVED / elementary conditional components:
- exact log-cosh decomposition;
- additive finite moment state for polynomial surrogate;
- potential-error -> density-ratio oscillation;
- oscillation c/t -> O(log T) cumulative approximation tax;
- fixed-d state/update dimension poly(log T), conditional on degree
  m=O(log T).

REMAINING proof obligations:
1. explicit Chebyshev error constants for h on [-BR,BR];
2. choose/reference a bounded-domain EW prior with a known regret guarantee
   versus ||theta||<=B, or prove the reference regret directly;
3. uniform deterministic integration complexity for qhat_t prediction;
4. finite precision/bit complexity.

Therefore this is currently a FIXED-d REPRESENTATION THEOREM SKELETON, not yet
a complete efficient online algorithm theorem.

## Relation to main open problem

McMahan--Streeter ask for O(poly(D) log T) regret without the exponential
diameter dependence. Later improper algorithms and EW analyses address major
parts/variants of that regret question. The current contribution target is
computational: whether a near-optimal EW-style predictor can be represented
and evaluated with polylogarithmic horizon dependence.

No novelty claim is made until a broader prior-art audit and the remaining
integration/reference-regret gaps are closed.
