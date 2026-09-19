import json
import math
import pathlib
import sys

import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from online_logistic import ExactGridBayes1D, GaussianLaplacePredictor


def tail_series(T):
    exact = ExactGridBayes1D()
    gauss = GaussianLaplacePredictor(1)
    x = np.array([1.0])

    rows = []
    checkpoints = {2**k for k in range(4, int(math.log2(T)) + 1)}

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

    return rows


def fit_power(rows, key):
    xs = []
    ys = []
    for r in rows:
        val = r[key]
        if val > 0:
            xs.append(math.log(r["t"]))
            ys.append(math.log(val))
    x = np.array(xs[-4:])
    y = np.array(ys[-4:])
    slope, intercept = np.polyfit(x, y, 1)
    return {"slope": float(slope), "exponent_q": float(-slope), "intercept": float(intercept)}


if __name__ == "__main__":
    rows = tail_series(4096)
    print(json.dumps({
        "rows": rows,
        "exact_tail_fit": fit_power(rows, "exact_tail"),
        "gaussian_tail_fit": fit_power(rows, "gaussian_tail"),
    }, indent=2))
