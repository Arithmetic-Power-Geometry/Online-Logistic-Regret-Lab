# Benchmark snapshot

Copyright (C) 2026 Mohammad Amir Khusru Akhtar. Licensed under Apache-2.0.

Local validation of `benchmarks/compare_existing.py` on the benchmark matrix
T in {128,256,512,1024}, d in {2,5,10}, and sequences
{random,separable,alternating} produced the following aggregate values.

| T | Algorithm | Mean regret | Median regret | Mean us/round | Max regret |
|---:|---|---:|---:|---:|---:|
| 128 | OGD | 10.5121 | 8.7882 | 10.90 | 19.3615 |
| 128 | ONS | 7.1499 | 6.3221 | 18.70 | 15.5316 |
| 256 | OGD | 15.0088 | 17.4449 | 9.62 | 20.6630 |
| 256 | ONS | 7.8345 | 7.2585 | 19.67 | 16.2154 |
| 512 | OGD | 23.9777 | 20.3006 | 9.44 | 35.2382 |
| 512 | ONS | 8.6376 | 8.3199 | 17.92 | 17.1196 |
| 1024 | OGD | 42.8402 | 34.9374 | 9.34 | 70.5048 |
| 1024 | ONS | 9.6190 | 10.2391 | 18.27 | 18.0646 |

Interpretation:
- ONS is stronger than OGD on this small synthetic matrix but is roughly twice
  as expensive per round in this implementation.
- These numbers validate the harness only; they are not empirical measurements
  of AIOLI, Foster et al., or Di Gennaro et al.
- Published algorithms are compared separately by their stated theoretical
  regret and complexity.

Published-theory reference points:
- Foster et al. (COLT 2018): improper logistic regression; positive resolution
  to a variant of the 2012 open problem.
- Jezequel et al. (COLT 2020): O(B log(BT)) regret and O(d^2+log T)
  per-round computation.
- Di Gennaro et al. (AISTATS 2026): O(d log(BT)) regret for Gaussian-prior EW
  with total worst-case complexity \tilde O(B^3 T^5).
