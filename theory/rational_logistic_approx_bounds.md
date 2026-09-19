# Polynomial approximation bounds for the logistic multiplier map

Define

  R_k(u) = u^k / [u^k + (1-u)^k],   u in [0,1], k>=1.

This is exactly sigma(k z) after the change of variable u=sigma(z).

We ask for the minimum polynomial degree m needed for uniform approximation
error epsilon.

## Basic structure

R_k(1-u)=1-R_k(u), R_k(1/2)=1/2, and

  R_k'(1/2)=k.

The transition layer around 1/2 has width Theta(1/k).

## A rigorous degree lower bound from Markov

Let P be a real polynomial of degree m such that

  ||P-R_k||_infinity <= epsilon

on [0,1], with epsilon<1/4.

Choose

  delta = 1/(2k).

Using the logit representation

  R_k(u)=sigma(k log(u/(1-u))),

at u_+=1/2+delta and u_-=1/2-delta, the logit separation is constant order
for k sufficiently large. More directly, for delta=c/k with fixed c, the
difference R_k(u_+)-R_k(u_-) tends to tanh(2c), a positive constant.

Hence for a fixed c and epsilon smaller than one quarter of that separation,

  |P(u_+)-P(u_-)| >= C_epsilon > 0.

By the mean value theorem there exists xi between u_- and u_+ with

  |P'(xi)| >= C_epsilon/(2delta) = Omega(k).

Markov's inequality on [0,1] gives

  ||P'||_infinity <= 2 m^2 ||P||_infinity.

Since ||P||_infinity <= 1+epsilon,

  m = Omega(sqrt(k)).

Therefore constant-error uniform polynomial approximation cannot have degree
independent of the multiplier k.

This lower bound is rigorous at scaling level; constants can be written
explicitly by fixing c (e.g. c=1/4) and k sufficiently large.

## Stronger approximation-theory heuristic

R_k is rational with complex singularities determined by

  u^k + (1-u)^k = 0.

Equivalently

  u/(1-u) = exp(i(2j+1)pi/k).

The nearest poles approach u=1/2 at imaginary distance Theta(1/k).

For analytic functions, Chebyshev approximation error is controlled by the
nearest complex singularity. A singularity distance Theta(1/k) suggests an
upper/lower exponential approximation scale roughly

  error ~ exp(-Theta(m/k)),

and therefore

  m = Theta(k log(1/epsilon))

may be the correct sharp regime.

This statement is currently a CONJECTURED sharp scaling, not yet a proved
theorem in this repository. It should be proved using Bernstein ellipses and
a converse lower bound before being used in a paper.

## Consequence for moment closure

Even the rigorous lower bound

  m=Omega(sqrt(k))

shows that exact collinear algebra does not give a fixed-order moment closure
uniformly over arbitrarily large multipliers.

If the feature-norm assumptions bound all effective multipliers independently
of T, this does not kill the route.

If an adversarial problem formulation permits effective k growing with T, the
moment-state dimension must grow at least Omega(sqrt(k)) for constant uniform
accuracy in this polynomial-basis architecture.

## Important limitation

This is a lower bound for UNIFORM POLYNOMIAL APPROXIMATION of R_k. It is NOT:
- a lower bound for every online logistic-regression algorithm;
- a lower bound for arbitrary rational/other approximation schemes;
- a regret lower bound;
- proof that ECC itself is Omega(sqrt(k)) under every possible basis.

Those stronger statements require separate arguments.

## Paper gate

Do not write the main breakthrough paper yet.

Write when at least one of these is complete:

A. Algorithm route:
   - explicit implementable predictor;
   - rigorous regret <= O(poly(d) log T) under the target Google assumptions;
   - polynomial/practical per-round complexity;
   - theorem demonstrably beyond known AIOLI/EW results;
   - adversarial experiments and prior-art search passed.

B. Obstruction route:
   - precisely defined nontrivial algorithm/compression class;
   - rigorous lower bound applying to that class;
   - construction realizable by online logistic data;
   - demonstrated relevance to the computational gap;
   - prior-art search establishes novelty.

A short theory note/preprint can be drafted earlier only after the sharp
R_k approximation theorem and its relevance to a meaningful posterior-
compression class are both proved.
