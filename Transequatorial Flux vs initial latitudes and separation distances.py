# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 14:18:15 2021

@author: Hannah
"""
from math import exp,pi
import matplotlib.pyplot as plt

def phi(d,l0,sig0):
    u0=17
    R = 696340000
    eta = 600*1000*1000 
    delu = 2*u0/R
    LR = (sig0**2 + (eta/((R**2)*delu)))
    return (d/(2*0.5 * pi**0.5*LR)) * exp((-l0**2)/(2*LR**2))    

xlist = [-pi/6 + i*pi/288 for i in range(96)]
ylist = [phi(0.1,x,0.1) for x in xlist]
plt.xlabel("Initial Insertion Latitude of the Bipole (Radians)")
plt.ylabel("Net Transequatorial Flux Fraction")
plt.title("Initial Latitude of Insertions vs Transequatorial Flux")
plt.plot(xlist,ylist)
plt.show()         

xl = [i*0.005 for i in range(100)]
yl = [phi(x,0.2,0.1) for x in xl]
#plt.xlabel('Separation between Flux Patches (radians)')
#plt.ylabel('Net Transequatorial Flux Fraction')
#plt.title('Separation Distance vs Transequatorial Flux')
#plt.plot(xl,yl)
#plt.show()
