# Final invariant calculation for the Gaussian recursion

We continue with

  a_t = 1/(1+e^{m_t}),
  c_t = a_t(1-a_t),
  h_{t+1}=h_t+c_t,
  m_{t+1}=m_t+eta a_t/h_{t+1}.

Define

  D_t = m_t - eta log h_t.

Then exactly

  D_{t+1}-D_t
  = eta a_t/h_{t+1} - eta log(h_{t+1}/h_t)
  = eta a_t/h_{t+1} - eta log(1+c_t/h_t).

Let u_t=c_t/h_t. Since h_t->infinity and 0<c_t<=1/4, u_t->0.

Use the standard inequalities, valid for sufficiently small u>=0,

  u - u^2/2 <= log(1+u) <= u.

Also

  a_t/h_{t+1}
  = a_t/[h_t(1+u_t)]
  = (a_t/h_t)(1-u_t+O(u_t^2)).

Because c_t=a_t(1-a_t),

  u_t = a_t(1-a_t)/h_t.

Hence

  a_t/h_t - u_t
  = a_t^2/h_t.

Therefore the leading mismatch between the two terms is of order

  a_t^2/h_t + a_t u_t/h_t + u_t^2
  = O(a_t^2/h_t + a_t^2/h_t^2).

So for large t,

  |D_{t+1}-D_t| <= C eta [a_t^2/h_t + a_t^2/h_t^2].

Using the exponent-level laws already derived,

  h_t = t^{1/(1+eta)+o(1)},
  a_t = h_t^{-eta+o(1)},

we get

  a_t^2/h_t
  = t^{-(2eta+1)/(1+eta)+o(1)}.

The exponent

  (2eta+1)/(1+eta)

is strictly greater than 1 for every eta>0. Therefore

  sum_t a_t^2/h_t < infinity

up to the usual epsilon-slack needed to convert o(1) exponents into a rigorous
comparison. The h_t^{-2} term is even smaller.

This makes the drift of D_t absolutely summable and strongly suggests

  D_t -> D_infinity,

hence

  m_t = eta log h_t + D_infinity + o(1).

Once this limit is made rigorous with epsilon-slack, we obtain

  e^{-m_t} = e^{-D_infinity} h_t^{-eta}(1+o(1)).

Substituting into

  h_{t+1}-h_t
  = a_t(1-a_t)
  = e^{-m_t}(1+o(1))

gives the regularly varying recursion

  h_{t+1}-h_t
  = K h_t^{-eta}(1+o(1)),

K=e^{-D_infinity}>0.

By Stolz-Cesaro (or standard regularly-varying difference equations),

  h_t^{eta+1}/t -> (eta+1)K,

so

  h_t ~ [((eta+1)K)t]^{1/(eta+1)}.

Consequently

  m_t
  = eta/(eta+1) log t + O(1),

and

  e^{-m_t}
  = Theta(t^{-eta/(eta+1)}).

## Gaussian-mixture predictive tail

Let Z_t ~ N(m_t,1/h_t). Then

  1-p_t^G = E[1-sigma(Z_t)].

For large positive z,

  e^{-z}/(1+e^{-z}) <= 1-sigma(z) <= e^{-z}.

The upper bound gives

  1-p_t^G <= E[e^{-Z_t}]
           = exp(-m_t + 1/(2h_t)).

For a lower bound, on the event Z_t>=0,

  1-sigma(Z_t)
  = e^{-Z_t}/(1+e^{-Z_t})
  >= (1/2)e^{-Z_t}.

Since m_t sqrt(h_t)->infinity, P(Z_t<0) is super-polynomially small. Therefore

  E[e^{-Z_t} 1{Z_t>=0}]
  = exp(-m_t+1/(2h_t))(1-o(1)).

Hence

  1-p_t^G
  = Theta(exp(-m_t))
  = Theta(t^{-eta/(eta+1)}).

Therefore the Gaussian cumulative loss on the all-positive stream is

  L_T^G
  = Theta(T^{1/(eta+1)}).

This is the intended theorem for the SPECIFIC implemented GaussianLaplacePredictor.
It is not yet a class-wide impossibility result for all local Gaussian-state algorithms.
