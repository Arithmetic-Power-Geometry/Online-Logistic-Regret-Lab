# Exact pole geometry and a rigorous Chebyshev upper bound

Let

  R_k(u)=u^k/[u^k+(1-u)^k],  u in [0,1].

Map [0,1] to [-1,1] by x=2u-1 and define

  F_k(x)=R_k((x+1)/2).

## Exact poles

Poles satisfy

  u^k+(1-u)^k=0,

hence

  u/(1-u)=exp(i(2j+1)pi/k).

For the nearest pair j=0,-1, write phi=pi/k. Then

  u_+ = exp(i phi)/(1+exp(i phi))
      = 1/2 + (i/2) tan(phi/2),

and its conjugate u_-.

Therefore in x coordinates,

  x_+ = i tan(pi/(2k)),
  x_- = -i tan(pi/(2k)).

These are the nearest singularities to [-1,1].

## Exact limiting Bernstein parameter

For a purely imaginary point x=i a, a>0, the Bernstein ellipse through x has

  rho = a + sqrt(1+a^2)
      = exp(asinh(a)).

Thus the largest open Bernstein ellipse free of the nearest poles has parameter

  rho_*(k)
  = exp(asinh(tan(pi/(2k)))),

so

  log rho_*(k)
  = asinh(tan(pi/(2k)))
  = pi/(2k) + O(k^{-3}).

Hence the analytic continuation radius shrinks at exact rate Theta(1/k).

## Rigorous upper-bound route

Fix any constant gamma in (0,1), and choose

  log rho = gamma log rho_*(k).

Then F_k is analytic on and inside E_rho. Standard Chebyshev/Bernstein theory
gives a degree-m polynomial P_m with

  ||F_k-P_m||_infinity
  <= [2 M_{k,gamma}/(rho-1)] rho^{-m},

where M_{k,gamma}=max_{z in E_rho}|F_k(z)|.

Because the chosen ellipse stays a fixed fractional conformal distance away
from the nearest simple poles, M_{k,gamma} grows at most polynomially in k
(a direct explicit bound should be supplied in the final proof).

Since

  rho-1 = Theta(1/k),
  log rho = Theta(1/k),

this yields the safe scaling

  m = O(k[log k + log(1/epsilon)])

provided the explicit polynomial bound on M_{k,gamma} is completed.

This is already enough to show that polynomial moment closure is possible with
degree polynomial in k and logarithmic in target accuracy.

## Expected sharp asymptotic

For each fixed k, classical converse results for polynomial approximation say
that geometric convergence faster than rho_*^{-m} would imply analytic
continuation beyond the nearest pole, impossible here. Simple-pole Chebyshev
asymptotics also suggest

  E_m(F_k) = exp[-Theta(m/k)]

up to k-dependent prefactors.

However, to state the UNIFORM two-parameter theorem

  m = Theta(k log(1/epsilon))

without qualifications, we still need control of those prefactors uniformly in
k and epsilon. We therefore do NOT claim this sharp two-sided theorem yet.

## Combined with the Markov lower bound

Already proved in the repository for fixed constant error:

  m = Omega(sqrt(k)).

Pole geometry strongly suggests the stronger Omega(k log(1/epsilon)) regime,
but the repository currently has:

  rigorous lower: Omega(sqrt(k)) for fixed small error;
  near-rigorous upper target:
      O(k[log k + log(1/epsilon)]),
      pending an explicit M_{k,gamma} bound;
  sharp conjecture:
      Theta(k log(1/epsilon)) in the appropriate joint regime.

## Consequence for the Google-problem route

This result does NOT solve online logistic regression. It says the collinear
logistic prediction family is polynomially approximable, so this branch is not
killed by an exponential closure explosion.

The next algorithmic question is whether effective multipliers k can be bounded
by poly(d,B) under the target feature/comparator assumptions, and whether the
required moments can themselves be updated/approximated online in polynomial
time with cumulative prediction error O(log T).

## Paper gate

Do NOT write the main paper yet.

Start the paper when either:

1. the approximation theorem is completed AND translated into a nontrivial
   posterior-compression/regret theorem; or

2. an explicit score/moment predictor achieves a proved regret improvement over
   the known practical O(B log(BT)) frontier with polynomial per-round cost.

The exact pole theorem alone is a lemma/section, not yet a paper-level solution.
