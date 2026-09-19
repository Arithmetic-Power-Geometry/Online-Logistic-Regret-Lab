# Can predictive approximation tax be quadratic? Pathwise audit

Let p in (0,1) be a reference probability and q=p+e an approximation.
For outcome y in {0,1}, binary log-loss difference is

  D_y(p,q)
   = -y log q -(1-y)log(1-q)
     +y log p +(1-y)log(1-p).

Exactly:
  D_1 = log(p/q) = -log(1+e/p),
  D_0 = log((1-p)/(1-q)) = -log(1-e/(1-p)).

Taylor expansion:
  D_y
   = e * [(1-y)/(1-p) - y/p]
     + (e^2/2)*[y/p^2+(1-y)/(1-p)^2]
     + O(e^3).

Thus for a FIXED realized adversarial outcome, there is generically a
first-order term.

## One-round impossibility of a universal quadratic pathwise bridge

Take y=0 and q=p+e with e>0. Then
  D_0 = -log(1-e/(1-p))
      >= e/(1-p).

As e -> 0 this is linear in e. Therefore no universal constant C can satisfy

  D_y(p,q) <= C e^2/[p(1-p)]

for all sufficiently small e, all p, and both outcomes.

Similarly choose y=1 and e<0.

Hence a purely pathwise quadratic approximation-tax inequality is FALSE.

This kills the hope that arbitrary probability approximation can replace the
first-order bridge by Bernoulli KL.

## Why Bernoulli KL is quadratic

If y is RANDOM with y~Bernoulli(p), then the first-order terms cancel in
expectation:

  E_y[D_y(p,q)]
   = KL(Ber(p)||Ber(q))
   = e^2/[2p(1-p)] + O(e^3).

But adversarial online logistic regression does not draw y_t from p_t.
Therefore this expectation cannot be used directly.

## Structural cancellation requirement

To obtain a quadratic/telescoping tax in the adversarial setting, the
approximation error e_t must be coupled to a potential/accounting term whose
first-order contribution telescopes or is prepaid by another part of the
algorithm.

A nearby-posterior construction alone does not automatically guarantee this:
the adversary observes the learner prediction and can choose the outcome
aligned with the sign of the probability error.

## Candidate compensated bridge

Seek an algorithm with an internal correction/account C_t such that

  ell(q_t,y_t)-ell(p_t,y_t)
    <= C_t-C_{t+1}
       + C * (q_t-p_t)^2/[p_t(1-p_t)]

(or a clipped analogue).

Then summing removes the first-order term.

This is analogous in spirit to optimistic/corrected online-learning analyses:
prediction error can be quadratic only when the linear error is explicitly
cancelled by an update/potential.

## Immediate implication

Without such compensation, the original absolute-error requirement is not an
artifact of loose analysis. It is locally necessary in the adversarial
pathwise setting.

Therefore ordinary posterior/coreset approximation with error O(1/sqrt(m))
cannot achieve polylog(T) complexity merely by invoking Bernoulli KL.

## Next theorem target

Derive a compensated prediction rule q_t from an approximate EW probability
p_hat_t plus a correction based on the approximation residual/gradient, so
that the first-order log-loss term is canceled in the cumulative potential.

If no observable correction can estimate the sign/magnitude of p_hat_t-p_t
without essentially solving the exact prediction problem, this may itself be
a computational obstruction.

Status:
- universal pathwise quadratic bridge: DISPROVED;
- stochastic/Bernoulli-p quadratic bridge: true but irrelevant to adversarial
  labels by itself;
- compensated/telescoping bridge: open.
