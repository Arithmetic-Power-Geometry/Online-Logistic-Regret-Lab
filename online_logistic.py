import math
import numpy as np


def sigmoid(z):
    z = np.asarray(z)
    out = np.empty_like(z, dtype=float)
    pos = z >= 0
    out[pos] = 1.0 / (1.0 + np.exp(-z[pos]))
    ez = np.exp(z[~pos])
    out[~pos] = ez / (1.0 + ez)
    return out


def logloss_from_prob(p, y):
    p = float(np.clip(p, 1e-15, 1 - 1e-15))
    return -math.log(p if y == 1 else 1 - p)


def logistic_loss(theta, x, y):
    z = float(np.dot(theta, x))
    a = -y * z
    return max(a, 0.0) + math.log1p(math.exp(-abs(a)))


class ProjectedOGD:
    def __init__(self, d, B, eta=0.5):
        self.theta = np.zeros(d)
        self.B = float(B)
        self.eta = float(eta)

    def predict(self, x):
        return float(sigmoid(np.array([self.theta @ x]))[0])

    def update(self, x, y):
        yz = y * float(self.theta @ x)
        grad = -y * x / (1.0 + math.exp(np.clip(yz, -60, 60)))
        self.theta -= self.eta * grad
        n = np.linalg.norm(self.theta)
        if n > self.B:
            self.theta *= self.B / n


class GaussianLaplacePredictor:
    """Research candidate, not a proven-regret algorithm.

    Maintains a Gaussian N(m, H^{-1}) approximation using damped online Newton
    updates and predicts E[sigma(theta^T x)] by Gauss-Hermite quadrature.
    """

    def __init__(self, d, prior_precision=1.0, damping=0.5, quadrature=24):
        self.d = d
        self.m = np.zeros(d)
        self.H = prior_precision * np.eye(d)
        self.damping = float(damping)
        self.nodes, self.weights = np.polynomial.hermite.hermgauss(quadrature)

    def variance_along(self, x):
        return float(x @ np.linalg.solve(self.H, x))

    def predict(self, x):
        mu = float(self.m @ x)
        var = max(self.variance_along(x), 0.0)
        z = mu + math.sqrt(2.0 * var) * self.nodes
        vals = sigmoid(z)
        return float(np.dot(self.weights, vals) / math.sqrt(math.pi))

    def update(self, x, y):
        z = float(self.m @ x)
        yz = y * z
        s = 1.0 / (1.0 + math.exp(np.clip(yz, -60, 60)))
        grad = -y * s * x
        p = float(sigmoid(np.array([z]))[0])
        curv = max(p * (1.0 - p), 1e-8)
        self.H += curv * np.outer(x, x)
        step = np.linalg.solve(self.H, grad)
        self.m -= self.damping * step
