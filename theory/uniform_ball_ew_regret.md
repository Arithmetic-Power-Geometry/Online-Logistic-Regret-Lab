# Uniform-ball Bayesian mixture regret and boundary geometry

## Setting

Theta = B_2(0,B) subset R^d.
Prior pi is uniform on Theta.
Features satisfy ||x_t||_2 <= R.
Labels y_t in {+-1}.
Likelihood
  L_t(theta)=sigma(y_t theta^T x_t),
so comparator cumulative logistic loss is
  L_T(theta)=sum_t -log L_t(theta).

The Bayesian mixture predicts the exact posterior predictive probability.
By the marginal-likelihood identity its cumulative log loss is

  L_mix = -log E_{theta~pi}[ exp(-L_T(theta)) ].

## Lipschitz loss

For one round,
  grad_theta log(1+exp(-y theta^T x))
   = - y x sigma(-y theta^T x),
so
  ||grad ell_t(theta)|| <= ||x_t|| <= R.

Hence
  |L_T(theta)-L_T(theta*)| <= T R ||theta-theta*||.

## Uniform-prior local mass at boundary

Fix any comparator theta* in B_2(0,B), and 0<delta<=B.

Define an inward-shifted center
  c = (1-delta/(2B)) theta*.

Then ||c|| <= B-delta/2.

Therefore the ball B_2(c,delta/2) lies inside B_2(0,B).

Also
  ||c-theta*|| = (delta/(2B))||theta*|| <= delta/2,
so B_2(c,delta/2) lies inside B_2(theta*,delta).

Thus

  Vol( Theta intersect B(theta*,delta) )
  >= Vol(B_d(delta/2)).

Under the uniform prior on B_d(B),

  pi(B(theta*,delta))
  >= (delta/(2B))^d.

This handles the worst comparator on the boundary with no cone theorem.

## Regret theorem

On A_delta = Theta intersect B(theta*,delta),

  L_T(theta) <= L_T(theta*) + TR delta.

Therefore

  E_pi[e^{-L_T(theta)}]
  >= pi(A_delta) exp(-L_T(theta*)-TR delta).

Taking -log:

  L_mix - L_T(theta*)
  <= TR delta + d log(2B/delta).

Choose
  delta = min(B, 1/(TR))
when T,R positive.

If 1/(TR)<=B,

  Regret_T(theta*)
  <= 1 + d log(2 B R T).

Thus for every ||theta*||<=B,

  R_T(theta*) <= 1 + d log(2BRT)

in the nontrivial BRT>=1 regime.

For BRT<1, choose delta=B to obtain a constant-scale bound
  <= BRT + d log 2.

Hence a clean safe statement is

  R_T(theta*) <= O(1 + d log(1+BRT)),

with explicit piecewise constants above.

## Significance

This gives the bounded-domain reference regret directly. No Gaussian prior is
needed.

The Bayesian mixture is improper in prediction space: it predicts a mixture
probability, not necessarily sigma(theta^T x) for a single theta.

The bound is adversarial and uses only:
- exact log-loss marginal-likelihood identity;
- R-Lipschitz logistic loss in theta;
- volume of a local ball under the uniform prior.

## Boundary denominator for surrogate integration

For numerical integration over Theta=B_2(0,B), suppose the surrogate potential
Fhat_t is convex, has minimizer theta_hat in Theta, and Hessian upper bound

  nabla^2 Fhat_t <= Lambda_t I

along feasible local segments.

Take r <= min(B, Lambda_t^{-1/2}).
Apply the same inward-ball construction at theta_hat with radius r:
there exists a ball of radius r/2 contained in
  Theta intersect B(theta_hat,r).

For theta in that inner ball,
  ||theta-theta_hat||<=r.
For a constrained minimizer at the boundary, the first-order term
  grad Fhat(theta_hat)^T(theta-theta_hat)
is nonnegative for feasible theta, so an UPPER Taylor bound cannot simply drop
it. This is a subtlety.

If theta_hat is an interior stationary point, then
  Fhat(theta)-Fhat(theta_hat) <= Lambda_t r^2/2 <= 1/2,
and denominator >= e^-1/2 Vol(B_d(r/2)) = Omega(Lambda_t^-d/2).

At a boundary constrained mode, a separate upper bound on the directional
first-order term is required. The prior-ball volume argument alone does NOT
close the denominator bound.

## Repair options for boundary mode

A. Use a prior/barrier whose potential forces the posterior mode into the
   interior while keeping enough local prior mass for regret.
B. Integrate around an interior near-minimizer rather than the exact boundary
   mode, paying controlled potential gap.
C. Bound ||grad Fhat(theta_hat)|| and choose a smaller inward radius.

The reference-regret gap is CLOSED.
The numerical boundary-denominator gap remains OPEN.
