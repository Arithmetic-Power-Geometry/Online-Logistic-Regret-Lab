import json
import numpy as np
from numpy.polynomial import Chebyshev, Polynomial


def R(u, k):
    a = np.power(u, k)
    b = np.power(1.0-u, k)
    return a / (a+b)


def fit_error(k, degree, grid_n=20001):
    # Chebyshev least-squares fit on a dense grid; diagnostic only, not a
    # certified minimax approximation.
    u = np.linspace(0.0, 1.0, grid_n)
    y = R(u, k)
    ch = Chebyshev.fit(u, y, degree, domain=[0.0, 1.0])
    pred = ch(u)
    return float(np.max(np.abs(pred-y)))


if __name__ == "__main__":
    out = {}
    for k in [1, 2, 4, 8, 16, 32, 64]:
        rows = []
        for degree in [2, 4, 8, 16, 32, 64, 128]:
            rows.append({
                "degree": degree,
                "max_grid_error": fit_error(k, degree),
            })
        out[str(k)] = rows
    print(json.dumps(out, indent=2))
