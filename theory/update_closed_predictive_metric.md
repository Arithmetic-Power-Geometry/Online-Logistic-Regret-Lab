# Predictive likelihood distortion under Bayes update

For distributions P,Q over theta and a likelihood class L, define
  d_L(P,Q)
   = sup_{L in class} |log E_P L - log E_Q L|.

For logistic one-step likelihoods,
  L_{x,y}(theta)=sigma(y theta^T x).

Question: if P and Q are close in d_L and both receive the SAME Bayes update
with likelihood A in L, are P^A and Q^A close in d_L?

Bayes update:
  P^A(dtheta)=A(theta)P(dtheta)/E_P A.

For a future likelihood B,

  E_{P^A} B = E_P[AB]/E_P[A].

Therefore

  log E_{P^A}B - log E_{Q^A}B
   = [log E_P(AB)-log E_Q(AB)]
     -[log E_P A-log E_Q A].

The second bracket is controlled by one-step d_L(P,Q).
The FIRST bracket involves the PRODUCT class L*L, not L.

Thus one-step predictive likelihood distortion is NOT closed under Bayes
updates.

## Hierarchy

After k future updates, relevant quantities are expectations of products

  E_P[ L_1 L_2 ... L_k ].

Define k-step path distortion

  d_k(P,Q)
   = sup_{L_1,...,L_k in L}
       | log E_P prod_{j=1}^k L_j
         - log E_Q prod_{j=1}^k L_j |.

Then a common Bayes update by A satisfies schematically

  d_k(P^A,Q^A) <= d_{k+1}(P,Q)+d_1(P,Q).

So closure requires a hierarchy of product-likelihood tests.

## Full future-path distortion

Define

  D_future(P,Q)
   = sup_{k>=1} sup_{L_1,...,L_k}
       |log E_P prod_j L_j - log E_Q prod_j L_j|.

This is update-stable up to normalization accounting, but is extremely strong:
it asks the compression to preserve evidence for every possible future
adversarial logistic sequence.

For finite horizon H, define D_H analogously for k<=H.

## Consequence for recompression

Preserving only the next predictive probability cannot guarantee that the
compressed posterior remains safe after arbitrary future updates.

This is the same structural phenomenon repeatedly encountered in the project:
decision/prediction equivalence for one query is not necessarily closed under
future interventions/updates.

## Possible escape

We do not need each compression to be safe for ALL future horizons if we
recompress every round. A dynamic potential could charge the newly created
higher-order distortion before it affects prediction.

But a static one-step metric is insufficient.

## Strong sufficient metric

Pointwise log-density-ratio control
  ||log(dP/dQ)-constant||_infinity <= rho
controls expectations of EVERY nonnegative future product and is closed under
common Bayes updates: multiplication by the same likelihood cancels in the
density ratio before renormalization.

Thus density-ratio oscillation is the natural update-closed metric.

Define
  osc(P,Q)
   = sup_theta log(dP/dQ)
     - inf_theta log(dP/dQ).

Under common Bayes update A,
the unnormalized ratio is unchanged; after normalization only a constant is
added, so

  osc(P^A,Q^A)=osc(P,Q).

This is an EXACT invariance.

Moreover if osc(P,Q)<=rho, after choosing a centering constant the predictive
log-evidence distortion for any nonnegative likelihood is at most rho
(up to a factor convention depending on centering).

## Breakthrough target sharpened

Construct an online compression family such that each recompression introduces
small density-ratio oscillation rho_t, while representation size remains
poly(d,B,log T), and cumulative introduced oscillation is O(log T).

Because common Bayes updates preserve oscillation exactly, compression errors
can then be accumulated without amplification.

This is a clean update-closed stability metric.

Problem:
uniform density-ratio oscillation is essentially uniform centered potential
error, which earlier looked too demanding. But now the required schedule may
be cumulative sum rho_t=O(log T), not rho_t=O(t^-2), a dramatically weaker
target.

Need derive exact cumulative theorem next.
