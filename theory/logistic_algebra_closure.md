# Logistic algebra closure: collinear directions

## Key change of variable

In d=1 let

  u = sigma(theta) in (0,1).

Then

  exp(theta) = u/(1-u).

For an integer multiplier k>=1,

  sigma(k theta)
  = exp(k theta)/(1+exp(k theta))
  = u^k / [u^k + (1-u)^k].

Therefore every sigmoid evaluated at an integer multiple of the SAME latent
projection is a rational function of the single scalar u.

Example:

  sigma(2 theta)
  = u^2/[u^2+(1-u)^2].

So the functions sigma(theta) and sigma(2theta) are NOT algebraically
independent generators.

## Consequence for the previous V=[1,2] ambiguity

The first score identity alone is underdetermined algebraically, but the actual
logistic posterior imposes nonlinear compatibility:

  p_1 = E[u],
  p_2 = E[ u^2/(u^2+(1-u)^2) ].

Thus arbitrary nullspace perturbations of (p_1,p_2) need not be realizable by a
single distribution of u.

This is why the previous score-nullity example must NOT be interpreted as a
realizability impossibility theorem.

## General collinear dictionary

Let all feature vectors lie on one ray:

  v_j = k_j v,

where k_j are positive integers. Define z=theta^T v and u=sigma(z). Then

  sigma(theta^T v_j)
  = sigma(k_j z)
  = R_{k_j}(u),

where

  R_k(u)=u^k/[u^k+(1-u)^k].

Hence the entire dictionary prediction vector is

  p_j=E[R_{k_j}(u)]

under one scalar push-forward posterior distribution.

The ambient nullity r-rank(V)=r-1 therefore overstates the true functional
degrees of freedom.

## But finite moment closure still does not follow

R_k(u) is rational, not generally a polynomial of bounded degree independent of
k. Exact expectations E[R_k(u)] are not determined by finitely many ordinary
moments E[u^m] in general.

Thus collinearity produces ALGEBRAIC REDUCTION but not automatically
FINITE-DIMENSIONAL EXPECTATION CLOSURE.

## Refined concepts

1. Linear Score Nullity:
   LSN(V)=r-rank(V).
   Measures ambiguity left by the first vector score equation only.

2. Functional Generator Dimension:
   FGD(F) = smallest number of latent scalar generators needed to represent all
   requested predictive functions algebraically/measurably.

   For integer collinear logistic directions, FGD=1 even though LSN=r-1.

3. Expectation Closure Complexity:
   ECC_epsilon(F,Q) = minimum number of expectations of basis functions needed
   to recover every required E[f], f in F, to error epsilon under posterior
   family Q.

The computationally relevant quantity is ECC, not LSN alone.

## Approximation route

Because each R_k is smooth on [0,1], approximate it uniformly by a polynomial

  P_{k,m}(u)=sum_{l=0}^m c_l u^l.

Then

  |E[R_k(u)]-E[P_{k,m}(u)]|
  <= ||R_k-P_{k,m}||_infinity.

Thus maintaining moments E[u^l], l<=m, can approximate predictions for an
entire collinear dictionary.

The crucial question becomes the degree m required as a function of:
- maximum multiplier k,
- desired predictive error epsilon,
- ultimately the regret horizon T.

If m=poly(log T,d) is sufficient for the accuracy needed by logarithmic regret,
this suggests a compact approximation architecture.

If m must grow polynomially in T or B, the route loses its computational
advantage.

## Immediate next theorem target

Bound the best polynomial approximation degree of

  R_k(u)=u^k/[u^k+(1-u)^k]

uniformly on [0,1].

The transition around u=1/2 sharpens with k. Its derivative at 1/2 is k.
This already implies increasing approximation difficulty as k grows.

We should derive upper/lower degree bounds in k and epsilon before building any
new predictor.
