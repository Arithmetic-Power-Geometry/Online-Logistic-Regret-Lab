import itertools
import json
import math
import numpy as np

from online_logistic import GaussianLaplacePredictor, ProjectedOGD, logloss_from_prob


def run_sequence(xs, ys, alg):
    loss = 0.0
    trajectory = []
    for x, y in zip(xs, ys):
        p = alg.predict(x)
        loss += logloss_from_prob(p, y)
        trajectory.append((p, loss))
        alg.update(x, y)
    return loss, trajectory


def best_1d_comparator(xs, ys, B, grid=4001):
    thetas = np.linspace(-B, B, grid)
    losses = np.zeros_like(thetas)
    for x, y in zip(xs, ys):
        z = thetas * float(x[0])
        a = -y * z
        losses += np.maximum(a, 0) + np.log1p(np.exp(-np.abs(a)))
    i = int(np.argmin(losses))
    return float(losses[i]), float(thetas[i])


def exhaustive_1d(T=10, B=5.0):
    xs = [np.array([1.0])] * T
    worst = None
    for ys_tuple in itertools.product([-1, 1], repeat=T):
        ys = list(ys_tuple)
        best_loss, theta_star = best_1d_comparator(xs, ys, B)
        cand_loss, _ = run_sequence(xs, ys, GaussianLaplacePredictor(1))
        regret = cand_loss - best_loss
        row = {
            "T": T,
            "ys": ys,
            "candidate_loss": cand_loss,
            "best_loss": best_loss,
            "theta_star": theta_star,
            "regret": regret,
        }
        if worst is None or regret > worst["regret"]:
            worst = row
    return worst


def structured_sequences(T):
    seqs = {}
    seqs["all_plus"] = [1] * T
    seqs["all_minus"] = [-1] * T
    seqs["half_reversal"] = [1] * (T // 2) + [-1] * (T - T // 2)
    seqs["late_reversal"] = [1] * max(1, T - max(1, T // 10)) + [-1] * max(1, T // 10)
    seqs["alternating"] = [1 if t % 2 == 0 else -1 for t in range(T)]
    return seqs


def benchmark(T=1000, B=5.0):
    xs = [np.array([1.0])] * T
    rows = []
    for name, ys in structured_sequences(T).items():
        best_loss, theta_star = best_1d_comparator(xs, ys, B)
        cand_loss, _ = run_sequence(xs, ys, GaussianLaplacePredictor(1))
        ogd_loss, _ = run_sequence(xs, ys, ProjectedOGD(1, B))
        rows.append({
            "name": name,
            "candidate_regret": cand_loss - best_loss,
            "ogd_regret": ogd_loss - best_loss,
            "best_theta": theta_star,
        })
    return rows


if __name__ == "__main__":
    out = {
        "exhaustive_T10": exhaustive_1d(T=10, B=5.0),
        "structured_T1000": benchmark(T=1000, B=5.0),
    }
    print(json.dumps(out, indent=2))
