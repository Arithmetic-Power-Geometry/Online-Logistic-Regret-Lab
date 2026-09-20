# Copyright (C) 2026 Mohammad Amir Khusru Akhtar
# Licensed under the Apache License, Version 2.0.
import numpy as np
from software.fixed_d import (GaussianPriorGridEW1D, score_prediction_from_mean,
                              fit_even_logcosh_chebyshev, LogCoshMomentSurrogate1D)

def test_score_identity_repeated_direction():
    ew=GaussianPriorGridEW1D(s=1.0,B=10,n_grid=12001)
    pos=neg=0
    for t in range(80):
        if t:
            p=ew.predict(1.0)
            q=score_prediction_from_mean(pos,neg,ew.mean(),1.0)
            assert abs(p-q)<3e-4
        y=1 if t%3 else -1
        ew.update(1.0,y)
        pos+=y>0; neg+=y<0

def test_even_logcosh_fit_improves_with_degree():
    z=np.linspace(-4,4,4001)
    h=np.logaddexp(z/2,-z/2)-np.log(2)
    e6=np.max(np.abs(fit_even_logcosh_chebyshev(4,6)(z)-h))
    e14=np.max(np.abs(fit_even_logcosh_chebyshev(4,14)(z)-h))
    assert e14 < e6

def test_update_closed_state():
    s=LogCoshMomentSurrogate1D(B=3,R=1,degree=8,n_grid=501)
    xs=[.2,-.7,.5]; ys=[1,-1,1]
    for x,y in zip(xs,ys): s.update(x,y)
    assert s.n==3
    assert abs(s.b-sum(x*y for x,y in zip(xs,ys)))<1e-12
    for k in range(2,9,2):
        assert abs(s.moments[k]-sum(x**k for x in xs))<1e-12
    assert 0 < s.predict(.4) < 1
