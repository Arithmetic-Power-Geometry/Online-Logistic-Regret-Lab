# Theory and falsification ledger

## 1. Exact problem

Assume ||x_t||_2 <= 1 and comparator ||theta||_2 <= B.
Predictions may be improper probabilities p_t rather than sigma(<theta_t,x_t>).

Target:
  R_T <= C d log(1+BT) + lower-order terms
with per-round computation near O(d^2), ideally horizon-free.

## 2. Exact exponential-weights benchmark

For any prior pi over theta, define
  W_t = integral exp(-L_t(theta)) pi(dtheta),
where L_t is cumulative logistic loss.

Because binary log loss is mixable, the Bayesian / exponential-weights
predictive distribution has cumulative loss exactly -log W_T.

A local-prior-volume argument yields logarithmic regret for suitable Gaussian
priors. This benchmark is statistically strong but exact integration is the
computational bottleneck.

## 3. Candidate theorem skeleton

Let q_t=N(m_t,H_t^{-1}) approximate the exact posterior.
Let
  p_t^G = E_{q_t}[sigma(theta^T x_t)].
Let p_t^* be the exact EW posterior predictive.

Then
  -log p_t^G(y_t)
  = -log p_t^*(y_t) + Delta_t.

If one can prove a one-step inequality of the form
  Delta_t <= C * min{1, lambda_t^2}
where
  lambda_t = x_t^T H_t^{-1} x_t
or a related posterior leverage, then

  sum_t Delta_t

may telescope / be controlled by a log-det potential because rank-one curvature
updates satisfy standard determinant identities.

This would convert approximation error into a geometric information budget.

## 4. Candidate principle

**Curvature-Budgeted Aggregation Principle (CBAP), conjectural.**

For online generalized-linear log loss with bounded third derivative relative
to local curvature, a Gaussian aggregation predictor whose covariance follows
observed information may incur cumulative approximation tax controlled by a
log-determinant curvature budget rather than linearly in T.

For logistic regression, the hoped-for form is

  sum_t Delta_t <= poly(d) log det(I + c sum_t x_t x_t^T)

under explicit regularity / damping conditions.

If true with constants independent of exp(B), combining with exact EW regret
would yield a near-optimal logarithmic regret algorithm with O(d^2) rank-one
updates.

THIS IS A CONJECTURE, NOT A RESULT.

## 5. Main attack surfaces

A. Separable one-sided sequence:
   y_t x_t points repeatedly in one direction; posterior becomes skewed/truncated.

B. Abrupt reversal:
   long run of one label, then opposite labels.

C. Delayed coordinate:
   posterior becomes extremely certain in one subspace before a new orthogonal
   direction appears.

D. Rotating directions:
   adversary repeatedly activates low-curvature directions.

E. Boundary comparator:
   best comparator has ||theta|| close to B.

F. Tiny predictive probabilities:
   small absolute probability error can cause large log-loss error.

## 6. Stop conditions

Breakthrough:
- prove CBAP or another strictly stronger theorem than existing efficient bounds,
  and validate computationally.

Counterexample:
- find a family where Gaussian approximation tax grows faster than logarithmic;
  then formulate the obstruction theorem instead.

No paper until one of these is established.


## 7. Direct approximation-tax falsification

Comparator regret alone cannot validate CBAP, because it mixes statistical
regret with posterior-approximation error. We therefore compare the Gaussian
candidate directly against an exact 1D Bayesian/exponential-weights predictor.

For a sequence s=(x_t,y_t), define

  Tax_T(s) = sum_t [
      ell_log(p_t^G, y_t) - ell_log(p_t^*, y_t)
  ].

CBAP requires this tax to admit a logarithmic information-budget control.
A single large finite-T value is not by itself a disproof. The relevant signal
is a sequence family s_T for which Tax_T grows asymptotically faster than every
candidate logarithmic curvature budget while all stated assumptions remain true.

The automated search records, for increasing T:
- cumulative Gaussian-vs-exact tax,
- Tax_T / log(1+T),
- cumulative squared leverage proxy,
- worst one-step approximation tax,
- separable, reversal, and alternating adversaries.

If Tax_T/log(1+T) grows systematically, the naive CBAP formulation is rejected
and the next target is an explicit counterexample theorem.


## 8. Counterexample found: curvature-only Gaussian compression fails

The CI scaling experiment falsifies the naive CBAP for the current
GaussianLaplacePredictor.

Take d=1, x_t=1, y_t=+1 for every t, with the same Gaussian prior used by the
exact-grid Bayesian benchmark.

Observed cumulative approximation tax:
- T=32:   Tax_T ~= 9.30
- T=64:   Tax_T ~= 15.24
- T=128:  Tax_T ~= 24.36
- T=256:  Tax_T ~= 38.40
- T=512:  Tax_T ~= 60.17
- T=1024: Tax_T ~= 94.10

Meanwhile the candidate cumulative squared-leverage proxy remains bounded near
5.5. Therefore no inequality of the proposed form

  Tax_T <= C * sum_t min{1, lambda_t^2}

can hold uniformly for this algorithm with a universal constant C.

Moreover Tax_T/log(1+T) grows from about 2.66 at T=32 to about 13.57 at T=1024,
which is strong empirical evidence against an O(log T) approximation tax.

### Mechanism

Under a one-sided separable stream, the exact EW posterior becomes strongly
asymmetric and keeps substantial one-sided tail geometry relevant to prediction.
The compact Gaussian update retains only a center and curvature matrix. Its
local variance shrinks, so a curvature-only budget declares the state
"increasingly resolved", yet its predictive tail bias persists. Thus local
curvature can decrease while cumulative log-loss distortion continues to grow.

### Candidate obstruction principle

**Tail-Skew / Curvature Decoupling (TSCD), conjectural theorem form.**

For adversarial online logistic prediction, any posterior-compression rule whose
prediction is determined solely by a Gaussian state (mean plus local covariance)
updated by local gradient/curvature information need not admit a cumulative
approximation-error bound controlled only by a logarithmic determinant or
summable leverage budget. In separable regimes, posterior skew/tail geometry can
remain decision-relevant after local curvature has become small.

This is not yet a theorem for all Gaussian-state algorithms. What is proved by
the executable counterexample is only failure of the specific current update
and failure of the proposed universal leverage inequality for it.

### Next theorem target

Do not patch the same Gaussian rule blindly. The next target is either:
1. prove TSCD for a well-defined broad class of local Gaussian-state updates; or
2. add an explicit skew/tail state variable and test whether the missing
   information can be summarized compactly enough to recover logarithmic tax.


## 9. One-skew-state repair also fails asymptotically

The skew-corrected prototype substantially reduces the separable all-positive
tax, but does not restore O(log T) behavior:

- T=32:   skew Tax/log(1+T) ~= 2.30
- T=64:   ~= 2.95
- T=128:  ~= 3.71
- T=256:  ~= 4.56
- T=512:  ~= 5.54
- T=1024: ~= 7.33

Thus one extra scalar asymmetry memory is insufficient for the tested family.

This suggests a stronger hypothesis:

**Finite-Moment Compression Obstruction (FMCO), conjectural.**
For separable online logistic prediction, no fixed-order local moment summary of
a Gaussian approximation is guaranteed to preserve the exact EW predictive
distribution with O(log T) cumulative approximation tax uniformly in T.

The next experiment tests orders K in {1,2,3,4,6,8}. This does not prove FMCO:
failure of a particular update family is only evidence. A theorem would require
a clearly defined class of admissible finite-moment compression algorithms and
an adversarial indistinguishability or approximation lower bound.


## 10. Narrowed theorem target: Local Gaussian State Obstruction (LGSO)

The finite-moment experiments are useful diagnostically but are too broad and
algorithm-dependent for a theorem. We therefore narrow the class.

Consider d=1 and algorithms with state S_t=(m_t,h_t), h_t>0, prediction

  p_t = Phi(m_t,h_t)

for a smooth map Phi, and updates

  m_{t+1} = m_t + A(m_t,h_t,g_t,c_t),
  h_{t+1} = h_t + B(m_t,h_t,g_t,c_t),

where g_t and c_t are the local logistic gradient and curvature at m_t.
Assume:

1. Locality: A and B use the history only through (m_t,h_t,g_t,c_t).
2. Gaussian-tail regularity: for large positive m and h, Phi(m,h) has the same
   first-order tail form as a Gaussian logistic mixture, namely

      1 - Phi(m,h) >= a * exp(-b m)

   on the all-positive stream for fixed constants a,b>0.
3. Curvature accumulation: h_t grows at least monotonically and at most
   polynomially in t.
4. Mean drift: m_t grows sublogarithmically or as alpha log t with coefficient
   alpha too small to match the exact Bayesian predictive tail.

### Candidate theorem (LGSO)

For the all-positive sequence x_t=1,y_t=+1, if the above assumptions imply

  1-p_t >= c t^{-q}

with q <= 1,

then cumulative learner loss satisfies

  sum_t -log p_t >= c' * {
      T^(1-q),  q<1,
      log T,    q=1
  }.

If exact EW on the same prior has strictly smaller asymptotic loss growth, then
the approximation tax cannot be O(log T) in the q<1 case and may have a strictly
larger logarithmic constant in the q=1 case.

This reduces the problem to an asymptotic tail-rate comparison rather than an
opaque moment argument.

### What remains to prove

A theorem needs:
- an exact asymptotic for the EW predictive tail on the all-positive stream;
- a derived tail exponent for the local Gaussian update;
- a strict exponent/constant separation.

The executable experiments now estimate these exponents directly.
