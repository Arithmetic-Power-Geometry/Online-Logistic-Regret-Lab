# Copyright (C) 2026 Mohammad Amir Khusru Akhtar
# Licensed under the Apache License, Version 2.0.
import numpy as np
from software.adaptive_localized import AdaptiveLocalizedEW1D

def test_adaptive_prediction_finite_and_state_fixed():
    a=AdaptiveLocalizedEW1D(B=4,degree=14,mode_grid=401,max_nodes=64)
    initial=a.state_size()
    rng=np.random.default_rng(3)
    for t in range(40):
        x=float(rng.uniform(-1,1))
        p=a.predict(x)
        assert 0<p<1
        assert a.last_nodes<=64
        a.update(x,1 if t%3 else -1)
        assert a.state_size()==initial
