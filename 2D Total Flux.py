# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 21:03:24 2021

@author: Hannah
"""

from math import sin,cos,exp,pi,e
import matplotlib.pyplot as plt
import numpy as np 

#quantities should be in km, seconds and radians

R = 696340
omega0 = -(-155.8/np.cos(np.rad2deg(50)) - 25.3)
B0 = 1 #idk
#g = np.deg2rad(20) #20 degrees
D = 450
p = 0.06*R

def A(t,g):
    return 0.25*(p**2)*(sin(g)**2) + 0.5*(p**2)*(cos(g)**2) + D*t + (1/3)*D*(omega0**2)*(t**3)

def B(t,g):
    return -0.5*(p**2)*sin(g)*cos(g) + D*omega0*(t**2)

def C(t,g):
    return 0.25*(p**2)*(cos(g)**2) + 0.5*(p**2)*(sin(g)**2) + D*t

def Q(t,g):
    return (4*A(t,g)*C(t,g)) - (B(t,g)**2)

def W(t,g):
    return A(t,g)*(sin(g)**2) + B(t,g)*sin(g)*cos(g) + C(t,g)*(cos(g)**2)

def phi(t,g):
        a = B0*(p**3)
        b = (2*pi*exp(1))**0.5
        c = W(t,g)/Q(t,g)
        return a*b*(c**0.5)


xvalues = [i/2 for i in range(700)]
y1values = [phi(t,np.deg2rad(0)) for t in xvalues]
plt.plot(xvalues, y1values, label='0')
y2values = [phi(t,np.deg2rad(10)) for t in xvalues]
plt.plot(xvalues,y2values,label='10')
y3values = [phi(t,np.deg2rad(20)) for t in xvalues]
plt.plot(xvalues, y3values, label='20')
y4values = [phi(t,np.deg2rad(30)) for t in xvalues]
plt.plot(xvalues,y4values,label='30')
y5values = [phi(t,np.deg2rad(40)) for t in xvalues]
plt.plot(xvalues, y5values, label='40')
y6values = [phi(t,np.deg2rad(50)) for t in xvalues]
plt.plot(xvalues, y6values, label = '50')
plt.legend()
plt.margins(x=0)
plt.xlabel('Time (days)')
plt.ylabel('Total Magnetic Flux')
plt.show()








