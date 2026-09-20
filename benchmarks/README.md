# Benchmark protocol

Copyright (C) 2026 Mohammad Amir Khusru Akhtar. Licensed under Apache-2.0.

This benchmark intentionally separates **implemented baselines** from **published theoretical baselines**.

Implemented:
- OGD: projected online gradient descent.
- ONS: a compact online-Newton baseline using a rank-one Hessian surrogate.

Published theory comparison:
- Foster et al. (COLT 2018): improper online logistic regression; positive resolution to a variant of the 2012 open problem.
- Jézéquel, Gaillard, Rudi (COLT 2020): O(B log(BT)) regret, O(d^2 + log T) per round.
- Di Gennaro, Chakraborty, Zhivotovskiy (AISTATS 2026): near-optimal O(d log(BT)) regret for Gaussian-prior EW, with total worst-case complexity \tilde O(B^3 T^5).

We do not report empirical runtime for those published algorithms unless their exact implementation is included. This avoids misleading comparisons.

Run:

    python benchmarks/compare_existing.py

Output:

    benchmark_results.json
