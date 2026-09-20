# Copyright (C) 2026 Mohammad Amir Khusru Akhtar
# Licensed under the Apache License, Version 2.0.
import json, math, time
import numpy as np
from software.fixed_d import ExactGridEW1D, QuadratureLogCoshSurrogate1D

def ll(p,y):
    p=min(max(p,1e-12),1-1e-12); return -math.log(p if y>0 else 1-p)

rows=[]
for T in [128,256,512,1024]:
    rng=np.random.default_rng(23)
    xs=rng.uniform(-1,1,T); ys=np.where((np.arange(T)%11)<6,1,-1)
    for nodes in [16,24,32,48,64]:
        exact=ExactGridEW1D(B=5,n_grid=8001)
        q=QuadratureLogCoshSurrogate1D(B=5,R=1,degree=18,nodes=nodes)
        tax=0.; maxerr=0.; tq=0.
        for x,y in zip(xs,ys):
            pe=exact.predict(x)
            s=time.perf_counter(); pq=q.predict(x); tq+=time.perf_counter()-s
            maxerr=max(maxerr,abs(pe-pq)); tax+=ll(pq,y)-ll(pe,y)
            exact.update(x,y); q.update(x,y)
        rows.append({"T":T,"nodes":nodes,"max_prediction_error":maxerr,
                     "loss_tax_vs_exact_grid_EW":tax,
                     "quadrature_us_per_round":1e6*tq/T,
                     "compressed_state_scalars":q.state_size()})
out={"quadrature":rows}
open("quadrature_results.json","w").write(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
