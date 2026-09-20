# Copyright (C) 2026 Mohammad Amir Khusru Akhtar
# Licensed under the Apache License, Version 2.0.
"""Adaptive localized 1D quadrature for the update-closed log-cosh surrogate.

This is an executable validation algorithm, not a claim of the unrestricted-d
theorem. It reconstructs the surrogate from additive state, localizes around
its numerical mode, and doubles Gauss-Legendre order until predictions stabilize.
"""
import math
import numpy as np
from .fixed_d import fit_even_logcosh_chebyshev, sigmoid

class AdaptiveLocalizedEW1D:
    def __init__(self,B=5.0,R=1.0,degree=18,mode_grid=1001,
                 min_nodes=8,max_nodes=256,tol_scale=0.05,tail_height=18.0):
        self.B=float(B); self.R=float(R); self.degree=int(degree)
        self.poly=fit_even_logcosh_chebyshev(B*R,degree)
        self.mode_grid=int(mode_grid); self.min_nodes=int(min_nodes)
        self.max_nodes=int(max_nodes); self.tol_scale=float(tol_scale)
        self.tail_height=float(tail_height)
        self.n=0; self.b=0.0
        self.moments={k:0.0 for k in range(2,degree+1,2)}
        self.last_nodes=0; self.last_interval=(-B,B)

    def update(self,x,y):
        self.n+=1; self.b+=float(y*x)
        for k in self.moments: self.moments[k]+=float(x)**k

    def potential_at(self,theta):
        th=np.asarray(theta,dtype=float)
        F=np.full_like(th,self.n*math.log(2.0),dtype=float)-0.5*self.b*th
        c=self.poly.coef
        for k,S in self.moments.items():
            if k<len(c): F += c[k]*S*th**k
        return F

    def _mode_and_interval(self):
        # Robust global scan; the paper theorem motivates replacing this by
        # Newton/local convex optimization. For validation this avoids false wins.
        g=np.linspace(-self.B,self.B,self.mode_grid)
        F=self.potential_at(g); j=int(np.argmin(F)); f0=float(F[j])
        # Find connected sublevel interval F <= Fmin + tail_height.
        ok=F<=f0+self.tail_height
        ids=np.flatnonzero(ok)
        if len(ids)==0: return float(g[j]),-self.B,self.B
        lo=float(g[ids[0]]); hi=float(g[ids[-1]])
        # never collapse interval below two grid cells
        pad=max(2*self.B/(self.mode_grid-1),1e-8)
        return float(g[j]),max(-self.B,lo-pad),min(self.B,hi+pad)

    def _quad_prediction(self,x,lo,hi,nodes):
        z,w=np.polynomial.legendre.leggauss(nodes)
        th=(hi+lo)/2+(hi-lo)*z/2
        qw=(hi-lo)*w/2
        F=self.potential_at(th); a=-F; a-=a.max()
        ww=qw*np.exp(a)
        return float(np.sum(ww*sigmoid(th*x))/np.sum(ww))

    def predict(self,x):
        _,lo,hi=self._mode_and_interval()
        # target is deliberately stricter than O(1/t) predictive accuracy.
        tol=self.tol_scale/max(1,self.n+1)**2
        n=self.min_nodes
        prev=self._quad_prediction(x,lo,hi,n)
        while n<self.max_nodes:
            n2=min(2*n,self.max_nodes)
            cur=self._quad_prediction(x,lo,hi,n2)
            if abs(cur-prev)<=tol:
                self.last_nodes=n2; self.last_interval=(lo,hi); return cur
            prev=cur; n=n2
        self.last_nodes=n; self.last_interval=(lo,hi); return prev

    def state_size(self):
        return 2+len(self.moments)
