# Tensor-sketch error budget for online logistic EW

## Prior art boundary

TensorSketch / polynomial-kernel sketches already avoid explicit d^k tensor
formation. High-degree polynomial-kernel sketching with target dimension
polynomial in the degree is established prior art. Therefore the novelty target
cannot be "sketch x^{tensor k}".

Our question is stricter and sequential:

Can sketches of the accumulated tensors
  S_k,t = sum_{s<t} x_s^{tensor k}
preserve the posterior potential accurately enough for online EW prediction
with an error schedule that yields only O(log T) additional regret?

## Quantity to estimate

For a candidate theta,

  A_k,t(theta)
    = <theta^{tensor k}, S_k,t>
    = sum_{s<t} (theta^T x_s)^k.

If Phi_k is a linear sketch of tensor features, maintain

  s_k,t = sum_{s<t} Phi_k(x_s).

A natural estimator is

  Ahat_k,t(theta) = <Phi_k(theta), s_k,t>.

This is exactly the polynomial-kernel-sum query.

## Why ordinary constant-relative-error kernel approximation is not enough

The surrogate potential is

  Fhat_t(theta)
   = prior + linear term + sum_j c_{2j} A_{2j,t}(theta).

Suppose each A_{2j,t} is estimated with additive error E_{j,t}(theta).
Then potential error is bounded by

  |Delta F_t(theta)| <= sum_j |c_{2j}| |E_{j,t}(theta)|.

Our conservative posterior-to-prediction bridge needs total potential error
roughly O(t^-2) if we want O(t^-2) predictive error directly from a uniform
density-ratio argument.

But A_k,t itself can be Theta(t L^k), L=BR. A constant relative error gives
Theta(t) potential error, catastrophically too large.

Even an estimator with standard deviation proportional to
  ||theta^{tensor k}|| ||S_k,t||_F / sqrt(D)
can have worst-case scale Theta(t L^k / sqrt(D)).
For absolute error O(t^-2), this crude worst-case calculation would require

  D = Omega(t^6 L^{2k}),

which destroys the desired poly(log T) complexity.

This is NOT a lower bound on TensorSketch or all sketches. It shows that a
naive worst-case additive-error analysis cannot close our theorem.

## Key cancellation opportunity

We do not actually need absolute approximation of the full historical
potential. Posterior predictions are invariant to theta-independent additive
constants.

Therefore define centered potential error

  Delta_t(theta) - Delta_t(theta_ref).

If sketch error is highly correlated across theta, or if we preserve potential
DIFFERENCES on the posterior-relevant region, the required dimension can be
much smaller than the crude t^6 calculation.

This suggests the correct object is not a kernel-value sketch but a
CENTERED LOCAL POTENTIAL SKETCH.

## Candidate: centered local tensor sketch (CLTS)

Choose a reference theta_bar_t (e.g. current posterior mode/center). For each
even degree k maintain a sketch permitting estimates of

  A_k,t(theta)-A_k,t(theta_bar_t).

Using
  a^k-b^k=(a-b) sum_{r=0}^{k-1} a^{k-1-r} b^r,

the difference contains a factor
  (theta-theta_bar_t)^T x_s.

Inside a shrinking posterior credible region this can be substantially smaller
than A_k,t(theta) itself.

The hoped-for mechanism is:
- history sum grows like t;
- posterior radius shrinks like t^{-1/2} in well-curved directions;
- centering converts absolute error into local variation error;
- local variation, not global potential level, controls the normalized
  posterior and prediction.

## Critical caveat

Adversarial online logistic regression need not have uniform strong curvature
in every direction. Separability can drive modes toward the boundary and
posterior contraction can be anisotropic. Thus a t^{-1/2} radius cannot be
assumed globally.

Any theorem must express the local radius through actual posterior/regularized
curvature and separately handle weak-curvature directions.

## Next theorem target

Prove a prediction-stability lemma of the form:

If on a posterior-relevant set K_t,

  sup_{theta in K_t}
  |Delta F_t(theta)-Delta F_t(theta_bar_t)| <= delta_t

and Q_t(K_t^c) <= tau_t,

then for f in [0,1],

  |E_Qt f-E_Qhat_t f| <= C delta_t + C' tau_t.

This replaces global potential approximation by centered local approximation.

Then ask whether high-degree polynomial sketches can achieve
  delta_t,tau_t = O(t^-2)
with dimension poly(d,B,log T).

## Status

- explicit tensor dimension bottleneck: bypassable by known sketching prior art;
- naive global TensorSketch error budget: insufficient;
- centered local potential sketch: new active route, novelty NOT established;
- no Google-problem solution yet.
