# Update-closed log-cosh tensor compression

## Exact decomposition

For logistic loss g_y(z)=log(1+exp(-y z)), y in {-1,+1},

  g_y(z) = log 2 - y z/2 + h(z),
  h(z)=log cosh(z/2).

Therefore after n=t-1 observations,

  F_t(theta)
    = ||theta||^2/(2 s^2)
      + n log 2
      - (1/2) theta^T b_t
      + sum_{s<t} h(theta^T x_s),

where

  b_t = sum_{s<t} y_s x_s.

Labels affect the historical potential only through the d-vector b_t.
The nonlinear term is label-free and h is even.

## Polynomial surrogate

On |z|<=L=BR, approximate

  h(z) ~= P_m(z)=sum_{j=1}^m c_{2j} z^{2j}.

Then

  sum_s P_m(theta^T x_s)
   = sum_{j=1}^m c_{2j}
       < theta^{tensor 2j}, S_{2j,t} >,

with

  S_{2j,t}=sum_{s<t} x_s^{tensor 2j}.

Hence the surrogate posterior potential is completely determined by

  C_t = (n, b_t, S_2,t, S_4,t, ..., S_2m,t).

Crucially this state is EXACTLY UPDATE-CLOSED for the polynomial surrogate:

  b_{t+1}=b_t+y_t x_t,
  S_{2j,t+1}=S_{2j,t}+x_t^{tensor 2j}.

This avoids the posterior-moment update hierarchy.

## Approximation-to-posterior bound

Suppose |h(z)-P_m(z)| <= eta on [-L,L]. On comparator ball
||theta||<=B, ||x_s||<=R,

  |F_t(theta)-Fhat_t(theta)| <= n eta =: delta.

Thus the exact and surrogate unnormalized densities differ pointwise by factors
in [exp(-delta),exp(delta)]. After normalization, their density ratio lies in
[exp(-2delta),exp(2delta)].

For any f in [0,1], including f(theta)=sigma(theta^T x_t),

  |E_Q f-E_Qhat f| <= exp(2delta)-1.

A sharper TV constant may improve this, but this elementary bound is enough for
a first complexity calculation.

To target predictive error epsilon_t, it suffices conservatively to choose

  delta_t = O(epsilon_t),
  eta_t = O(epsilon_t/t).

For epsilon_t=Theta(t^-2), per-factor uniform approximation eta_t=Theta(t^-3).

## Degree from complex singularities

h(z)=log cosh(z/2) has nearest complex singularities where cosh(z/2)=0:

  z = i pi (2k+1).

On [-L,L], scaling z=L x puts nearest singularities at x=+- i pi/L.
Chebyshev approximation therefore has geometric rate

  error ~ exp(-Theta(m/L))

up to prefactors/logarithmic details.

To reach eta_t=Theta(t^-3), expected sufficient degree is

  m = O(L log t)

for fixed L=BR.

This is logarithmic in T, not polynomial in T.

## State dimension

A symmetric order-k tensor in d variables has

  N(d,k)=binom(d+k-1,k)

independent entries.

The even tensors through order 2m require

  sum_{j=1}^m binom(d+2j-1,2j)

entries.

For fixed d and m=O(log T), this is poly(log T) with exponent depending on d.
For variable d it is not poly(d,log T); the highest-order term behaves like
binom(d+2m-1,2m).

Therefore:

- update closure is solved for the polynomial surrogate;
- T-dependence of approximation degree is only logarithmic;
- the remaining obstruction is HIGH-ORDER SYMMETRIC TENSOR DIMENSION.

## New precise frontier

Can the contractions needed for predictive inference under this surrogate be
maintained/sketched without explicitly storing all S_{2j}, with state and
per-round time poly(d,m), where m=O(BR log T)?

This is now the positive algorithmic target.

Possible routes:
1. tensor sketches preserving contractions theta^{tensor k}:S_k;
2. random features for the even ridge-function sum;
3. query-adaptive sketches sufficient only for E[sigma(theta^T x_t)];
4. low-rank structure if the empirical feature covariance/effective rank is
   small (not enough for worst-case theorem unless explicitly parameterized).

## Paper gate

This decomposition/update-closure theorem is useful but does not solve the
Google frontier by itself.

Write the main paper only if:
- a sketch reduces the tensor state to poly(d,BR,log T) while preserving the
  predictive error schedule; or
- a rigorous lower bound shows such sketching is impossible for a meaningful
  representation class, creating a new complexity barrier.
