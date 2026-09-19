import json
import numpy as np
from scipy.optimize import differential_evolution, least_squares

def sig(z): return 1/(1+np.exp(-np.clip(z,-60,60)))

class Grid:
    def __init__(self,R=6,n=161,s2=4):
        g=np.linspace(-R,R,n); self.a,self.b=np.meshgrid(g,g,indexing="ij")
        lw=-(self.a*self.a+self.b*self.b)/(2*s2); lw-=lw.max()
        self.base=np.exp(lw); self.base/=self.base.sum()
        self.factors=[
            sig(self.b), sig(-self.b),
            sig(self.a+self.b), sig(-(self.a+self.b)),
            sig(self.a-self.b), sig(-(self.a-self.b))]
    def eval(self,c,r):
        lw=np.log(self.base+1e-300)
        for q,f in zip(c,self.factors): lw += q*np.log(f+1e-300)
        lw-=lw.max(); w=np.exp(lw); w/=w.sum()
        m=[]
        for deg in range(1,r+1):
            for i in range(deg+1):
                m.append(float(np.sum(w*(self.a**i)*(self.b**(deg-i)))))
        p=float(np.sum(w*sig(self.a)))
        return np.array(m),p

def search(r,seed=7):
    G=Grid()
    # Two independent nonnegative weighted histories on same six valid factors.
    # Optimize prediction separation subject to strong moment matching.
    def obj(v):
        c1=v[:6]; c2=v[6:]
        m1,p1=G.eval(c1,r); m2,p2=G.eval(c2,r)
        mm=np.linalg.norm(m1-m2)
        sep=abs(p1-p2)
        return 1000*mm - sep
    res=differential_evolution(obj,[(0,12)]*12,seed=seed,popsize=8,maxiter=80,
                               polish=False,workers=1,updating="immediate")
    v=res.x
    # local least-squares: moment equality plus a small incentive to preserve
    # the separation found globally
    c1=v[:6]; c2=v[6:]
    m1,p1=G.eval(c1,r); m2,p2=G.eval(c2,r)
    sign=1 if p1>=p2 else -1
    def residual(v):
        m1,p1=G.eval(v[:6],r); m2,p2=G.eval(v[6:],r)
        return np.r_[100*(m1-m2), 0.05*((p1-p2)-sign*0.05)]
    ls=least_squares(residual,v,bounds=(0,12),max_nfev=300)
    c1,c2=ls.x[:6],ls.x[6:]
    m1,p1=G.eval(c1,r); m2,p2=G.eval(c2,r)
    return {"r":r,"weights1":c1.tolist(),"weights2":c2.tolist(),
            "max_abs_moment_mismatch":float(np.max(np.abs(m1-m2))),
            "l2_moment_mismatch":float(np.linalg.norm(m1-m2)),
            "prediction1":p1,"prediction2":p2,
            "prediction_separation":abs(p1-p2),
            "moments1":m1.tolist(),"moments2":m2.tolist()}

if __name__=="__main__":
    print(json.dumps([search(2,7),search(3,11)],indent=2))
