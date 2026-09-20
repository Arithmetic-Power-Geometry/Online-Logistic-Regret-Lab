# Copyright (C) 2026 Mohammad Amir Khusru Akhtar
# Licensed under the Apache License, Version 2.0.
import json, math, time
import numpy as np
from software.fixed_d import GaussianPriorGridEW1D, score_prediction_from_mean, ExactGridEW1D, LogCoshMomentSurrogate1D

def ll(p,y):
    p=min(max(p,1e-12),1-1e-12)
    return -math.log(p if y>0 else 1-p)

def repeated_score_test(T=512,s=1.0):
    ew=GaussianPriorGridEW1D(s=s)
    npat=[("all_plus",lambda t:1),("alternating",lambda t:1 if t%2==0 else -1),
          ("blocks",lambda t:1 if (t//16)%2==0 else -1)]
    out=[]
    for name,fn in npat:
        ew=GaussianPriorGridEW1D(s=s); pos=neg=0; maxerr=0.0
        for t in range(T):
            if t>0:
                p=ew.predict(1.0); ps=score_prediction_from_mean(pos,neg,ew.mean(),s)
                maxerr=max(maxerr,abs(p-ps))
            y=fn(t); ew.update(1.0,y)
            if y>0: pos+=1
            else: neg+=1
        out.append({"case":name,"T":T,"max_score_identity_error":maxerr})
    return out

def surrogate_test():
    rows=[]
    for T in [64,128,256,512]:
      for degree in [6,10,14,18]:
        exact=ExactGridEW1D(B=5,n_grid=4001)
        sur=LogCoshMomentSurrogate1D(B=5,R=1,degree=degree,n_grid=4001)
        tax=0.; maxpe=0.
        rng=np.random.default_rng(17)
        # changing magnitudes makes moment state nontrivial
        xs=rng.uniform(-1,1,T); ys=np.where(np.arange(T)%7<4,1,-1)
        t0=time.perf_counter()
        for x,y in zip(xs,ys):
            pe=exact.predict(x); ps=sur.predict(x)
            maxpe=max(maxpe,abs(pe-ps)); tax+=ll(ps,y)-ll(pe,y)
            exact.update(x,y); sur.update(x,y)
        secs=time.perf_counter()-t0
        rows.append({"T":T,"degree":degree,"max_prediction_error":maxpe,
                     "loss_tax_vs_exact_grid_EW":tax,"state_scalars":sur.state_size(),
                     "seconds_joint":secs})
    return rows

def main():
    out={"score_identity":repeated_score_test(),"surrogate":surrogate_test()}
    with open("software_results.json","w") as f: json.dump(out,f,indent=2)
    print(json.dumps(out,indent=2))
if __name__=="__main__": main()
