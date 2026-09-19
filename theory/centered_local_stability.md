# Centered local posterior stability lemma

Let Q and Qhat have densities on parameter space proportional to exp(-F) and
exp(-Fhat), respectively. Let

  D(theta)=Fhat(theta)-F(theta).

Fix a measurable K and reference theta0 in K. Assume

  sup_{theta in K} |D(theta)-D(theta0)| <= delta.

Because adding a constant to a potential does not change its normalized
distribution, replace Fhat by Fhat-D(theta0). Then on K,

  |D(theta)| <= delta.

## Conditional stability on K

Let Q_K and Qhat_K be the distributions conditioned on K. Their density ratio
on K is

  dQhat_K/dQ_K
    = exp(-D(theta)) / E_{Q_K}[exp(-D)].

Since exp(-D) lies in [exp(-delta),exp(delta)],

  exp(-2delta) <= dQhat_K/dQ_K <= exp(2delta).

Hence for any f in [0,1],

  |E_{Q_K}f-E_{Qhat_K}f|
    <= exp(2delta)-1.

A sharper total-variation calculation can replace this constant, but the
linear small-delta scaling is enough.

## Adding tail mass

If

  Q(K^c) <= tau
and
  Qhat(K^c) <= tauhat,

then for f in [0,1],

  |E_Q f-E_Qhat f|
  <= |E_{Q_K}f-E_{Qhat_K}f| + 2 tau + 2 tauhat

under a simple decomposition (constants can be sharpened).

Therefore

  |E_Q f-E_Qhat f|
  <= exp(2delta)-1 + 2(tau+tauhat).

For logistic prediction f(theta)=sigma(theta^T x_t), a sufficient schedule is

  delta_t = O(t^-2),
  tau_t+tauhat_t = O(t^-2).

## Why this matters

The approximation target is now invariant to arbitrary theta-independent
errors in the historical potential. A sketch only needs to preserve potential
variation over a high-posterior-mass region.

This is strictly weaker than requiring
  sup_theta |Fhat(theta)-F(theta)|=O(t^-2).

## Remaining hard step

Construct K_t and theta0 online, prove tail control without assuming favorable
data curvature, and show a polynomial-kernel/tensor sketch preserves centered
potential variation on K_t with poly(d,B,log T) state.

This lemma is a bridge, not yet the algorithmic breakthrough.
