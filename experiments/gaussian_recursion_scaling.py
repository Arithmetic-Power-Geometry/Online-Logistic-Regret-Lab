import json
import math
import pathlib
import sys

import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from online_logistic import GaussianLaplacePredictor


def run_one(T, eta):
    alg = GaussianLaplacePredictor(1, damping=eta)
    x = np.array([1.0])
    checkpoints = {2**k for k in range(5, int(math.log2(T)) + 1)}
    rows = []

    for t in range(1, T + 1):
        p = alg.predict(x)
        if t in checkpoints:
            tail = max(1e-300, 1.0 - p)
            rows.append({
                "t": t,
                "m": float(alg.m[0]),
                "h": float(alg.H[0,0]),
                "m_over_logt": float(alg.m[0] / math.log(t)),
                "logh_over_logt": float(math.log(alg.H[0,0]) / math.log(t)),
                "tail_exponent_effective": float(-math.log(tail) / math.log(t)),
                "tail": tail,
            })
        alg.update(x, 1)

    pred_a = eta / (eta + 1.0)
    pred_h = 1.0 / (eta + 1.0)
    return {
        "eta": eta,
        "predicted_mean_and_tail_exponent": pred_a,
        "predicted_precision_exponent": pred_h,
        "rows": rows,
    }


if __name__ == "__main__":
    out = {
        str(eta): run_one(131072, eta)
        for eta in [0.25, 0.5, 1.0]
    }
    print(json.dumps(out, indent=2))
