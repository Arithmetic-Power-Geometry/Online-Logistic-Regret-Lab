import json
import math
import pathlib
import sys

import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from online_logistic import ExactGridBayes1D, MomentCorrectedGaussian1D, logloss_from_prob


def tax(ys, order):
    exact = ExactGridBayes1D()
    alg = MomentCorrectedGaussian1D(order=order)
    x = np.array([1.0])
    le = 0.0
    la = 0.0
    for y in ys:
        pe = exact.predict(x)
        pa = alg.predict(x)
        le += logloss_from_prob(pe, y)
        la += logloss_from_prob(pa, y)
        exact.update(x, y)
        alg.update(x, y)
    T = len(ys)
    return {
        "T": T,
        "order": order,
        "tax": la - le,
        "tax_over_log1pT": (la - le) / math.log1p(T),
        "alg_loss": la,
        "exact_loss": le,
    }


def run():
    out = {}
    for T in [32, 64, 128, 256, 512, 1024]:
        ys = [1] * T
        out[str(T)] = {str(k): tax(ys, k) for k in [1, 2, 3, 4, 6, 8]}
    return out


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
