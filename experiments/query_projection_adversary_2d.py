import json
import numpy as np


def sigmoid(z):
    return 1.0/(1.0+np.exp(-np.clip(z,-60,60)))


class GridEW2D:
    def __init__(self, radius=6.0, n=241, prior_var=4.0):
        g=np.linspace(-radius,radius,n)
        self.t1,self.t2=np.meshgrid(g,g,indexing="ij")
        logw=-(self.t1**2+self.t2**2)/(2*prior_var)
        logw-=logw.max()
        self.w=np.exp(logw); self.w/=self.w.sum()

    def update(self,x,y):
        z=x[0]*self.t1+x[1]*self.t2
        p=sigmoid(y*z)
        self.w*=np.maximum(p,1e-300)
        self.w/=self.w.sum()

    def predict(self,x):
        return float(np.sum(self.w*sigmoid(x[0]*self.t1+x[1]*self.t2)))


class ProjectionEW1D:
    # Query is fixed to e1. Historical factors are replaced by their e1
    # projections, deleting all orthogonal coupling.
    def __init__(self,radius=6.0,n=4001,prior_var=4.0):
        self.z=np.linspace(-radius,radius,n)
        logw=-(self.z**2)/(2*prior_var)
        logw-=logw.max()
        self.w=np.exp(logw); self.w/=self.w.sum()

    def update(self,x,y):
        a=float(x[0])
        p=sigmoid(y*a*self.z)
        self.w*=np.maximum(p,1e-300)
        self.w/=self.w.sum()

    def predict_e1(self):
        return float(np.sum(self.w*sigmoid(self.z)))


def run(n_axis,n_diag,diag_sign=1):
    exact=GridEW2D()
    proj=ProjectionEW1D()

    # Learn theta2 strongly.
    for _ in range(n_axis):
        x=np.array([0.0,1.0]); y=1
        exact.update(x,y); proj.update(x,y)

    # Diagonal evidence. Projection-only model sees only x1=1 and cannot
    # condition on the already learned theta2.
    xdiag=np.array([1.0,float(diag_sign)])
    for _ in range(n_diag):
        y=-1
        exact.update(xdiag,y); proj.update(xdiag,y)

    p=exact.predict(np.array([1.0,0.0]))
    q=proj.predict_e1()
    return {
        "n_axis":n_axis,
        "n_diag":n_diag,
        "diag_sign":diag_sign,
        "exact_p_e1":p,
        "projection_p_e1":q,
        "absolute_error":abs(p-q),
        "t":n_axis+n_diag+1,
        "t_squared_error":(n_axis+n_diag+1)**2*abs(p-q),
    }


if __name__=="__main__":
    out=[]
    for n in [4,8,16,32,64]:
        out.append(run(n,n,1))
        out.append(run(n,n,-1))
    print(json.dumps(out,indent=2))
