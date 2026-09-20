# Copyright (C) 2026 Mohammad Amir Khusru Akhtar
# Licensed under the Apache License, Version 2.0.
"""Executable fixed-d/1D components supporting the manuscript.

These routines are deliberately claim-safe: ExactGridEW1D is a numerical oracle;
ScoreCalibratedRepeated1D implements the exact repeated-direction score identity;
LogCoshMomentSurrogate1D is an update-closed polynomial surrogate.
"""
import math
import numpy as np
from numpy.polynomial.chebyshev import Chebyshev

def sigmoid(z):
    z=np.asarray(z,dtype=float)
    out=np.empty_like(z)
    pos=z>=0
    out[pos]=1/(1+np.exp(-z[pos]))
    ez=np.exp(z[~pos]); out[~pos]=ez/(1+ez)
    return out if out.ndim else float(out)

class ExactGridEW1D:
    def __init__(self,B=5.0,n_grid=4001):
        self.B=float(B)
        self.grid=np.linspace(-B,B,n_grid)
        self.logw=np.zeros(n_grid)
    def predict(self,x=1.0):
        a=self.logw-self.logw.max()
        w=np.exp(a); w/=w.sum()
        return float(w@sigmoid(self.grid*x))
    def mean(self):
        a=self.logw-self.logw.max()
        w=np.exp(a); w/=w.sum()
        return float(w@self.grid)
    def update(self,x,y):
        yz=y*x*self.grid
        self.logw -= np.logaddexp(0.0,-yz)

class GaussianPriorGridEW1D:
    def __init__(self,s=1.0,B=10.0,n_grid=8001):
        self.s=float(s); self.grid=np.linspace(-B,B,n_grid)
        self.logw=-0.5*(self.grid/s)**2
    def predict(self,x=1.0):
        a=self.logw-self.logw.max(); w=np.exp(a); w/=w.sum()
        return float(w@sigmoid(self.grid*x))
    def mean(self):
        a=self.logw-self.logw.max(); w=np.exp(a); w/=w.sum()
        return float(w@self.grid)
    def update(self,x,y):
        self.logw -= np.logaddexp(0.0,-y*x*self.grid)

def score_prediction_from_mean(n_pos,n_neg,mu,s=1.0):
    n=n_pos+n_neg
    if n==0: return 0.5
    return n_pos/n - mu/(s*s*n)

def fit_even_logcosh_chebyshev(L,degree,grid_n=12001):
    """Return power-basis Polynomial approximation to h(z)=log cosh(z/2)."""
    if degree%2: degree+=1
    z=np.linspace(-L,L,grid_n)
    h=np.logaddexp(z/2,-z/2)-math.log(2.0)
    ch=Chebyshev.fit(z,h,degree,domain=[-L,L])
    p=ch.convert(kind=np.polynomial.Polynomial)
    c=p.coef.copy()
    # enforce evenness exactly
    c[1::2]=0.0
    return np.polynomial.Polynomial(c)

class LogCoshMomentSurrogate1D:
    """Update-closed 1D surrogate on theta in [-B,B], |x|<=R."""
    def __init__(self,B=5.0,R=1.0,degree=12,n_grid=4001):
        self.B=float(B); self.R=float(R); self.degree=int(degree)
        self.grid=np.linspace(-B,B,n_grid)
        self.poly=fit_even_logcosh_chebyshev(B*R,degree)
        self.n=0; self.b=0.0
        self.moments={k:0.0 for k in range(2,degree+1,2)}
    def update(self,x,y):
        self.n+=1; self.b+=y*x
        for k in self.moments: self.moments[k]+=x**k
    def potential(self):
        th=self.grid
        F=np.full_like(th,self.n*math.log(2.0))-0.5*self.b*th
        c=self.poly.coef
        for k,S in self.moments.items():
            if k<len(c): F += c[k]*S*(th**k)
        return F
    def predict(self,x):
        F=self.potential(); a=-F; a-=a.max(); w=np.exp(a); w/=w.sum()
        return float(w@sigmoid(self.grid*x))
    def state_size(self):
        return 2+len(self.moments)
