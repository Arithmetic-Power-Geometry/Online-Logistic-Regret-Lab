# Online Logistic Regret Lab

Falsification-first research lab for efficient online logistic regression.

## Core setting

For rounds t=1,...,T:
- x_t in R^d arrives with ||x_t||_2 <= 1.
- The learner outputs a probability p_t in (0,1), equivalently a logit z_t.
- y_t in {-1,+1} is revealed.
- Logistic/log loss is
  ell(z_t,y_t) = log(1 + exp(-y_t z_t)).

Comparator class:
  Theta_B = {theta in R^d : ||theta||_2 <= B}.

Regret:
  R_T(theta) = sum_t ell(z_t,y_t)
             - sum_t ell(<theta,x_t>,y_t).

## Known frontier

The raw target O(poly(d,B) log T) is already known in several forms.
The research target here is sharper:

> Can one achieve near-optimal O(d log(BT)) worst-case regret with genuinely
> lightweight sequential computation (ideally O(d^2) time and O(d^2) state per
> round), without exponential dependence on B?

If not, can we prove an obstruction for a broad class of compact posterior /
second-order approximations?

## Candidate direction: curvature-budgeted Gaussian aggregation

Maintain a Gaussian approximation q_t=N(m_t,H_t^{-1}) to the exponential-weights
posterior. Predict by the Gaussian mixture probability

  p_t = E_{theta~q_t}[sigma(<theta,x_t>)].

Update m_t by a damped Newton step on accumulated logistic loss plus Gaussian
regularization, and H_t by rank-one observed curvature.

The theorem attempt is not assumed true. We decompose regret as

  learner regret
  <= exact exponential-weights regret
   + cumulative approximation tax.

The key question is whether the approximation tax can be bounded by a
log-determinant / leverage budget rather than by T times a uniform error.

## Breakthrough gate

Do NOT claim a breakthrough unless all hold:
1. Exact assumptions are stated.
2. A theorem stronger than the known efficient O(B log(BT)) frontier is proved,
   or a meaningful impossibility result is proved.
3. The proof survives adversarial review.
4. Exhaustive / randomized counterexample searches fail to refute it.
5. Reproducible CI passes.
6. Literature search finds no equivalent prior result.

See THEORY.md and experiments/.


## Software benchmark and license

Copyright (C) 2026 Mohammad Amir Khusru Akhtar.

This repository is licensed under the Apache License, Version 2.0; see
`LICENSE` and `NOTICE`.

Reproducible software validation is provided by:

- `benchmarks/compare_existing.py`
- `tests/test_benchmarks.py`
- `.github/workflows/software-benchmark.yml`
- `benchmarks/BENCHMARK_SNAPSHOT.md`

Run locally:

```bash
pip install -r requirements.txt
pip install pytest
pytest -q
python benchmarks/compare_existing.py
```

The benchmark distinguishes implemented baselines from published theoretical
comparators. It does not attribute runtime measurements to external algorithms
unless their exact implementation is included.
