# Copyright (C) 2026 Mohammad Amir Khusru Akhtar
# Licensed under the Apache License, Version 2.0.
import numpy as np
from benchmarks.compare_existing import OGD, ONS, seq, run_alg, best_comparator_loss

def test_sequences_bounded():
    X,y=seq(32,4,"random",1)
    assert np.all(np.linalg.norm(X,axis=1) <= 1.0000001)
    assert set(np.unique(y)).issubset({-1,1})

def test_ogd_ons_finite():
    X,y=seq(64,3,"separable",2)
    for alg in [OGD(3), ONS(3)]:
        loss,secs=run_alg(alg,X,y)
        assert np.isfinite(loss) and loss>=0 and secs>=0

def test_comparator_finite():
    X,y=seq(32,2,"alternating",3)
    c=best_comparator_loss(X,y,steps=50)
    assert np.isfinite(c) and c>=0
