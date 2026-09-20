# Sequential recompression accounting: exact identity and obstruction

Consider any approximate state Q_t before round t. For the realized likelihood
  L_t(theta)=p(y_t | x_t,theta) in (0,1),
define its predictive evidence
  Z_t(Q_t)=E_{Q_t}[L_t].
The learner incurs
  ell_t(Q_t)=-log Z_t(Q_t).

After observing y_t, the exact Bayes update of Q_t is
  Q_t^+(dtheta)=L_t(theta) Q_t(dtheta)/Z_t(Q_t).

Then a compression/projection produces Q_{t+1}.

## Change-of-measure identity for one compression

Let R_t = Q_t^+ be the uncompressed updated state and let C_t=Q_{t+1}
be its compressed replacement. For the NEXT likelihood L_{t+1},

  Z_{t+1}(C_t)/Z_{t+1}(R_t)
   = E_{R_t}[ L_{t+1} (dC_t/dR_t)] / E_{R_t}[L_{t+1}]

when absolutely continuous.

Equivalently the next excess predictive log loss is

  log Z_{t+1}(R_t) - log Z_{t+1}(C_t).

This quantity is an EVENT/LIKELIHOOD-SPECIFIC change of measure. It is not
equal in general to KL(R_t||C_t) or KL(C_t||R_t).

## Exact path-density viewpoint

If no compression is performed, multiplying the predictive evidences
telescopes:
  prod_t Z_t = integral prior(dtheta) prod_t L_t(theta).

With compression after every update, this exact global marginal-likelihood
identity is broken. Each compression changes the base measure used for all
future likelihood factors.

Thus there is no automatic KL telescope merely from "Bayes update then KL
projection."

## Generic KL cannot control adversarial next log loss

A two-state construction shows the obstruction.

Let parameter space {A,B}. Take
  R(A)=1-epsilon, R(B)=epsilon.
Construct C that reduces the rare-state mass B by factor exp(-M), with
normalization:
  C(B) approximately epsilon exp(-M),
  C(A) approximately 1.

Then
  KL(R||C) approximately epsilon M.

Choose epsilon=delta/M. The forward KL can stay about delta while M is
arbitrarily large.

Now choose a next likelihood concentrated on B:
  L(B)=1, L(A) approximately 0.
Then
  Z(R) approximately epsilon,
  Z(C) approximately epsilon exp(-M),
so the excess next log loss is approximately M.

Therefore arbitrarily small/fixed forward KL does NOT control worst-case
future predictive log loss.

Reverse KL also fails to protect mass that C deletes from regions that can
later become predictive.

For bounded logistic parameters/features, likelihood ratios are not literally
infinite, but the same phenomenon is limited by the available logit range BR;
a generic KL bound can therefore inherit undesirable B dependence.

## What divergence WOULD control all future likelihoods?

A sufficient condition is a pointwise density-ratio bound:
  exp(-rho) <= dC/dR <= exp(rho).
Then for every future likelihood 0<=L<=1,
  exp(-rho) Z(R) <= Z(C) <= exp(rho) Z(R),
so one-step predictive excess loss <= rho.

This is essentially an infinity/Renyi-infinity control, much stronger than KL.

A weaker task-specific condition can control only the logistic likelihood
class:
  sup_{||x||<=R,y}
  | log E_C sigma(y theta^T x)
    - log E_R sigma(y theta^T x) |
  <= rho.

Call this Predictive Likelihood Distortion (PLD).

## PLD

Define
  PLD_R(C)
   = sup_{x in X,y in {+-1}}
       | log E_C[L_{x,y}]
         - log E_R[L_{x,y}] |.

If each recompression R_t -> C_t has PLD <= rho_t, then the immediate next
prediction made from C_t differs from what R_t would predict by at most
rho_t in log loss for any adversarial next query/outcome.

But future updates compound compression errors, so a complete theorem needs
stability of PLD under Bayes updates or a cumulative path-space version.

## Decision

Generic KL/I-projection recompression is NOT enough for adversarial log-loss
regret. The hoped-for simple KL telescope is false.

The right compression objective must preserve the logistic predictive
likelihood class directly (or use a stronger density-ratio guarantee).

This returns us to a function-class compression problem, but with a cleaner
metric than t^-2 probability error: preserve LOG predictive evidence and study
how this metric propagates through Bayes updates.

Status:
- exact marginal-likelihood telescope without compression: established;
- automatic KL telescope under recompression: DISPROVED;
- generic forward/reverse KL control: insufficient;
- Predictive Likelihood Distortion: active metric, novelty unverified.
