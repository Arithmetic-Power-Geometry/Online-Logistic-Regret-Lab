# Manuscript blueprint — FROZEN after paper gate

## Recommended title

**Compressing Exponential Weights for Online Logistic Regression: Exact Identities, Failed Surrogates, and a Geometric Bottleneck**

Alternative, more theorem-forward:
**Toward Practical Near-Optimal Online Logistic Regression: Update-Closed Compression and the Geometry of Exponential Weights**

Do NOT use "solving the Google open problem" in the title or abstract.

## Literature position

- Foster et al. (COLT 2018): efficient improper learning and positive resolution to a variant of the 2012 open problem; near-optimal norm dependence but computationally prohibitive construction.
- Jezequel, Gaillard, Rudi (COLT 2020): practical improper algorithm with O(B log(BT)) regret and O(d^2+log T) per-round complexity.
- Di Gennaro, Chakraborty, Zhivotovskiy (AISTATS 2026): Gaussian-prior EW achieves near-optimal O(d log(BT)) regret with proved total worst-case computation roughly tilde-O(B^3 T^5), substantially improving the older huge polynomial but still strongly horizon-dependent.

Our manuscript does NOT claim a new complete O(poly(d) log T)-time algorithm.

## Central question

Can the near-optimal exponential-weights predictor be represented and evaluated from an update-closed state whose horizon dependence is polylogarithmic, at least in fixed dimension?

## Contributions — claim-safe ordering

### C1. Exact predictive score identities
For repeated directions / finite independent dictionaries, posterior score identities recover predictive probabilities from low-order state exactly. Introduce score-nullity only as an algebraic diagnostic, not a universal impossibility measure.

### C2. Counterexamples to natural compression architectures
Document rigorous/numerical counterexamples at the level actually certified:
- projection-only query compression fails badly on explicit reachable 2D histories;
- exact mean+covariance Gaussian replacement fails the t^-2 predictive schedule on explicit grid-EW histories;
- adding directional third cumulant does not repair that tested family;
- generic forward/reverse KL recompression cannot control adversarial next-step log evidence (two-state exact counterexample);
- naive sequential oscillation errors accumulate with age-weighted cost.

Avoid claiming universal lower bounds from numerical witnesses.

### C3. Update-closed log-cosh tensor representation
Use
  log(1+exp(-yz))=log 2-yz/2+log cosh(z/2).
Approximate the even log-cosh term by a convexity-preserving curvature-first polynomial.
Historical nonlinear terms are represented by additive symmetric tensors
  S_{2j,t}=sum_{s<t} x_s^{tensor 2j}.
For fixed d and degree m=O(BR log t), state size is poly_d(log t).

### C4. Approximation-to-regret bridge
If current approximate predictive log evidence differs from exact reference EW by O(1/t), cumulative extra loss is O(log T).
Centered potential oscillation O(1/t) suffices.
Per-factor bounded-domain approximation O(t^-2) suffices after aggregation.

### C5. Bounded-domain reference mixture regret
Using a uniform cube prior on [-B,B]^d, compete against every l2 comparator ||theta*||<=B:
  R_mix(theta*) <= 1+d log(2 B sqrt(d) R T)
in the nontrivial regime, hence O(d log(BRT)).

### C6. Logistic analytic geometry
Exact complex curvature:
  |g''(a+ib)|/g''(a) <= sec^2(b/2), |b|<pi.
Directional curvature-height theorem:
  Delta_v(r)
  >= alpha r^2/2
     +(v^T H(theta_hat+rv)v-alpha)
       [1-(1+Rr)e^{-Rr}]/R^2.
This holds on every ray in R^d.

### C7. One-dimensional polylog integration route
Adaptive analytic intervals yield O(log t) pieces and O(log t) Chebyshev degree per piece, giving an O(log^2 t)-scale deterministic quadrature skeleton under the stated bounded-domain/surrogate perturbation assumptions.
State exact assumptions and constants; do not oversell if final constant proof remains in notes.

### C8. Structured multidimensional cases and bottleneck
Separable/fixed finite-direction families admit polylog fixed-d covering.
For unrestricted directions, reduce the remaining deterministic integration issue to controlling Hessian-metric covering/volume of O(log T) posterior sublevel sets.
State as OPEN.

### C9. Empirical geometric evidence
In d=2 adversarial direction search, metric volume over A=2 log(T+2) sublevels had V/log T approximately flat over T=16,...,256.
Present only as evidence motivating the open geometric conjecture.

## Main open statement

Conjecture / Open Problem:
For fixed d,R,alpha, characterize whether
  int_{F-Fmin<=A} sqrt(det nabla^2F(theta)) dtheta
is bounded by poly_{d,R,alpha}(A), uniformly over the number and directions of bounded logistic ridge terms.

Do NOT label this a theorem.

## Suggested theorem/lemma sequence in manuscript

Theorem 1: bounded-domain Bayesian-mixture regret.
Lemma 2: exact score identity.
Proposition 3: finite-dictionary score recovery.
Proposition 4: update-closed log-cosh tensor state.
Lemma 5: convexity-preserving curvature surrogate.
Lemma 6: posterior/evidence stability from centered potential approximation.
Theorem 7: exact complex logistic-curvature bound.
Theorem 8: directional curvature-height inequality.
Proposition 9: 1D adaptive quadrature complexity (with explicit assumptions).
Proposition 10: structured multidimensional cover.
Counterexample 11: generic KL recompression failure.
Section 7/8: unrestricted-direction metric-volume bottleneck and d=2 evidence.

Counterexamples to Gaussian/projection compression can be grouped in an experiments/negative-results section rather than inflated into universal theorems.

## Abstract draft facts

The abstract should say:
- near-optimal regret for EW is known;
- computational realization remains expensive in the near-optimal EW line;
- we study update-closed compression/evaluation rather than claim a complete new O(poly(d)log T) algorithm;
- give exact identities, negative results for natural compressions, update-closed polynomial state, bounded-domain regret/stability lemmas, analytic curvature/localization results;
- identify a precise fixed-d geometric bottleneck;
- empirical d=2 evidence supports favorable metric-volume scaling.

## Paper gate

FIRED. Manuscript writing begins now.
Research exploration remains frozen unless manuscript proof-checking reveals an actual error in a stated proved result.
