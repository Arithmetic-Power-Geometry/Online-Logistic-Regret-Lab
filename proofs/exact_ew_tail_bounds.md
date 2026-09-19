# Exact EW tail bounds: theorem target

Let theta~N(0,sigma^2), and define

  Z_t = E[sigma(theta)^t].

Then the exact EW predictive probability of +1 on the all-positive stream is

  p_{t+1}^{EW}=Z_{t+1}/Z_t.

Thus

  1-p_{t+1}^{EW}
  = E_t[1-sigma(theta)],

where E_t denotes expectation under the tilted posterior density

  q_t(theta) proportional to sigma(theta)^t exp(-theta^2/(2 sigma^2)).

## Saddle location

Let

  F_t(theta)=t log sigma(theta)-theta^2/(2sigma^2).

Then

  F_t'(theta)
  = t(1-sigma(theta)) - theta/sigma^2.

The exact saddle theta_t solves

  t/(1+e^{theta_t}) = theta_t/sigma^2.

Equivalently,

  theta_t(1+e^{theta_t})=sigma^2 t.

For large t, theta_t->infinity and

  theta_t e^{theta_t}
  = sigma^2 t (1+o(1)),

so

  theta_t = W(sigma^2 t)+o(1).

At the saddle,

  1-sigma(theta_t)
  = theta_t/(sigma^2 t).

## Concentration target

Since

  F_t''(theta)
  = -t sigma(theta)(1-sigma(theta)) - 1/sigma^2 < 0,

F_t is globally strictly concave. At theta_t,

  -F_t''(theta_t)
  = t sigma(theta_t)(1-sigma(theta_t)) + 1/sigma^2
  = theta_t sigma(theta_t)/sigma^2 + 1/sigma^2
  = Theta(theta_t/sigma^2).

Hence posterior width is expected to be

  s_t = Theta(sigma/sqrt(theta_t)).

Because theta_t~log t, this width is o(theta_t), so the posterior lies in a
relative neighborhood of the saddle.

## Desired two-sided bound

For sufficiently large t, prove constants c1,c2>0 such that

  c1 * theta_t/(sigma^2 t)
  <= E_t[1-sigma(theta)]
  <= c2 * theta_t/(sigma^2 t).

Since theta_t~W(sigma^2 t), this yields

  1-p_{t+1}^{EW}
  = Theta(W(sigma^2 t)/(sigma^2 t)).

Then

  L_T^{EW}
  = Theta(sum_{t<=T} W(sigma^2 t)/t)
  = Theta((log T)^2).

## Elementary route to concentration

Fix a window

  I_t=[theta_t-r_t, theta_t+r_t],

with

  r_t = K sigma sqrt(log theta_t / theta_t).

Taylor expansion plus global log-concavity should give posterior mass outside I_t
at most theta_t^{-A} for K chosen large enough.

Inside I_t,

  1-sigma(theta)
  = (1-sigma(theta_t)) * exp(-(theta-theta_t)) * [1+small relative error].

Since r_t->0, this ratio is 1+o(1) uniformly on I_t.

Therefore posterior concentration would imply

  E_t[1-sigma(theta)]
  = (1-sigma(theta_t))(1+o(1))
  = theta_t/(sigma^2 t)(1+o(1)).

This is stronger than merely two-sided constants.

## Remaining proof obligation

Make the concentration estimate explicit using:
1. strict concavity of F_t;
2. a local quadratic lower bound on -F_t'' near theta_t;
3. a global tail bound from concavity outside the local window.

Once this is done, the exact EW side is closed.
