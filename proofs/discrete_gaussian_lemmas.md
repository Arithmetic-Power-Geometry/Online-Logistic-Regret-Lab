# Discrete comparison lemmas for Gaussian recursion

We analyze the exact implemented recursion on x_t=1,y_t=+1:

  a_t = 1/(1+e^{m_t}),
  c_t = a_t(1-a_t),
  h_{t+1} = h_t + c_t,
  m_{t+1} = m_t + eta a_t / h_{t+1}.

Assume eta in (0,1].

## Lemma 1: monotonicity

For all t:
- a_t in (0,1),
- c_t>0,
- h_{t+1}>h_t,
- m_{t+1}>m_t.

Hence h_t and m_t are increasing.

## Lemma 2: increment-ratio bounds

Because c_t=a_t(1-a_t),

  (m_{t+1}-m_t)/(h_{t+1}-h_t)
  = eta / [h_{t+1}(1-a_t)].

Once m_t>=0, a_t<=1/2, so

  eta/h_{t+1}
  <= Delta m_t / Delta h_t
  <= 2 eta/h_{t+1}.

More sharply, for any epsilon>0, once m_t is large enough that a_t<=epsilon,

  eta/h_{t+1}
  <= Delta m_t / Delta h_t
  <= eta/[(1-epsilon)h_{t+1}].

This implies asymptotic equivalence

  Delta m_t / Delta h_t ~ eta/h_t.

## Lemma 3: logarithmic coupling candidate

Since log h is concave and h_{t+1}-h_t=c_t=o(h_t), compare

  log h_{t+1}-log h_t

with c_t/h_{t+1} and c_t/h_t:

  c_t/h_{t+1}
  <= log h_{t+1}-log h_t
  <= c_t/h_t.

Combining with Lemma 2 gives, eventually,

  eta [log h_{t+1}-log h_t]
  <= Delta m_t
  <= eta/(1-epsilon) * [c_t/h_{t+1}] * [h_{t+1}/h_t].

Because c_t/h_t -> 0 if h_t -> infinity, h_{t+1}/h_t ->1. Therefore summation suggests

  m_t = eta log h_t + O(1) + o(log h_t).

The remaining rigorous task is to prove h_t->infinity and c_t/h_t->0.

## Lemma 4: divergence of h_t

Suppose h_t were bounded. Then m_t is increasing. If m_t also bounded, a_t and c_t stay bounded away from zero, forcing h_t to diverge, contradiction.

If m_t->infinity while h_t stayed bounded, then from the increment ratio above,

  Delta m_t >= eta Delta h_t / h_{t+1}.

This alone does not contradict bounded h, so a separate summability argument is needed. However the exact relation

  Delta m_t = eta a_t/h_{t+1},
  Delta h_t = a_t(1-a_t)

shows that if sum c_t<infinity then sum a_t<infinity eventually, hence sum Delta m_t<infinity because h_{t+1}>=h_1, so m_t would remain bounded, contradiction.

Therefore h_t->infinity.

Consequently c_t/h_t<=1/(4h_t)->0.

## Corollary candidate

For every epsilon>0 there exists t_epsilon such that for t>=t_epsilon,

  eta log h_t - C_epsilon
  <= m_t
  <= eta/(1-epsilon) log h_t + C_epsilon.

Letting epsilon->0 yields

  m_t/log h_t -> eta.

## Lemma 5: polynomial precision growth

From m_t = eta log h_t + o(log h_t),

  a_t = 1/(1+e^{m_t}) = h_t^{-eta+o(1)}.

Since c_t=a_t(1-a_t)=h_t^{-eta+o(1)},

  h_{t+1}-h_t = h_t^{-eta+o(1)}.

Standard comparison for regularly varying recursions then gives

  log h_t / log t -> 1/(1+eta),

hence

  m_t/log t -> eta/(1+eta).

This establishes the exponent at the level of logarithmic asymptotics.

## What is still needed for theorem-grade bounds

To obtain Theta rather than exponent-only asymptotics, prove boundedness of

  m_t - eta log h_t.

The ratio lemmas suggest the drift of this difference is summable because the
error is controlled by a_t and c_t/h_t. If this summability closes, then

  m_t = eta log h_t + O(1)

and

  h_t = Theta(t^{1/(1+eta)}).

That is the final discrete-recursion gap.
