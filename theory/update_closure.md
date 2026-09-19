# Update-closure stress test

## Exact 1D moment update

Let u=sigma(theta) and let M_j=E[u^j] under the current posterior.

After a positive observation at the same direction, posterior density is
reweighted by u, so

  M_j^+ = M_{j+1}/M_1.

After a negative observation it is reweighted by 1-u, so

  M_j^- = (M_j-M_{j+1})/(1-M_1).

Therefore a stored vector (M_0,...,M_m) is not exactly update-closed:
updating M_m requires M_{m+1}.

## Important observation: finite-horizon exact closure by growing degree

If the horizon is T and we are willing to store moments through degree m+T,
then exact repeated-direction updates are possible for T future rounds. This is
linear in T and therefore unsuitable for the desired poly(log T) state.

## Approximate closure question

Can M_{m+1} be reconstructed from M_0,...,M_m with error small enough to
preserve the delta_t=O(t^-2) prediction schedule for every posterior reachable
from the allowed online process?

For arbitrary probability measures on [0,1], truncated moments do not uniquely
determine the next moment. The feasible interval for M_{m+1} is a classical
truncated moment problem.

But reachable logistic posteriors form a much narrower family than arbitrary
measures. Any impossibility claim must therefore construct TWO reachable
posteriors with nearly identical stored moments but sufficiently different
next moments/predictions.

This is the next adversarial target.

## Candidate lower-bound template

For a chosen compression order m:

1. Construct two online histories H and H' that produce reachable posteriors
   Q,Q'.
2. Match/approximately match their compressed state:
      |M_j(Q)-M_j(Q')| <= eta, j<=m.
3. Ensure the next required quantity differs:
      |M_{m+1}(Q)-M_{m+1}(Q')| >= Delta,
   or produce a next direction x for which
      |E_Q sigma(theta^T x)-E_Q' sigma(theta^T x)| >= Delta.
4. Choose Delta large relative to the O(t^-2) accuracy needed for logarithmic
   approximation tax.
5. Conclude that this moment-compression class cannot guarantee the desired
   tax with state order m.

This would be a meaningful class-specific obstruction, not a universal lower
bound for online logistic regression.

## Positive alternative

If reachable posterior structure forces a deterministic/stable recurrence
M_{m+1}=F(M_1,...,M_m)+small error with error decaying exponentially in m,
then choose m=O(log T) and obtain approximate update closure.

This is now the decisive fork.
