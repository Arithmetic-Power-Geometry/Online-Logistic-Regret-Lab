import json
import math
import pathlib
import sys

import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from online_logistic import ExactGridBayes1D, GaussianLaplacePredictor, logloss_from_prob


def compare_sequence(ys, x_value=1.0):
    exact = ExactGridBayes1D()
    gauss = GaussianLaplacePredictor(1)

    exact_loss = 0.0
    gauss_loss = 0.0
    leverage_sum = 0.0
    worst_one_step_tax = -1e100
    x = np.array([x_value], dtype=float)

    for y in ys:
        p_star = exact.predict(x)
        p_g = gauss.predict(x)

        l_star = logloss_from_prob(p_star, y)
        l_g = logloss_from_prob(p_g, y)
        one_tax = l_g - l_star

        exact_loss += l_star
        gauss_loss += l_g
        worst_one_step_tax = max(worst_one_step_tax, one_tax)

        lam = gauss.variance_along(x)
        leverage_sum += min(1.0, lam * lam)

        exact.update(x, y)
        gauss.update(x, y)

    T = len(ys)
    tax = gauss_loss - exact_loss
    return {
        "T": T,
        "tax": tax,
        "tax_over_log1pT": tax / math.log1p(T),
        "exact_loss": exact_loss,
        "gaussian_loss": gauss_loss,
        "leverage_sq_budget": leverage_sum,
        "worst_one_step_tax": worst_one_step_tax,
    }


def families(T):
    k10 = max(1, T // 10)
    k4 = max(1, T // 4)
    return {
        "all_plus": [1] * T,
        "half_reversal": [1] * (T // 2) + [-1] * (T - T // 2),
        "late_reversal_10pct": [1] * (T - k10) + [-1] * k10,
        "late_reversal_1": [1] * (T - 1) + [-1],
        "quarter_flip_quarter": [1] * (T - 2 * k4) + [-1] * k4 + [1] * k4,
        "alternating": [1 if t % 2 == 0 else -1 for t in range(T)],
    }


def run():
    out = {}
    for T in [32, 64, 128, 256, 512, 1024]:
        out[str(T)] = {name: compare_sequence(ys) for name, ys in families(T).items()}
    return out


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
