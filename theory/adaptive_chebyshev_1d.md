# Geometric adaptive Chebyshev cover in 1D

We use the adaptive analytic tube derived from:
1. exact complex logistic curvature ratio;
2. curvature-height coupling.

Work in delta=theta-theta_hat on one side; the other side is symmetric in the
argument.

Let the relevant real interval be [0,D_t], where strong-convexity truncation
gives
  D_t=O(s sqrt(log t))
or is clipped by the bounded domain.

Let the near-mode scale be
  r0 = c0 / sqrt(H0),
H0=F''(theta_hat).

## Geometric partition

Define intervals
  I_0=[0,r0],
  I_j=[2^{j-1}r0, 2^j r0]
until reaching min(D_t,1/R).

Beyond 1/R, use intervals of fixed real length c/R (or geometric intervals
with tube width saturated at c/R) until D_t.

### Number of inner geometric intervals

The inner count is

  J1 <= log_2((1/R)/r0)+O(1)
     = O(log(1+sqrt(H0)/R)).

Since H0<=alpha+tR^2/4=O(t) for fixed parameters,

  J1=O(log t).

### Number of outer intervals

D_t=O(s sqrt(log t)).
With fixed length Theta(1/R), the outer count is

  J2=O(R s sqrt(log t))=O(sqrt(log t))

for fixed R,s.

Therefore total intervals
  J=O(log t).

## Ellipse fit

On an inner interval I_j with real length L_j=Theta(delta_j), the adaptive
tube half-width is eta>=c delta_j, so the ratio
  eta/L_j >= c'
is a constant.

Thus each inner interval admits a Bernstein ellipse with parameter rho>1
bounded away from 1 uniformly in t.

Near mode I_0 has real length r0 and tube width Theta(r0), again constant
aspect ratio.

Outer intervals have real length Theta(1/R) and saturated tube width
Theta(1/R), also constant aspect ratio.

Hence EVERY piece has a Bernstein ellipse with a common
  rho_*>1
depending only on fixed problem constants/tube safety factors, not t.

## Complex magnitude

By the curvature-height plus sec^2 argument, on each allowed ellipse/tube,

  |exp(-(F(z)-F(theta_hat)))|
  <= C exp(-kappa DeltaF(real anchor))

up to fixed constants.

In particular a global safe supremum M_j on each piece is at most a fixed
constant for near pieces and decays with potential height for far pieces.

For the prediction numerator, multiply by logistic likelihood. Staying a
fixed fraction away from its poles gives another fixed multiplicative bound.

Thus take
  M_j <= M_*
with M_* independent of t, under the exact-potential tube construction.

## Chebyshev error per interval

For a function analytic in Bernstein ellipse E_rho with sup M,

  ||f-p_n||_infty
  <= 2M rho^{-n}/(rho-1).

Choose local uniform error
  eps_j = t^{-p}/J
for fixed p>d+2 safety.

Since J=O(log t),

  n_j
   = O(log(M_* J t^p))
   = O(log t).

## Integral error

Interval integration error is bounded by interval length times uniform
approximation error. Summing over J pieces gives at most
  O(D_t t^{-p})
up to log factors.

Since D_t=O(sqrt(log t)), increase p by a fixed margin to achieve required
absolute error t^{-C_d}.

## Total 1D node count

J=O(log t) intervals,
n=O(log t) nodes/degree each.

Therefore

  N_1D = O(log^2 t)

up to fixed constants and possibly an extra sqrt(log t) dominated by log t.

This is POLYLOGARITHMIC.

## Tail error

Choose D_t via strong convexity and the polynomial denominator lower bound so
that omitted posterior mass/numerator contribution is <=t^{-p}. This was
proved separately.

Thus total integration error is polynomially small with O(log^2 t) analytic
function evaluations in 1D.

## Important implementation issue

The exact potential F(theta) cannot be evaluated from the compressed moment
state without history.

But the polynomial surrogate Fhat CAN be evaluated from the moment state.

The analytic tube proof above used exact logistic identities for F. To obtain
an algorithm, we need transfer the tube/curvature-height properties to Fhat.

Two options:
A. evaluate/integrate exact F using a coreset/history -- defeats compression;
B. prove the convexity-preserving surrogate is sufficiently close in
   function/curvature on the bounded domain that the same tube geometry holds.

Uniform curvature approximation r_m≈h'' gives precisely such a transfer:
  Fhat'' = prior + sum_i r_m(theta x_i)x_i^2.
But per-factor curvature error accumulates as t eps_curv. To keep relative
geometry in saturated low-curvature regions may require very small error.

For integration, an absolute Hessian error O(1) is enough because the prior
curvature alpha>0 provides a floor. It suffices to choose per-factor curvature
error
  eps_curv=O(1/t).

Our regret potential approximation already targets per-factor function error
O(1/t^2), obtainable from curvature approximation O(1/t^2) (fixed B,R), which
is stronger.

Then aggregate Hessian error is O(1/t), hence negligible relative to alpha.

Therefore:
  ||Fhat''-F''|| <= O(1/t)
uniformly on bounded Theta,
provided the curvature approximation is uniform and feature norms are fixed.

Similarly aggregate function error is O(1/t).

This transfers strong convexity and curvature comparisons up to constants.

## 1D theorem status

Under bounded domain, quadratic/interior-compatible prior handling, and the
curvature-first polynomial surrogate with per-factor curvature error
O(t^-2):

- truncation/tail: closed;
- adaptive analytic tube: closed for exact F and stable under O(1/t)
  aggregate C^2 perturbation;
- geometric interval cover: O(log t);
- Chebyshev degree per interval: O(log t);
- total deterministic quadrature nodes: O(log^2 t);
- required absolute error polynomially small.

This is now a credible 1D polylog integration theorem skeleton.

Remaining before paper gate:
1. write perturbation-transfer lemma carefully;
2. extend the adaptive cover to fixed d (tensor-product of 1D conditional
   slices is not automatic because cross-directions couple);
3. finite precision/mode computation can be stated separately.

Do NOT claim fixed-d theorem yet; 1D is essentially closed.
