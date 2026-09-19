# From predictive approximation to regret: the log-loss bridge

Let p_t in (0,1) be a reference predictive probability (e.g. exact EW) and
q_t in (0,1) an approximation. For y_t in {0,1}, binary log loss is

  ell(q,y) = -y log q -(1-y)log(1-q).

The approximation tax is

  Delta_t = ell(q_t,y_t)-ell(p_t,y_t).

## Deterministic clipped-probability bound

Assume both p_t and q_t lie in [alpha_t,1-alpha_t], alpha_t in (0,1/2], and

  |q_t-p_t| <= delta_t < alpha_t.

By the mean value theorem,

  |Delta_t|
  <= |q_t-p_t| / min{alpha_t-delta_t, alpha_t}
  <= delta_t/(alpha_t-delta_t).

In particular if delta_t <= alpha_t/2,

  Delta_t <= 2 delta_t/alpha_t.

Therefore

  sum_t Delta_t <= 2 sum_t delta_t/alpha_t.

So a sufficient condition for O(log T) approximation tax is

  sum_{t<=T} delta_t/alpha_t = O(log T).

## Consequence for a 1/t clipping floor

If alpha_t = c/t, then it suffices to have

  delta_t = O(1/t^2),

because

  delta_t/alpha_t = O(1/t)

and hence

  sum_t Delta_t = O(log T).

More generally, alpha_t=Theta(t^{-a}) and delta_t=O(t^{-a-1}) suffice.

This exposes the real accuracy requirement: absolute probability error must
shrink faster near the boundary because log loss is not globally Lipschitz.

## Polynomial closure requirement

Suppose a prediction has the form

  p_t = E[R_{k_t}(u)]

and we approximate R_{k_t} uniformly by degree m_t polynomial P_t with

  ||R_{k_t}-P_t||_infinity <= epsilon_t.

Then automatically

  |E[R_{k_t}(u)]-E[P_t(u)]| <= epsilon_t.

Thus set epsilon_t <= delta_t.

Using the pole-geometry upper target

  m_t = O(k_t[log k_t + log(1/epsilon_t)]),

and the sufficient schedule epsilon_t=Theta(t^{-2}) for alpha_t=Theta(1/t),

  m_t = O(k_t[log k_t + log t]).

If k_t is bounded by poly(d,B) independently of T, the required degree is only
poly(d,B)*log T.

This is a positive bridge: the pole geometry by itself does NOT force
polynomial-in-T approximation degree.

## But moment maintenance is the remaining bottleneck

A degree-m polynomial approximation requires expectations

  E[u^j], j=0,...,m.

The posterior changes every round. Unless these moments admit efficient online
updates or controlled approximations, the polynomial representation does not
yet give an efficient online algorithm.

For logistic updating, multiplying a posterior by sigma(z) generally maps
moments of u to higher moments. In the repeated identical-direction positive
case, however, the transformed density is multiplied by u, and moments obey

  M_j^{new} = M_{j+1}^{old}/M_1^{old}.

Thus exact finite moment vectors are NOT closed: updating the top stored moment
M_m requires M_{m+1}.

Negative labels similarly multiply by (1-u):

  M_j^{new} = (M_j-M_{j+1})/(1-M_1).

Again one extra moment is needed.

This gives a concrete closure leak at the state-update stage.

## Repeated-direction special structure

After n_+ positive and n_- negative labels, the posterior push-forward over u
is proportional to

  prior_u(u) u^{n_+}(1-u)^{n_-}.

Therefore all required moments can in principle be represented through ratios
of one-dimensional integrals. That is computationally tractable in 1D, but it
does not solve arbitrary d-dimensional online logistic regression.

## Candidate algorithmic target

Compressed-EW predictor should maintain a basis whose UPDATE operator and
PREDICTION operator are both approximately closed:

  state_t --update(x_t,y_t)--> state_{t+1}
  state_t --predict(x)-------> q_t(x).

Polynomial approximation solves only prediction closure. The hard missing
piece is update closure under arbitrary changing directions.

## New criterion: Bidirectional Closure Complexity (BCC)

For a function/basis family B, define informally

  BCC(epsilon,T)

as the minimum state dimension required so that:
1. posterior update under every admissible logistic factor can be approximated
   within the required tolerance; and
2. next-round sigmoid expectations can be recovered within that tolerance.

A useful efficient-EW construction needs BCC=poly(d,log T, relevant norm
parameters), not merely low prediction approximation degree.

This is a research definition, not yet a novelty claim.

## Paper gate

Do not write the main paper yet.

The next paper-triggering result would be one of:

A. Construct an approximately update-closed basis with
   BCC=poly(d,log T) (and acceptable B dependence), then combine the
   approximation-tax lemma with EW regret.

B. Prove a lower bound showing BCC must grow super-polynomially for a meaningful
   class of posterior-compression schemes under arbitrary adversarial
   directions.

The log-loss bridge in this note should become a lemma in either paper.
