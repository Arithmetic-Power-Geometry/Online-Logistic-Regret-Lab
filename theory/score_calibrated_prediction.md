# Score-Calibrated Prediction (SCP): new algorithmic direction

## Why this direction

The previous Gaussian obstruction shows that directly replacing the EW posterior
by a Gaussian and integrating the sigmoid can destroy the predictive tail.

But Gaussian shape error does NOT imply that prediction itself requires the full
posterior. Under a Gaussian prior, posterior score identities can determine
certain predictive probabilities from posterior means and low-dimensional
sufficient statistics.

This suggests a different principle:

> Approximate the posterior moments needed by an exact score identity, rather
> than approximate the posterior density and then integrate the loss.

We call this Score-Calibrated Prediction (SCP).

## Exact 1D repeated-direction identity

Let theta have Gaussian prior N(0,s^2). Suppose all observed covariates are
x_i=1. Let n_+ and n_- be the positive and negative label counts, n=n_++n_-.

The posterior density is proportional to

  exp(-theta^2/(2s^2))
  sigma(theta)^{n_+}
  sigma(-theta)^{n_-}.

Let

  mu_n = E_n[theta],
  p_n  = E_n[sigma(theta)].

The posterior score is

  d/dtheta log q_n(theta)
  = n_+ sigma(-theta) - n_- sigma(theta) - theta/s^2.

Its posterior expectation is zero. Since sigma(-theta)=1-sigma(theta),

  n_+(1-p_n) - n_- p_n - mu_n/s^2 = 0.

Therefore, EXACTLY,

  p_n = n_+/n - mu_n/(s^2 n).

This is not an approximation.

Thus on a repeated one-dimensional direction, the Bayesian/EW predictive
probability is determined by only:
- positive count,
- total count,
- posterior mean.

No posterior tail integral is required.

## Finite dictionary generalization

Suppose x_i belongs to a finite dictionary of r directions
v_1,...,v_r in R^d. For direction j let n_j^+, n_j^- and n_j be its counts.
Define

  p_j = E[sigma(theta^T v_j)],
  mu  = E[theta].

The expected posterior score gives

  sum_j v_j [n_j^+ - n_j p_j] = mu/s^2.

Let V=[v_1 ... v_r] and a_j=n_j^+-n_j p_j. Then

  V a = mu/s^2.

If V has full column rank (r<=d), then

  a = V^+ mu/s^2

and every predictive probability is exactly recoverable:

  p_j = [n_j^+ - (V^+mu/s^2)_j]/n_j.

## Candidate principle: Score-Identifiable Prediction

Whenever the vector of posterior predictive expectations enters an invertible
posterior score system, prediction can be recovered from posterior moments
without reconstructing the posterior density.

This suggests an online architecture:

1. maintain an approximation mu_hat_t to the EW posterior mean;
2. maintain the score-design sufficient statistics;
3. solve the low-dimensional score system for predictive probabilities;
4. clip only for numerical safety;
5. fall back to another improper predictor for score-unidentifiable directions.

The research question is whether the posterior-mean approximation error can be
controlled strongly enough that the resulting regret is O(poly(d) log T)
without linear B dependence and with practical polynomial per-round cost.

## Immediate falsification tasks

A. Verify the exact 1D identity numerically against grid EW for arbitrary label
sequences.

B. Verify the finite-dictionary identity in low dimension using numerical
quadrature / enumeration where possible.

C. Replace exact mu by the Gaussian/Laplace mean and measure whether score
calibration removes the catastrophic all-positive predictive-tail error.

D. Construct dependent-direction cases r>d. The score system becomes
underdetermined; test whether this is the fundamental obstruction.

No novelty claim is made until prior art on Stein identities, Bayesian logistic
regression, assumed-density filtering, expectation propagation, and online
score calibration is exhausted.
