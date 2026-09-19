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
            h = float(alg.H[0, 0])
            m = float(alg.m[0])
            rows.append({
                "t": t,
                "m_minus_eta_logh": m - eta * math.log(h),
                "tail_times_exp_m": (1.0 - p) * math.exp(m),
                "variance": 1.0 / h,
            })
        alg.update(x, 1)

    return {"eta": eta, "rows": rows}


if __name__ == "__main__":
    out = {str(e): run_one(131072, e) for e in [0.25, 0.5, 1.0]}
    print(json.dumps(out, indent=2))
