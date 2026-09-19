# Asymptotic proof notebook: all-positive 1D stream

We study d=1, x_t=1, y_t=+1 for all t.

Let the EW prior be Gaussian N(0,sigma^2). Define

  Z_t = E_{theta~N(0,sigma^2)}[ sigma(theta)^t ].

The EW one-step probability of +1 at round t+1 is

  p_{t+1}^{EW} = Z_{t+1}/Z_t,

hence

  1-p_{t+1}^{EW} = 1 - Z_{t+1}/Z_t.

## A. Saddle-point equation for Z_t

Write the exponent

  F_t(theta) = t log sigma(theta) - theta^2/(2 sigma^2).

For large positive theta,

  log sigma(theta) = -log(1+e^{-theta})
                   = -e^{-theta} + O(e^{-2 theta}).

Thus the leading saddle solves

  d/dtheta[-t e^{-theta} - theta^2/(2 sigma^2)] = 0,

so

  t e^{-theta_t} = theta_t/sigma^2.

Equivalently,

  theta_t e^{theta_t} = sigma^2 t,

therefore

  theta_t = W(sigma^2 t),

where W is the Lambert-W function.

Using W(u)=log u - log log u + o(1),

  theta_t = log t - log log t + O(1).

At the saddle,

  e^{-theta_t} = theta_t/(sigma^2 t)
                = W(sigma^2 t)/(sigma^2 t).

This strongly suggests the EW wrong-label probability scale

  1-p_t^{EW} ~ W(sigma^2 t)/(sigma^2 t),

i.e. essentially (log t)/t rather than t^{-1-epsilon}.

IMPORTANT: this corrects the earlier empirical power-law interpretation.
A finite-window log-log fit can report an effective exponent >1 even when the
true asymptotic is (log t)/t.

Consequently the cumulative EW loss is expected to grow like

  sum_t (log t)/t = Theta((log T)^2),

not remain bounded.

Therefore the earlier hoped-for exponent crossing q_EW>1 is probably a finite-T
artifact and cannot be used as the LGSO theorem.

## B. Revised theorem target

The proper asymptotic comparison is now:

  EW tail:          ~(log t)/t
  Gaussian tail:    empirically much larger.

If the Gaussian recursion can be proved to satisfy

  1-p_t^G >= c t^{-q},  q<1,

then

  L_T^G = Omega(T^{1-q}),

whereas

  L_T^EW = O((log T)^2).

That still yields a polynomial-vs-polylog separation:

  Tax_T = Omega(T^{1-q}).

This is sufficient to refute O(poly(d) log T) approximation tax for the local
Gaussian recursion.

## C. What must be made rigorous

1. Establish two-sided saddle bounds for Z_t showing

   c1 W(sigma^2 t)/(sigma^2 t)
   <= 1-Z_{t+1}/Z_t
   <= c2 W(sigma^2 t)/(sigma^2 t)

   for all sufficiently large t.

2. Analyze the GaussianLaplacePredictor recursion. On y=+1:

   g_t = -1/(1+e^{m_t}),
   c_t = sigmoid(m_t)(1-sigmoid(m_t)),

   h_{t+1}=h_t+c_t,
   m_{t+1}=m_t + damping * [1/(1+e^{m_t})]/h_{t+1}.

3. Prove asymptotics for m_t and h_t, then convert to the Gaussian-mixture
   predictive tail.

The key correction is conceptual: exact EW itself is not bounded-loss on this
stream under a fixed Gaussian prior; its tail is expected to be ~log(t)/t.
The obstruction theorem only needs the Gaussian approximation to decay
strictly slower than 1/t up to logarithmic factors.
