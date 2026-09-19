import json
import math
import pathlib
import sys

import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from online_logistic import (
    ExactGridBayes1D,
    GaussianLaplacePredictor,
    SkewCorrectedGaussian1D,
    logloss_from_prob,
)


def tax_on_sequence(ys, alg):
    exact = ExactGridBayes1D()
    exact_loss = 0.0
    alg_loss = 0.0
    x = np.array([1.0])
    for y in ys:
        pe = exact.predict(x)
        pa = alg.predict(x)
        exact_loss += logloss_from_prob(pe, y)
        alg_loss += logloss_from_prob(pa, y)
        exact.update(x, y)
        alg.update(x, y)
    T = len(ys)
    tax = alg_loss - exact_loss
    return {
        "T": T,
        "tax": tax,
        "tax_over_log1pT": tax / math.log1p(T),
        "alg_loss": alg_loss,
        "exact_loss": exact_loss,
    }


def families(T):
    return {
        "all_plus": [1] * T,
        "late_reversal_1": [1] * (T - 1) + [-1],
        "half_reversal": [1] * (T // 2) + [-1] * (T - T // 2),
        "alternating": [1 if t % 2 == 0 else -1 for t in range(T)],
    }


def run():
    out = {}
    for T in [32, 64, 128, 256, 512, 1024]:
        out[str(T)] = {}
        for name, ys in families(T).items():
            out[str(T)][name] = {
                "gaussian": tax_on_sequence(ys, GaussianLaplacePredictor(1)),
                "skew": tax_on_sequence(ys, SkewCorrectedGaussian1D()),
            }
    return out


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
