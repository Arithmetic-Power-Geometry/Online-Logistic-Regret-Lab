# Predictive-gradient coreset: variance gate

## Prior-art boundary

Logistic-regression coresets, local sensitivity via leverage scores, online
Lewis-weight sampling, streaming coresets, and gradient-approximating coresets
already exist. We do not claim those primitives.

Our target is different:
maintain an approximation to the EW/Bayesian posterior whose NEXT predictive
probability is accurate enough to incur only O(log T) extra sequential
log-loss regret.

## Gradient target

Historical nonlinear gradient:
  g(theta)=sum_i h'(theta^T x_i) x_i.

At center theta_bar:
  g_bar=sum_i h'(a_i)x_i,
  H=s^{-2}I+sum_i w_i x_i x_i^T,
  w_i=h''(a_i).

A sampled approximation should control
  ||ghat(theta)-g(theta)||_{H^{-1}}
under the posterior, because an H-metric gradient-error bound can feed the
log-concave concentration/KL bridge.

## Simple independent sampling calculation

Suppose terms v_i(theta) are sampled independently with probabilities p_i and
reweighted. The H^{-1}-metric variance is of the generic form

  Var_H <= (1/m) sum_i ||v_i||_{H^{-1}}^2 / p_i

(after normalization conventions).

Optimal importance probabilities are proportional to
  ||v_i||_{H^{-1}},
giving squared total sensitivity
  (sum_i ||v_i||_{H^{-1}})^2 / m.

For curvature-linearized variation,
  v_i ~ w_i x_i x_i^T (theta-theta_bar).

Writing l_i=x_i^T H^{-1}x_i and ||theta-theta_bar||_H<=r,

  ||v_i||_{H^{-1}}
  <= w_i sqrt(l_i) |x_i^T(theta-theta_bar)|
  <= r w_i l_i.

Therefore
  sum_i ||v_i||_{H^{-1}}
  <= r sum_i w_i l_i
  <= r d.

Hence the linearized gradient variation admits an importance-sampling
variance scale at most

  O(r^2 d^2 / m),

independent of history length t.

This is a second concrete place where the weighted leverage identity removes t.

## Accuracy gate

If we demanded gradient-error scale epsilon_t=Theta(t^-2), this crude
Monte-Carlo bound would still require

  m = Omega(r^2 d^2 t^4),

which is unacceptable.

Therefore removing the t factor from the DATA SUM is not sufficient by itself:
ordinary sampling variance decays only as m^{-1/2}, while our per-round
predictive target t^-2 becomes increasingly stringent.

## Consequence

A fresh coreset resampled to absolute accuracy t^-2 cannot have poly(log T)
size under ordinary Monte Carlo concentration.

To get poly(log T), we need one of:

1. deterministic/high-order approximation with exponential convergence in
   representation size;
2. a regret bridge that requires much weaker per-round predictive accuracy
   than t^-2;
3. exploit cancellation so approximation tax depends on squared error, allowing
   epsilon_t about t^-1/2 or t^-1 (depending on boundary behavior);
4. exact/near-exact sufficient representation for the predictive functional.

This identifies a likely over-stringency in our current bridge.

## Next best target

Revisit the approximation-to-log-loss bridge using the exact Bernoulli KL
identity. For a reference probability p and approximate q,

  expected excess log loss under Bernoulli(p) is KL(Ber(p)||Ber(q))
  ~ (p-q)^2/[2 p(1-p)].

Pathwise adversarial loss has a first-order term and needs the stronger
absolute-error bound, but EW mixability/potential analysis may allow a
second-order or telescoping control of approximation error.

If the approximation tax can be bounded by
  sum_t (q_t-p_t)^2/[p_t(1-p_t)]
rather than
  sum_t |q_t-p_t|/alpha_t,
then with p_t(1-p_t) ~ 1/t at the boundary, epsilon_t=O(1/t)
already gives summable/logarithmic tax.

That would reduce sampling requirement from t^4 to t^2, still not polylog;
epsilon_t=O(t^-1/2) would give constant per-step weighted KL and is too large.
Further telescoping/biased structure would still be needed.

Status:
- t-free linearized gradient sensitivity: established;
- ordinary Monte Carlo cannot meet t^-2 with polylog samples;
- next target: sharpen the regret bridge before building a coreset.
