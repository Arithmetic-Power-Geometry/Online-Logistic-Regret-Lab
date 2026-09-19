# KL stability for posterior-potential perturbations

Let Q have density
  q(theta)=exp(-F(theta))/Z,
and let Qhat be induced by an approximate potential
  Fhat(theta)=F(theta)+Delta(theta).

Then
  qhat(theta)
    = q(theta) exp(-Delta(theta)) / E_Q[exp(-Delta)].

Therefore exactly,

  KL(Q || Qhat)
    = E_Q[Delta] + log E_Q[exp(-Delta)].

Because adding a constant to Delta changes neither Qhat nor this KL, define the
centered perturbation

  X = Delta - E_Q[Delta].

Then

  KL(Q || Qhat) = log E_Q[exp(-X)].

This identity exposes the correct target: not mean absolute potential error,
but a centered exponential-moment bound.

## Sub-Gaussian sufficient condition

If X is sigma_Delta^2-sub-Gaussian under Q,

  log E_Q[exp(lambda X)]
    <= lambda^2 sigma_Delta^2 / 2

for all relevant lambda, then at lambda=-1,

  KL(Q || Qhat) <= sigma_Delta^2/2.

Pinsker gives

  TV(Q,Qhat) <= sqrt(KL/2) <= sigma_Delta/2.

For any f in [0,1],

  |E_Q f-E_Qhat f| <= TV(Q,Qhat)
                    <= sigma_Delta/2.

Thus logistic predictive error O(t^-2) follows if the CENTERED potential
perturbation has sub-Gaussian scale

  sigma_Delta = O(t^-2).

This is stronger than merely Var(Delta)=O(t^-4): variance alone does not
control the exponential moment.

## Strong-log-concavity route

If Q is alpha-strongly log-concave and Delta is L_Delta-Lipschitz in Euclidean
norm, standard concentration for strongly log-concave measures gives a
sub-Gaussian bound with scale on the order of

  sigma_Delta^2 <= L_Delta^2 / alpha.

Here alpha >= s^{-2}, so the universal bound becomes

  sigma_Delta <= s L_Delta.

This would be useful only if the sketch error Delta has Lipschitz constant
O(t^-2/s), which a naive accumulated sketch is unlikely to satisfy.

## Metric refinement

The natural local metric is a curvature matrix H. If a log-Sobolev /
concentration inequality is available in the H metric, then a gradient bound

  sup_theta ||grad Delta(theta)||_{H^{-1}} <= eps

would imply centered sub-Gaussian scale O(eps), up to constants.

This suggests a new sketch objective:

  preserve the GRADIENT of the historical potential in the posterior metric,

rather than preserve its absolute value.

## Why gradient is structurally attractive

For the nonlinear historical term
  G(theta)=sum_i h(theta^T x_i),

  grad G(theta)=sum_i h'(theta^T x_i) x_i,
  Hess G(theta)=sum_i h''(theta^T x_i) x_i x_i^T.

At the center, Hessian weights are exactly
  w_i=h''(theta_bar^T x_i),

and their leverage obeys
  sum_i w_i x_i^T H^{-1}x_i <= d.

Therefore a randomized approximation whose gradient-error variance is charged
to w_i x_i^T H^{-1}x_i could have dimension dependence rather than history
length dependence.

## Critical obstacle

Ordinary polynomial-kernel sketches approximate function values/inner
products. We need a concentration guarantee for the GRADIENT ERROR in an
adaptive posterior metric, uniformly or exponentially under Q.

This is not supplied automatically by the previous tensor-sketch argument.

## New theorem target

Construct an online random-feature/tensor sketch Delta_t satisfying

  log E_Qt exp(
    lambda [Delta_t-E_Qt Delta_t]
  ) <= lambda^2 eps_t^2/2

with eps_t=O(t^-2), using poly(d,B,log T) state/time.

Equivalent sufficient route:
- prove posterior-metric gradient error is O(t^-2);
- invoke an appropriate log-Sobolev/concentration inequality.

Then:
  KL(Q_t||Qhat_t)=O(t^-4),
  TV=O(t^-2),
  predictive error=O(t^-2),
  approximation tax=O(log T).

Status:
- exact KL identity: established;
- sub-Gaussian-to-prediction bridge: established;
- construction with polylog(T) complexity: open.
