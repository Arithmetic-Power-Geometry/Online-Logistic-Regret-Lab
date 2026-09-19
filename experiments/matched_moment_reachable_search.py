import json, itertools
import numpy as np

def sigmoid(z):
    return 1/(1+np.exp(-np.clip(z,-60,60)))

class Grid:
    def __init__(self,R=5,n=101,s2=4):
        g=np.linspace(-R,R,n); self.a,self.b=np.meshgrid(g,g,indexing="ij")
        lw=-(self.a*self.a+self.b*self.b)/(2*s2); lw-=lw.max()
        self.base=np.exp(lw); self.base/=self.base.sum()
    def posterior(self,hist):
        w=self.base.copy()
        for x,y,count in hist:
            z=x[0]*self.a+x[1]*self.b
            w*=np.maximum(sigmoid(y*z),1e-300)**count
            w/=w.sum()
        return w
    def features(self,w,r=3):
        vals=[]
        for deg in range(1,r+1):
            for i in range(deg+1):
                vals.append(float(np.sum(w*(self.a**i)*(self.b**(deg-i)))))
        p=float(np.sum(w*sigmoid(self.a)))
        return np.array(vals),p

def histories(max_count=6):
    # compact dictionary chosen to generate cross-direction shape
    dirs=[(np.array([0.,1.]),1),(np.array([0.,1.]),-1),
          (np.array([1.,1.]),1),(np.array([1.,1.]),-1),
          (np.array([1.,-1.]),1),(np.array([1.,-1.]),-1)]
    out=[]
    # two-block histories keep search manageable and interpretable
    for i,j in itertools.combinations(range(len(dirs)),2):
        for c1 in range(1,max_count+1):
            for c2 in range(1,max_count+1):
                x1,y1=dirs[i]; x2,y2=dirs[j]
                out.append([(x1,y1,c1),(x2,y2,c2)])
    return out

def search(r=2,max_count=6):
    G=Grid(); rows=[]
    for h in histories(max_count):
        w=G.posterior(h); m,p=G.features(w,r); rows.append((m,p,h))
    # normalize moment coordinates before nearest-state search
    M=np.stack([x[0] for x in rows]); sd=M.std(axis=0)+1e-12
    best=None
    for i in range(len(rows)):
        mi,pi,hi=rows[i]
        for j in range(i+1,len(rows)):
            mj,pj,hj=rows[j]
            mismatch=float(np.linalg.norm((mi-mj)/sd))
            sep=abs(pi-pj)
            score=sep/(mismatch+1e-6)
            if best is None or score>best[0]:
                best=(score,mismatch,sep,hi,hj,mi,mj,pi,pj)
    score,mm,sep,h1,h2,m1,m2,p1,p2=best
    enc=lambda h:[{"x":x.tolist(),"y":y,"count":c} for x,y,c in h]
    return {"r":r,"score":score,"normalized_moment_mismatch":mm,
            "prediction_separation":sep,"history1":enc(h1),"history2":enc(h2),
            "moments1":m1.tolist(),"moments2":m2.tolist(),
            "prediction1":p1,"prediction2":p2}

if __name__=="__main__":
    print(json.dumps([search(2),search(3)],indent=2))
