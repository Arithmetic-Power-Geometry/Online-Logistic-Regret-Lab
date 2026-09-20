# Cumulative density-ratio oscillation theorem

We compare exact Bayesian/EW evolution P_t with a compressed evolution Q_t.

At each round t:
1. both see the same likelihood L_t(theta) in (0,1);
2. exact Bayes update maps P_t -> P_t^+;
3. approximate Bayes update maps Q_t -> Q_t^+;
4. compression maps Q_t^+ -> Q_{t+1}.

Let P_{t+1}=P_t^+ for the exact process.

Define the log density-ratio
  r_t(theta)=log(dQ_t/dP_t)(theta)
when mutually absolutely continuous, and its oscillation
  omega_t = sup r_t - inf r_t.

## Lemma 1: common Bayes update preserves oscillation exactly

After multiplying both measures by L_t and renormalizing,

  log(dQ_t^+/dP_t^+)
   = r_t(theta) + constant_t.

Hence
  osc(Q_t^+,P_t^+) = omega_t.

## Lemma 2: compression adds oscillation subadditively

Suppose compression satisfies
  osc(Q_{t+1},Q_t^+) <= rho_t.

Then
  log(dQ_{t+1}/dP_{t+1})
   = log(dQ_{t+1}/dQ_t^+)
     + log(dQ_t^+/dP_t^+).

Therefore
  omega_{t+1} <= omega_t + rho_t.

If Q_1=P_1,
  omega_t <= sum_{s<t} rho_s.

## Lemma 3: oscillation controls evidence ratio with HALF the oscillation

Let Q and P be probability measures and
  r=log(dQ/dP), osc(r)<=omega.

Because E_P[e^r]=1, r must straddle 0 in the normalization sense, but this
alone does not imply |r|<=omega/2.

For any nonnegative likelihood L,

  E_Q L / E_P L
   = E_P[L e^r]/E_P[L].

This weighted average of e^r lies between e^{inf r} and e^{sup r}.
Thus
  log(E_Q L/E_P L) lies in [inf r,sup r].

The absolute value is bounded by max(|inf r|,|sup r|), which can be as large
as omega, not universally omega/2.

Safe bound:
  |log E_Q L - log E_P L| <= omega.

So per-round prediction difference at round t is <= omega_t.

## Naive per-round summation is BAD

Summing per-round bounds gives
  sum_t omega_t
  <= sum_t sum_{s<t} rho_s
  = sum_s (T-s) rho_s,

which reintroduces a horizon multiplier.

Therefore the previous conjecture
  total regret tax <= C sum_t rho_t
does NOT follow from update invariance alone.

This is the crucial accounting correction.

## Path-evidence analysis with interleaved compression

Exact cumulative loss:
  L_T(P)=-sum_t log E_{P_t} L_t
        =-log E_{P_1}[prod_t L_t].

Approximate cumulative loss uses a different measure after every compression,
so it does not reduce to one final expectation under Q_1.

A compression at time s can affect every future predictive evidence. Without
additional structure, its distortion can persist and be charged repeatedly.

## Counterexample intuition

If a compression changes odds between two latent hypotheses by factor e^rho,
and future likelihoods repeatedly probe the same distinction without washing
it out, each subsequent prediction can remain shifted. Bayes update preserves
the density-ratio oscillation exactly, so there is no automatic contraction.

Thus O(1/t) recompression oscillation is NOT sufficient by this argument for
O(log T) cumulative tax; a persistent error introduced early can cost O(T).

## What would suffice?

A schedule controlling current accumulated oscillation:
  omega_t = O(1/t)
would give
  sum_t omega_t=O(log T).

But since
  omega_t <= sum_{s<t} rho_s
with nonnegative worst-case accumulation, this requires either:
1. rho_s so small that cumulative oscillation decays -- impossible without
   corrective compression;
2. compression sometimes REDUCES prior distortion relative to exact P_t;
3. a contraction property in a weaker task-specific metric;
4. periodic reset/reconstruction against an exact or certified reference.

## Decision

The attractive claim that update-invariant oscillation converts per-compression
O(1/t) error directly into O(log T) regret is FALSE.

Density-ratio oscillation is update-stable but not self-healing.

This closes the naive sequential-recompression route.

Next target should be corrective projection:
Can compression at time t approximate the CURRENT exact posterior directly
with omega_t=O(1/t), using an update-closed summary, rather than merely
approximating Q_t^+ relative to the already-approximate state?

That returns the burden to a certified summary of the full history, but the
required current error O(1/t) is weaker than the earlier O(1/t^2) probability
target only if log-evidence oscillation maps favorably.

Status:
- Bayes invariance of oscillation: PROVED.
- subadditive compression accumulation: PROVED.
- total tax O(sum rho_t): DISPROVED as a generic consequence.
- naive recompression breakthrough route: CLOSED.
