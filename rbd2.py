#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 14:01:53 2019

@author: enlightened
"""

import numpy as np
import matplotlib.pyplot as plt

#                                                                               M = I w dot + w x I w

def fdot(t, w, I, M):
    g = crossprod (matrixvectprod(I.I, w), matrixvectprod(I, w))
    h = matrixvectprod(I.I, M)
    return addvectors(h, scalarvectprod(-1, g))
    
def matrixvectprod(m, v):
    k = [m.item(0)*v[0]+m.item(1)*v[1]+m.item(2)*v[2], m.item(3)*v[0]+m.item(4)*v[1]+m.item(5)*v[2], m.item(6)*v[0]+m.item(7)*v[1]+m.item(8)*v[2]]
    return k

def crossprod(e,j):
    p = [e[1]*j[2]-e[2]*j[1], e[2]*j[0]-e[0]*j[2], e[0]*j[1]-e[1]*j[0]]
    return p

def scalarvectprod(s, x):
    u = [s*x[0], s*x[1], s*x[2]]
    return u

def addvectors(a, b):
    return [a[0]+b[0], a[1]+b[1], a[2]+b[2]]

def mod(y):
    return y[0]*y[0]+y[1]*y[1]+y[2]*y[2]

def main():
    w = [[3 ,-3, 1]]
    M = [[0 , 0, 0]]
    H= [[0,0,0]]
    I = np.matrix([[2,0,0],[0,2,0],[0,0,9]])
    h = float(input ("Enter interval \n"))
    time = []
    t0 = float(input ("Enter t0 \n"))
    deltaT = float(input("Enter DeltaT : simulation t -> t + deltaT \n"))
    time.append(t0)    
    for i in range (int(deltaT / h)):
        k1 = scalarvectprod(h, fdot(t0 + i*h , w[i], I, M[0]))
        k2 = scalarvectprod(h, fdot(t0 + i*h + h/2 , addvectors(w[i], scalarvectprod(0.5, k1)), I, M[0]))
        k3 = scalarvectprod(h, fdot(t0 + i*h + h/2 , addvectors(w[i], scalarvectprod(0.5, k2)), I, M[0]))
        k4 = scalarvectprod(h, fdot(t0 + i*h + h , addvectors(w[i], k3), I, M[0]))
        ksum = addvectors(addvectors(k1, k4), scalarvectprod(2,addvectors(k2, k3)))
        w.append(addvectors( w[i], scalarvectprod(1/6 , ksum)))
        print (mod(w[i]), " ")
        time.append(t0 + (i+1)*h)
    print (w[][2])
    
main()