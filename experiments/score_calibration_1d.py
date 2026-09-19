import json
import math
import pathlib
import sys

import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from online_logistic import ExactGridBayes1D, GaussianLaplacePredictor, logloss_from_prob


def posterior_mean(exact):
    return float(np.dot(exact.w, exact.theta))


def sequence(kind, T):
    if kind == "all_plus":
        return [1] * T
    if kind == "alternating":
        return [1 if t % 2 == 0 else -1 for t in range(T)]
    if kind == "half_reversal":
        return [1] * (T // 2) + [-1] * (T - T // 2)
    if kind == "blocks":
        out = []
        sign = 1
        block = 1
        while len(out) < T:
            out.extend([sign] * min(block, T - len(out)))
            sign *= -1
            block *= 2
        return out
    raise ValueError(kind)


def run(kind, T=4096, prior_var=25.0):
    exact = ExactGridBayes1D(prior_var=prior_var, grid_radius=20.0, grid_size=30001)
    gauss = GaussianLaplacePredictor(1, prior_precision=1.0/prior_var, damping=0.5)
    nplus = 0
    exact_identity_err = 0.0
    tax_plain = 0.0
    tax_score = 0.0

    ys = sequence(kind, T)
    for t, y in enumerate(ys, start=1):
        x = np.array([1.0])

        p_exact = exact.predict(x)
        p_plain = gauss.predict(x)

        if t == 1:
            p_score = 0.5
        else:
            # Posterior after t-1 observations.
            mu_hat = float(gauss.m[0])
            p_score = nplus/(t-1) - mu_hat/(prior_var*(t-1))
            p_score = float(np.clip(p_score, 1e-12, 1-1e-12))

            mu_exact = posterior_mean(exact)
            p_from_exact_mean = nplus/(t-1) - mu_exact/(prior_var*(t-1))
            exact_identity_err = max(exact_identity_err, abs(p_from_exact_mean-p_exact))

        tax_plain += logloss_from_prob(p_plain, y) - logloss_from_prob(p_exact, y)
        tax_score += logloss_from_prob(p_score, y) - logloss_from_prob(p_exact, y)

        if y == 1:
            nplus += 1
        exact.update(x, y)
        gauss.update(x, y)

    return {
        "kind": kind,
        "T": T,
        "max_exact_score_identity_error": exact_identity_err,
        "plain_gaussian_tax": tax_plain,
        "score_calibrated_gaussian_mean_tax": tax_score,
    }


if __name__ == "__main__":
    out = [run(k) for k in ["all_plus", "alternating", "half_reversal", "blocks"]]
    print(json.dumps(out, indent=2))
