#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 14:01:53 2019

@author: enlightened
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLine2D

#                                                                               M = I w dot + w x I w

def fdot(t, w, I, M):
    M= scalarvectprod(0, w)
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
    w = [[0.1 , 1, -0.1]]
    M = [[1 , 1, 0]]
    H= [[0,0,0]]
    I = np.matrix([[2,0,0],[0,2,0],[0,0,2]])
    zero = [0]
    h = float(input ("Enter interval \n"))
    time = []
    wx =[]
    wy =[]
    wz = []
    energy = []
    energy.append(0.5*I.item(0)*(w[0][0])*(w[0][0])+0.5*I.item(4)*(w[0][1])*(w[0][1])+0.5*I.item(8)*(w[0][2])*(w[0][2]))
    wx.append(w[0][0])
    wy.append(w[0][1])
    wz.append(w[0][2])
    H.append(matrixvectprod(I, w[0]))
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
        wx.append(w[i+1][0])
        wy.append(w[i+1][1])
        wz.append(w[i+1][2])
        energy.append(0.5*I.item(0)*(w[i+1][0])*(w[i+1][0])+0.5*I.item(4)*(w[i+1][1])*(w[i+1][1])+0.5*I.item(8)*(w[i+1][2])*(w[i+1][2]))
   #     print (mod(w[i]), " ")
        time.append(t0 + (i+1)*h)
        zero.append(0)
        H.append(matrixvectprod(I, w[i+1]))
 #   plt.plot( time,  H[0:], label = 'line')
 #   plt.plot( time,  energy, label = "energy")
 #   plt.plot.Axes.set_ybounds(-1.6, 1.6)
  #  line1, = plt.plot( time,  energy, 'r', label = "Energy(J)") 
    line1, = plt.plot( time,  wx, label = "wx")
  #  line2, = plt.plot( time,  wy, label = "wy")
  #  line3, = plt.plot( time,  wz, label = "wz")
 #   print(energy) 

  #  line5, = plt.plot( time, zero, 'w')
 #   plt.title('Angular velocity v/s Time plot')
    plt.title('Energy v/s Time plot') 
    plt.xlabel('Time (seconds)')
  #  plt.ylabel('Angular velocity(Hz)')    
    plt.ylabel('Energy (J)')
    plt.legend(handler_map={line1: HandlerLine2D(numpoints=4)})
    
main()
