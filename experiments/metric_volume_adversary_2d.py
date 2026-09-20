"""Adversarial d=2 search for Hessian metric volume scaling.

Approximates V_H(S_A)=integral_{F-Fmin<=A} sqrt(det H) dtheta
for many distinct bounded ridge directions. Uses deterministic grid integration
and several adversarial direction/label families plus random search.
"""
import json, math
import numpy as np

ALPHA=1.0
R=1.0

def softplus(x):
    return np.logaddexp(0.0,x)

def eval_grid(X,y,lim=4.5,n=241,A=None):
    z=np.linspace(-lim,lim,n)
    h=z[1]-z[0]
    a,b=np.meshgrid(z,z,indexing="ij")
    pts=np.stack([a.ravel(),b.ravel()],axis=1)
    F=.5*ALPHA*np.sum(pts*pts,axis=1)
    H11=np.full(len(pts),ALPHA); H22=np.full(len(pts),ALPHA); H12=np.zeros(len(pts))
    # chunks over observations; grid vectorized
    for x,yy in zip(X,y):
        q=yy*(pts@x)
        F += softplus(-q)
        w=1/(2+2*np.cosh(np.clip(q,-40,40)))
        H11 += w*x[0]*x[0]; H22 += w*x[1]*x[1]; H12 += w*x[0]*x[1]
    fmin=float(F.min())
    if A is None: A=2.0*math.log(len(X)+2)
    mask=F<=fmin+A
    det=np.maximum(H11*H22-H12*H12,0)
    V=float(np.sum(np.sqrt(det[mask]))*h*h)
    area=float(mask.sum()*h*h)
    return V,area,fmin,A

def family(T,kind,seed=0):
    rng=np.random.default_rng(seed)
    if kind=="uniform":
        ang=np.linspace(0,2*np.pi,T,endpoint=False)
        X=np.c_[np.cos(ang),np.sin(ang)]
        y=np.ones(T)
    elif kind=="alternating_circle":
        ang=np.linspace(0,2*np.pi,T,endpoint=False)
        X=np.c_[np.cos(ang),np.sin(ang)]
        y=np.where(np.arange(T)%2==0,1.,-1.)
    elif kind=="semicircle":
        ang=np.linspace(-.49*np.pi,.49*np.pi,T)
        X=np.c_[np.cos(ang),np.sin(ang)]
        y=np.ones(T)
    elif kind=="two_arcs":
        a1=rng.normal(.55,.12,T//2); a2=rng.normal(-.55,.12,T-T//2)
        ang=np.r_[a1,a2]
        X=np.c_[np.cos(ang),np.sin(ang)]
        y=np.r_[np.ones(T//2),-np.ones(T-T//2)]
    elif kind=="random":
        ang=rng.uniform(0,2*np.pi,T)
        X=np.c_[np.cos(ang),np.sin(ang)]
        y=rng.choice([-1.,1.],T)
    elif kind=="narrow_fan":
        ang=np.linspace(-.3,.3,T)
        X=np.c_[np.cos(ang),np.sin(ang)]
        y=np.ones(T)
    return X,y

Ts=[16,32,64,128,256]
kinds=["uniform","alternating_circle","semicircle","two_arcs","random","narrow_fan"]
rows=[]
for T in Ts:
    best=None
    for kind in kinds:
        seeds=range(5) if kind in ("random","two_arcs") else range(1)
        for seed in seeds:
            X,y=family(T,kind,seed)
            V,area,fmin,A=eval_grid(X,y)
            row=dict(T=T,kind=kind,seed=seed,V=V,area=area,A=A,
                     V_over_log=V/math.log(T),V_over_log2=V/(math.log(T)**2))
            rows.append(row)
            if best is None or V>best["V"]: best=row
    print("BEST",best)

# fit worst-by-T log V = beta log T + c, and log V = beta log logT+c
bestrows=[]
for T in Ts:
    rr=max((r for r in rows if r["T"]==T),key=lambda r:r["V"])
    bestrows.append(rr)
lt=np.log(np.array(Ts,float)); lv=np.log(np.array([r["V"] for r in bestrows]))
ll=np.log(np.log(np.array(Ts,float)))
beta_T=float(np.polyfit(lt,lv,1)[0])
beta_log=float(np.polyfit(ll,lv,1)[0])
out={"rows":rows,"best_by_T":bestrows,"fit_power_T":beta_T,"fit_power_logT":beta_log}
open("metric_volume_adversary_2d_results.json","w").write(json.dumps(out,indent=2))
print("fit V~T^beta beta=",beta_T)
print("fit V~(logT)^beta beta=",beta_log)
