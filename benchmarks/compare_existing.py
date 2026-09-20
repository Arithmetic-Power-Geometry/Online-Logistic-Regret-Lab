# Copyright (C) 2026 Mohammad Amir Khusru Akhtar
# Licensed under the Apache License, Version 2.0.

import json, math, time
import numpy as np

try:
    from online_logistic import ExactGridBayes1D, GaussianLaplacePredictor
except Exception:
    ExactGridBayes1D = None
    GaussianLaplacePredictor = None

def logloss_prob(p, y):
    p=min(max(float(p),1e-12),1-1e-12)
    return -math.log(p if y>0 else 1-p)

class OGD:
    def __init__(self,d,eta=0.5,B=5.0):
        self.w=np.zeros(d); self.eta=eta; self.B=B
    def predict(self,x):
        z=float(self.w@x)
        return 1/(1+math.exp(-max(min(z,40),-40)))
    def update(self,x,y):
        p=self.predict(x)
        grad=(-y)/(1+math.exp(y*float(self.w@x))) * x
        self.w-=self.eta*grad
        n=np.linalg.norm(self.w)
        if n>self.B: self.w*=self.B/n

class ONS:
    def __init__(self,d,eta=1.0,B=5.0,lam=1.0):
        self.w=np.zeros(d); self.A=lam*np.eye(d); self.eta=eta; self.B=B
    def predict(self,x):
        z=float(self.w@x)
        return 1/(1+math.exp(-max(min(z,40),-40)))
    def update(self,x,y):
        z=float(self.w@x)
        g=(-y)/(1+math.exp(y*z))*x
        self.A += np.outer(g,g)
        step=np.linalg.solve(self.A,g)
        self.w -= self.eta*step
        n=np.linalg.norm(self.w)
        if n>self.B: self.w*=self.B/n

def seq(T,d,kind,seed=0):
    rng=np.random.default_rng(seed)
    if kind=="random":
        X=rng.normal(size=(T,d)); X/=np.maximum(np.linalg.norm(X,axis=1,keepdims=True),1e-12)
        y=rng.choice([-1,1],size=T)
    elif kind=="separable":
        w=rng.normal(size=d); w/=np.linalg.norm(w)
        X=rng.normal(size=(T,d)); X/=np.maximum(np.linalg.norm(X,axis=1,keepdims=True),1e-12)
        y=np.where(X@w>=0,1,-1)
    elif kind=="alternating":
        X=np.zeros((T,d)); X[:,0]=1.0; y=np.where(np.arange(T)%2==0,1,-1)
    else:
        X=np.zeros((T,d)); X[:,0]=1.0; y=np.ones(T,dtype=int)
    return X,y

def best_comparator_loss(X,y,B=5.0,steps=2500,lr=0.15):
    d=X.shape[1]; w=np.zeros(d)
    for _ in range(steps):
        yz=y*(X@w)
        coeff=-y/(1+np.exp(np.clip(yz,-40,40)))
        g=(coeff[:,None]*X).sum(axis=0)
        w -= lr*g/max(1,len(y))
        n=np.linalg.norm(w)
        if n>B: w*=B/n
    yz=y*(X@w)
    return float(np.logaddexp(0,-yz).sum())

def run_alg(alg,X,y):
    loss=0.0; t0=time.perf_counter()
    for x,yy in zip(X,y):
        p=alg.predict(x); loss+=logloss_prob(p,yy); alg.update(x,yy)
    return loss, time.perf_counter()-t0

def main():
    rows=[]
    for T in [128,256,512,1024]:
      for d in [2,5,10]:
       for kind in ["random","separable","alternating"]:
        X,y=seq(T,d,kind,seed=7)
        comp=best_comparator_loss(X,y)
        for name,alg in [
            ("OGD",OGD(d,eta=0.5,B=5)),
            ("ONS",ONS(d,eta=1.0,B=5,lam=1.0)),
        ]:
            loss,secs=run_alg(alg,X,y)
            rows.append(dict(T=T,d=d,sequence=kind,algorithm=name,
                             loss=loss,comparator_loss=comp,regret=loss-comp,
                             seconds=secs,us_per_round=1e6*secs/T))
    out={"benchmarks":rows,
         "published_theory":[
           {"method":"Foster et al. 2018","regret":"near-optimal improper norm dependence; positive resolution to a variant","computation":"efficient but EW construction in that line remains costly"},
           {"method":"Jezequel et al. 2020 (AIOLI)","regret":"O(B log(BT))","computation":"O(d^2 + log T) per round"},
           {"method":"Di Gennaro et al. 2026 EW","regret":"O(d log(BT))","computation":"~O(B^3 T^5) total worst case"}
         ]}
    with open("benchmark_results.json","w") as f: json.dump(out,f,indent=2)
    print(json.dumps(out,indent=2))

if __name__=="__main__":
    main()
