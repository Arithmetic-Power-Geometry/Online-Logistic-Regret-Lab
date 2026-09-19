import json
import numpy as np


def ambiguity_example():
    # d=1, r=2 dependent dictionary v1=1, v2=2.
    V = np.array([[1.0, 2.0]])
    # Choose counts allowing an interior predictive vector.
    nplus = np.array([5.0, 5.0])
    n = np.array([10.0, 10.0])
    # Pick mu/s^2 = 0 for the algebraic test.
    rhs = np.array([0.0])

    a0 = np.linalg.pinv(V) @ rhs
    # Kernel vector for [1,2].
    z = np.array([2.0, -1.0])
    assert np.allclose(V @ z, 0.0)

    feasible = []
    for alpha in np.linspace(-2.0, 2.0, 17):
        a = a0 + alpha * z
        p = (nplus - a) / n
        if np.all((p > 0.0) & (p < 1.0)):
            feasible.append({
                "alpha": float(alpha),
                "p1": float(p[0]),
                "p2": float(p[1]),
                "score_residual": float(np.linalg.norm(V @ a-rhs)),
            })

    return {
        "V": V.tolist(),
        "rank": int(np.linalg.matrix_rank(V)),
        "r": 2,
        "score_nullity": 2-int(np.linalg.matrix_rank(V)),
        "num_distinct_feasible_predictive_vectors": len(feasible),
        "examples": feasible,
    }


if __name__ == "__main__":
    print(json.dumps(ambiguity_example(), indent=2))
