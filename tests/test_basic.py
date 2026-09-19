import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import numpy as np

from online_logistic import GaussianLaplacePredictor, sigmoid


def test_sigmoid_symmetry():
    z = np.array([-3.0, -1.0, 0.0, 1.0, 3.0])
    s = sigmoid(z)
    assert np.allclose(s + sigmoid(-z), 1.0)


def test_gaussian_predictor_probability():
    alg = GaussianLaplacePredictor(3)
    p = alg.predict(np.array([1.0, 0.0, 0.0]))
    assert 0.0 < p < 1.0
    assert abs(p - 0.5) < 1e-10


def test_update_changes_state():
    alg = GaussianLaplacePredictor(1)
    x = np.array([1.0])
    before = alg.m.copy()
    alg.update(x, 1)
    assert not np.allclose(before, alg.m)
