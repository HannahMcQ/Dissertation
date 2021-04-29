# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 13:17:14 2021

@author: Hannah
"""

from math import exp
import numpy as np
import matplotlib.pyplot as plt


def sigma(t,eta,r,delu,sig0):
    x = sig0**2 +(eta/(r**2*delu))*(1-exp(-2*delu*t))
    return x**0.5

x=24*60*60 #number of seconds are in a day
def BL(tt,lambdaL,a,lambda0,eta,r,delu,sig0):
    return (a/sigma(tt*x,eta,r,delu,sig0))*exp(-((lambdaL-lambda0)**2)/(2*sigma(tt*x, eta, r, delu, sig0)**2))



n = 450*1000*1000 
R = 696340000
D = (2*17)/R
    

y1 = np.linspace(-0.5,0.75,730)
t1 = np.linspace(0,1460,730) #runtime = 4 years
t,y = np.meshgrid(t1,y1)
BL2 = np.vectorize(BL)
z = BL2(t,y,1,0.2,n,R,D,0.05) - BL2(t,y,1,0.3,n,R,D,0.05) #subtracting so it's of opposite polarity
# and a lamda0 of 0.2 and 0.3 (is this in radians?)

plt.contourf(t,y,z,730,cmap='bwr')
plt.xlabel('Time (days)')
plt.ylabel('latitude (radians)')
plt.colorbar()
plt.show()