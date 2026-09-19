# Predictive-regret coresets: narrower target than Bayesian likelihood coresets

## Prior-art correction

Bayesian logistic-regression coresets already approximate the full
log-likelihood/posterior and can be constructed in streaming settings.
Therefore "compress the logistic posterior with a coreset" is NOT a novelty
claim.

Our online objective is different and potentially weaker:

We do not need a uniform multiplicative approximation to the entire historical
log-likelihood for every theta. At round t we only need the next predictive
probability accurate enough that cumulative extra log loss is O(log T).

From approximation_to_regret_bridge.md, with clipping alpha_t=Theta(1/t), a
sufficient schedule is

  |q_t(x_t)-p_t(x_t)| = O(1/t^2).

This motivates a task-specific object.

## Predictive-Regret Coreset (PRC)

Given a reference EW posterior Q_t and compressed weighted history C_t, define
Q_t^C as the posterior induced by C_t.

A sequence C_t is an epsilon_t predictive coreset along an online sequence if

  | E_{Q_t^C}[sigma(theta^T x_t)]
    - E_{Q_t}[sigma(theta^T x_t)] |
  <= epsilon_t

for the actually queried next direction x_t.

A stronger anticipatory version requires the bound for every admissible
x in X before x_t is revealed:

  sup_{x in X}
  | E_{Q_t^C}[sigma(theta^T x)]
    - E_{Q_t}[sigma(theta^T x)] |
  <= epsilon_t.

If epsilon_t=O(t^-2) and probabilities are clipped at Theta(1/t), the
compressed predictor pays only O(log T) additional log loss.

## Why this is potentially weaker than classical coresets

Classical Bayesian logistic coresets target approximation of the entire
historical likelihood/posterior over parameter space.

PRC targets only posterior expectations of the predictive function class

  F = { theta -> sigma(theta^T x) : x in X }.

Thus a likelihood coreset implies useful posterior control under suitable
conditions, but PRC need not approximate the likelihood pointwise.

This distinction could permit smaller online summaries.

## Critical timing issue

If x_t is observed BEFORE prediction (standard online supervised protocol), the
learner may adapt computation to x_t at round t. Therefore the weakest useful
PRC only needs accuracy at the current query x_t, not uniformly over all future
directions.

That makes the compression problem significantly easier than an anticipatory
uniform coreset.

## Candidate theorem template

Suppose an algorithm maintains C_t with:
1. update time poly(d, log t, B);
2. size poly(d, log t, B);
3. after seeing x_t, it computes q_t satisfying
      |q_t-p_t^EW| <= c/t^2;
4. q_t and p_t^EW are clipped to [c0/t,1-c0/t].

Then

  L_T(PRC) - L_T(EW) = O(log T).

Combining with a reference EW regret R_T^EW gives

  R_T(PRC) <= R_T^EW + O(log T).

This theorem is elementary once property 3 is achieved. The research problem
is construction of C_t/property 3.

## Next construction attempt: query-adaptive compression

Because x_t is known before prediction, seek a summary that preserves the
one-dimensional push-forward distribution of

  z = theta^T x_t

only to the accuracy needed for E[sigma(z)].

Historical factors depend on theta in many directions, but for one query x_t
their effect is integrated over orthogonal directions.

Potential routes:
- deterministic quadrature after low-rank projection;
- query-specific Laplace/tilting correction;
- random-feature approximation to historical softplus sum;
- sensitivity sampling targeted to the current sigmoid expectation rather than
  uniform likelihood approximation.

No novelty claim until these are compared against Bayesian coresets, Bayesian
coreset predictive guarantees, online/streaming coresets, and approximate
Bayesian prediction literature.

## Paper gate

Do not write yet.

A paper becomes justified if we prove either:
A. PRC construction with size/update complexity poly(d,log T,B) and
   epsilon_t=O(t^-2), yielding an explicit regret theorem; or
B. a lower bound showing even query-adaptive predictive compression requires
   substantially growing state for a meaningful algorithm class.

At that point stop expanding concepts and write.
