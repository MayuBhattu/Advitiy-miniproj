#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 18:47:00 2019

@author: enlightened
"""
#%%

import matplotlib.pyplot as plt 
import math


def fdot( t, y):
    return t * (1 - y *y)

    

def main():
    h = float(input ("Enter interval \n"))
    y = []
    j = []
    t0 = float(input ("Enter t0 \n"))
    y.append (float(input ("Enter y0 \n")))
    j.append(t0)
    for i in range (50):
        k1 = h * fdot(t0 + i*h , y[i])
        k2 = h * fdot(t0 + i*h + h/2, y[i]+ k1/2)
        k3 = h * fdot(t0 + i*h + h/2, y[i]+ k2/2)
        k4 = h * fdot(t0 + i*h + h, y[i]+ k3 )
        y.append(float( y[i] + 1/6 * (k1 + 2*k2 + 2*k3 + k4)))
        j.append(t0 + (i+1)*h)
    print (y)
    plt.plot(j, y)        
    
main()
        
        
    
    
#%%
    