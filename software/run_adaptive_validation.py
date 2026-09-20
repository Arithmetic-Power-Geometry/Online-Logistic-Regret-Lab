# Copyright (C) 2026 Mohammad Amir Khusru Akhtar
# Licensed under the Apache License, Version 2.0.
import json, math, time
import numpy as np
from software.fixed_d import ExactGridEW1D
from software.adaptive_localized import AdaptiveLocalizedEW1D

def ll(p,y):
    p=min(max(float(p),1e-12),1-1e-12)
    return -math.log(p if y>0 else 1-p)

def make_seq(T,kind,seed=31):
    rng=np.random.default_rng(seed)
    if kind=="random":
        return rng.uniform(-1,1,T),rng.choice([-1,1],T)
    if kind=="alternating":
        return np.ones(T),np.where(np.arange(T)%2==0,1,-1)
    if kind=="blocks":
        return np.ones(T),np.where((np.arange(T)//16)%2==0,1,-1)
    if kind=="varying":
        x=rng.uniform(-1,1,T); y=np.where(np.arange(T)%7<4,1,-1); return x,y
    raise ValueError(kind)

def one(T,kind):
    x,y=make_seq(T,kind)
    exact=ExactGridEW1D(B=5,n_grid=8001)
    alg=AdaptiveLocalizedEW1D(B=5,R=1,degree=18,mode_grid=1001,
                             min_nodes=8,max_nodes=256,tol_scale=.05,tail_height=18)
    tax=0.; maxerr=0.; nodes=[]; widths=[]; secs=0.
    for xx,yy in zip(x,y):
        pe=exact.predict(xx)
        st=time.perf_counter(); pa=alg.predict(xx); secs+=time.perf_counter()-st
        maxerr=max(maxerr,abs(pe-pa)); tax+=ll(pa,yy)-ll(pe,yy)
        nodes.append(alg.last_nodes); widths.append(alg.last_interval[1]-alg.last_interval[0])
        exact.update(xx,yy); alg.update(xx,yy)
    return dict(T=T,sequence=kind,max_prediction_error=maxerr,
                loss_tax_vs_exact_EW=tax,mean_nodes=float(np.mean(nodes)),
                max_nodes=int(max(nodes)),mean_interval_width=float(np.mean(widths)),
                us_per_round=1e6*secs/T,state_scalars=alg.state_size())

def main():
    rows=[]
    for T in [128,256,512,1024,2048]:
        for kind in ["random","alternating","blocks","varying"]:
            rows.append(one(T,kind))
    with open("adaptive_results.json","w") as f: json.dump(rows,f,indent=2)
    print(json.dumps(rows,indent=2))
if __name__=="__main__": main()
