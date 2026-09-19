import json
import numpy as np
from numpy.polynomial.hermite import hermgauss

def sigmoid(z):
    return 1.0/(1.0+np.exp(-np.clip(z,-60,60)))

class GridEW2D:
    def __init__(self,radius=6.0,n=241,prior_var=4.0):
        g=np.linspace(-radius,radius,n)
        self.t1,self.t2=np.meshgrid(g,g,indexing="ij")
        lw=-(self.t1**2+self.t2**2)/(2*prior_var)
        lw-=lw.max(); self.w=np.exp(lw); self.w/=self.w.sum()
    def update(self,x,y):
        z=x[0]*self.t1+x[1]*self.t2
        self.w*=np.maximum(sigmoid(y*z),1e-300); self.w/=self.w.sum()
    def predict(self,x):
        return float(np.sum(self.w*sigmoid(x[0]*self.t1+x[1]*self.t2)))
    def moments(self):
        m1=float(np.sum(self.w*self.t1)); m2=float(np.sum(self.w*self.t2))
        d1=self.t1-m1; d2=self.t2-m2
        C=np.array([[np.sum(self.w*d1*d1),np.sum(self.w*d1*d2)],
                    [np.sum(self.w*d1*d2),np.sum(self.w*d2*d2)]],float)
        return np.array([m1,m2]),C

GHX,GHW=hermgauss(80)
def matched_gaussian_predict(mean,cov,x):
    mu=float(x@mean); var=max(float(x@cov@x),0.0)
    z=mu+np.sqrt(2.0*var)*GHX
    return float(np.sum(GHW*sigmoid(z))/np.sqrt(np.pi))

def run(n,diag_sign):
    ew=GridEW2D()
    for _ in range(n): ew.update(np.array([0.,1.]),1)
    xd=np.array([1.,float(diag_sign)])
    for _ in range(n): ew.update(xd,-1)
    xq=np.array([1.,0.])
    p=ew.predict(xq); mean,cov=ew.moments()
    q=matched_gaussian_predict(mean,cov,xq)
    t=2*n+1
    return {"n":n,"diag_sign":diag_sign,"t":t,"exact":p,
            "oracle_mean_cov_gaussian":q,"absolute_error":abs(p-q),
            "t_squared_error":t*t*abs(p-q),
            "mean":mean.tolist(),"cov":cov.tolist()}

if __name__=="__main__":
    print(json.dumps([run(n,s) for n in [4,8,16,32,64] for s in [1,-1]],indent=2))
