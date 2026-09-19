# Universal curvature audit for centered-local compression

## Posterior potential

With Gaussian prior variance s^2,

  F_t(theta)
    = ||theta||^2/(2s^2)
      + sum_{i<t} log(1+exp(-y_i theta^T x_i)).

Its Hessian is

  nabla^2 F_t(theta)
    = s^{-2} I
      + sum_{i<t} sigma(y_i theta^T x_i)
                    sigma(-y_i theta^T x_i) x_i x_i^T.

Every data term is PSD. Hence universally

  nabla^2 F_t(theta) >= s^{-2} I.

So the posterior is s^{-2}-strongly log-concave for every adversarial history.

## What this gives -- and what it does not

Strong log-concavity implies a dimension-scale concentration radius around an
appropriate center of order

  ||theta-theta_bar|| = O(s sqrt(d + log(1/tau)))

with high probability (up to standard constants/choice of center).

Crucially this radius does NOT shrink with t from the prior floor alone.

Thus the centered identity

  a^k-b^k=(a-b) sum_{r=0}^{k-1} a^{k-1-r} b^r

only replaces a global magnitude by a factor proportional to

  |(theta-theta_bar)^T x_i|,

which is O(s R sqrt(d+log(1/tau))) under the universal bound, not O(t^-1/2).

Summing over t historical factors can therefore still leave an O(t) scale.

Conclusion: prior strong convexity alone does NOT cancel the sequential
accumulation that broke the naive global TensorSketch argument.

## Data curvature

Define the local logistic curvature matrix

  H_t(theta)
    = s^{-2} I
      + sum_{i<t} w_i(theta) x_i x_i^T,

  w_i(theta)=sigma(y_i theta^T x_i)sigma(-y_i theta^T x_i) in (0,1/4].

Near a center theta_bar, local displacement is naturally measured in the
H_t(theta_bar) metric.

Directions with eigenvalue lambda have characteristic posterior radius roughly
lambda^{-1/2}. If informative non-saturated examples accumulate, lambda can
grow with t and centering becomes powerful.

But on separable/saturated histories, w_i can become tiny, so some eigenvalues
remain near the prior floor.

## Correct complexity parameter

The sketch theorem should not be stated only in terms of Euclidean dimension.
A natural local quantity is an effective curvature/leverage budget such as

  L_t = sum_{i<t} x_i^T H_t^{-1} x_i

or weighted variants

  Lw_t = sum_i w_i x_i^T H_t^{-1} x_i.

For H=s^{-2}I+sum_i w_i x_i x_i^T,

  sum_i w_i x_i^T H^{-1}x_i
    = tr(H^{-1}(H-s^{-2}I))
    = d - s^{-2} tr(H^{-1})
    <= d.

This exact identity is promising: WEIGHTED logistic leverage has a universal
dimension bound, even though unweighted leverage need not.

## New key question

Can centered log-cosh approximation/sketch error be expressed with the SAME
logistic curvature weights w_i?

If yes, the historical t factor may be replaced by a dimension-scale weighted
leverage budget <= d.

If no, the centered-local sketch route probably cannot yield a worst-case
poly(d,log T) theorem through this argument.

## Next target

Derive a curvature-weighted Taylor representation for

  h(theta^T x_i)-h(theta_bar^T x_i)

whose second/higher-order remainder is controlled by
  w_i(theta_bar) [x_i^T(theta-theta_bar)]^2
or an integrated analogue.

Note:
  h''(z) = (1/4) sech^2(z/2)
         = sigma(z)sigma(-z).

This is EXACTLY the logistic curvature weight.

That coincidence is the strongest structural signal found in this route.
