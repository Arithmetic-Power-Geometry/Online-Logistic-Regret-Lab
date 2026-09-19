import json
import numpy as np
from numpy.polynomial.hermite import hermgauss

def sigmoid(z):
    return 1/(1+np.exp(-np.clip(z,-60,60)))

class GridEW2D:
    def __init__(self,radius=6,n=241,prior_var=4):
        g=np.linspace(-radius,radius,n)
        self.a,self.b=np.meshgrid(g,g,indexing="ij")
        lw=-(self.a**2+self.b**2)/(2*prior_var); lw-=lw.max()
        self.w=np.exp(lw); self.w/=self.w.sum()
    def update(self,x,y):
        z=x[0]*self.a+x[1]*self.b
        self.w*=np.maximum(sigmoid(y*z),1e-300); self.w/=self.w.sum()
    def directional(self,x):
        z=x[0]*self.a+x[1]*self.b
        mu=float(np.sum(self.w*z)); c=z-mu
        var=float(np.sum(self.w*c*c))
        m3=float(np.sum(self.w*c**3))
        p=float(np.sum(self.w*sigmoid(z)))
        return p,mu,var,m3

X,W=hermgauss(120)

def edgeworth_sigmoid(mu,var,m3):
    sd=np.sqrt(max(var,1e-15))
    z=np.sqrt(2)*X
    # E[f(mu+sd Z)] + kappa3/(6 sd^3) E[H3(Z) f(...)]
    f=sigmoid(mu+sd*z)
    base=np.sum(W*f)/np.sqrt(np.pi)
    skew=m3/(sd**3)
    corr=(skew/6.0)*np.sum(W*(z**3-3*z)*f)/np.sqrt(np.pi)
    return float(base+corr)

def gaussian_sigmoid(mu,var):
    sd=np.sqrt(max(var,0))
    return float(np.sum(W*sigmoid(mu+np.sqrt(2)*sd*X))/np.sqrt(np.pi))

def run(n,s):
    ew=GridEW2D()
    for _ in range(n): ew.update(np.array([0.,1.]),1)
    for _ in range(n): ew.update(np.array([1.,float(s)]),-1)
    p,mu,var,m3=ew.directional(np.array([1.,0.]))
    g=gaussian_sigmoid(mu,var)
    e=edgeworth_sigmoid(mu,var,m3)
    t=2*n+1
    return {"n":n,"diag_sign":s,"t":t,"exact":p,"gaussian":g,
            "edgeworth3":e,"m3":m3,
            "gaussian_error":abs(g-p),"edgeworth3_error":abs(e-p),
            "gaussian_t2_error":t*t*abs(g-p),
            "edgeworth3_t2_error":t*t*abs(e-p)}

if __name__=="__main__":
    print(json.dumps([run(n,s) for n in [4,8,16,32,64] for s in [1,-1]],indent=2))
