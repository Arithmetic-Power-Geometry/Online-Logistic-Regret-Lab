import json
import math
import pathlib
import sys

import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from online_logistic import ExactGridBayes1D, GaussianLaplacePredictor


def run_one(T, prior_var):
    exact = ExactGridBayes1D(prior_var=prior_var, grid_radius=20.0, grid_size=30001)
    gauss = GaussianLaplacePredictor(1, prior_precision=1.0 / prior_var)
    x = np.array([1.0])
    rows = []
    checkpoints = {2**k for k in range(5, int(math.log2(T)) + 1)}

    for t in range(1, T + 1):
        pe = exact.predict(x)
        pg = gauss.predict(x)

        if t in checkpoints:
            rows.append({
                "t": t,
                "exact_tail": 1.0 - pe,
                "gaussian_tail": 1.0 - pg,
                "gaussian_mean": float(gauss.m[0]),
                "gaussian_precision": float(gauss.H[0, 0]),
            })

        exact.update(x, 1)
        gauss.update(x, 1)

    def fit(key):
        pts = [(math.log(r["t"]), math.log(r[key])) for r in rows[-5:] if r[key] > 0]
        xs = np.array([p[0] for p in pts])
        ys = np.array([p[1] for p in pts])
        slope, intercept = np.polyfit(xs, ys, 1)
        return {"q": float(-slope), "intercept": float(intercept)}

    return {"prior_var": prior_var, "rows": rows, "exact_fit": fit("exact_tail"), "gaussian_fit": fit("gaussian_tail")}


if __name__ == "__main__":
    out = {
        str(v): run_one(16384, v)
        for v in [1.0, 4.0, 9.0, 25.0, 100.0]
    }
    print(json.dumps(out, indent=2))
