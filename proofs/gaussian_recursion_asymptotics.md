# Gaussian recursion asymptotics: all-positive stream

We analyze the implemented GaussianLaplacePredictor in d=1 on x_t=1, y_t=+1.

Let damping be eta in (0,1]. Write m_t for the Gaussian mean and h_t for precision.
The implementation updates

  c_t = sigma(m_t)(1-sigma(m_t)),
  h_{t+1} = h_t + c_t,

and

  m_{t+1}
  = m_t + eta * [1/(1+e^{m_t})] / h_{t+1}.

For large m_t,

  1/(1+e^{m_t}) = e^{-m_t}(1+o(1)),
  c_t = e^{-m_t}(1+o(1)).

Hence the asymptotic recursion is

  h_{t+1}-h_t ~ e^{-m_t},
  m_{t+1}-m_t ~ eta e^{-m_t}/h_t.

Dividing the increments suggests

  dm/dh ~ eta/h,

so

  m_t ~ eta log h_t + C.

Therefore

  e^{-m_t} ~ C' h_t^{-eta}.

Substitute into dh/dt:

  dh/dt ~ C' h^{-eta}.

Solving,

  h_t^{eta+1} ~ (eta+1) C' t,

hence

  h_t ~ K_h t^{1/(eta+1)}
  and
  m_t ~ [eta/(eta+1)] log t + K_m.

Thus the candidate mean exponent is

  a = eta/(eta+1).

For the implementation eta=0.5,

  a = 1/3.

This is the first analytic exponent candidate.

## Predictive tail

The predictor is not sigma(m_t); it is the Gaussian mixture

  p_t^G = E[sigma(Z_t)],
  Z_t ~ N(m_t, 1/h_t).

Since Var(Z_t)=1/h_t -> 0, a Taylor expansion gives

  1-p_t^G
  = E[1-sigma(Z_t)]
  = e^{-m_t}(1+o(1))

provided the vanishing-variance correction is controlled uniformly.

Therefore

  1-p_t^G ~ C t^{-eta/(eta+1)}.

For eta=0.5,

  1-p_t^G ~ C t^{-1/3},

and cumulative Gaussian loss obeys

  L_T^G = Theta(T^{1/(eta+1)}).

At eta=0.5 this is

  L_T^G = Theta(T^{2/3}).

## Comparison with exact EW

The saddle-point analysis gives the EW scale

  1-p_t^EW ~ W(sigma^2 t)/(sigma^2 t)
           ~ (log t)/(sigma^2 t),

so

  L_T^EW = Theta((log T)^2)

at the heuristic asymptotic level.

Thus the predicted separation is

  L_T^G - L_T^EW
  = Theta(T^{1/(eta+1)}) - Theta((log T)^2).

For eta=0.5 this becomes

  Theta(T^{2/3}) versus polylogarithmic EW.

## What is proved vs conjectural

The differential-equation derivation is not yet a proof. A rigorous theorem needs
comparison inequalities converting the discrete recursions into matching upper
and lower bounds:

  c1 t^{1/(eta+1)} <= h_t <= c2 t^{1/(eta+1)},
  a1 log t - C <= m_t <= a2 log t + C,

with a1,a2 converging to eta/(eta+1), plus a uniform control of the
Gaussian-mixture tail.

The next executable test checks the predicted slopes:
- log h_t / log t -> 1/(eta+1),
- m_t / log t -> eta/(eta+1),
- -log(1-p_t^G)/log t -> eta/(eta+1).
