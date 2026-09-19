# Matched-moment obstruction: certification protocol

A numerical nearest pair is NOT itself evidence of a theorem. A candidate pair
(H,H') must pass all of the following before it is promoted.

## C1. Reachability
Both posteriors must be generated from the same stated prior by finite valid
online-logistic histories.

## C2. Full state matching
For order r, compare every raw monomial moment

  E[theta_1^a theta_2^b],  1 <= a+b <= r,

not only moments along the final query direction.

Report both:
- absolute coordinatewise mismatch;
- normalized Euclidean mismatch.

## C3. Predictive separation
For query x=e1 report

  Delta = |E_H sigma(theta_1)-E_H' sigma(theta_1)|.

A useful pair requires Delta to materially exceed numerical integration error
and to dominate the state mismatch at the intended accuracy scale.

## C4. Grid certification
Recompute the SAME pair at increasing (radius,resolution), e.g.
  (5,101), (6,161), (7,241), (8,321).
The prediction gap and moment differences must stabilize.

## C5. Accuracy relevance
Compare Delta with t^-2, where t is the larger history length plus one.
A counterexample relevant to our regret bridge should have Delta >> t^-2 while
the compressed-state mismatch is small enough that a stable state-based
predictor could not reliably distinguish the pair.

## C6. From approximate matching to theorem
Approximate numerical matching is insufficient for an impossibility theorem.
Need one of:
- an exact symmetry giving identical moments;
- a continuous parameter family plus intermediate-value/topological argument
  forcing exact matching;
- a quantitative stability lower bound showing eta-close states still force
  Delta-separated predictions for the specified compressor class.

## C7. Generalization
r=2 or r=3 only establishes failure of those fixed orders. A paper-level
hierarchy theorem needs a construction or argument for arbitrary fixed r, or
a quantitative lower bound on r as a function of required predictive accuracy.

## Stop rule
If the initial search plus ONE expanded dictionary fails to produce a
certifiable pair, stop this obstruction route. Do not endlessly enlarge the
search. Return to adaptive predictive bases/coresets.
