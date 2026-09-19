import json
import numpy as np
from numpy.polynomial import Chebyshev


def R(u, k):
    a = np.power(u, k)
    b = np.power(1.0-u, k)
    return a/(a+b)


def err(k, m, n=40001):
    u=np.linspace(0.0,1.0,n)
    y=R(u,k)
    # diagnostic LS Chebyshev fit, not certified minimax
    p=Chebyshev.fit(u,y,m,domain=[0,1])
    return float(np.max(np.abs(p(u)-y)))


if __name__=="__main__":
    targets=[1e-2,1e-3,1e-4]
    degrees=[4,8,12,16,24,32,48,64,96,128,192,256]
    out={}
    for k in [2,4,8,16,32,64]:
        rows=[]
        for m in degrees:
            e=err(k,m)
            rows.append({"degree":m,"error":e})
        mins={}
        for eps in targets:
            ok=[r["degree"] for r in rows if r["error"]<=eps]
            mins[str(eps)]=min(ok) if ok else None
        out[str(k)]={"rows":rows,"minimum_tested_degree":mins}
    print(json.dumps(out,indent=2))
