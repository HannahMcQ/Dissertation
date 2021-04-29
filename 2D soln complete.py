# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 17:48:06 2021

@author: Hannah
"""


from math import sin,cos,e

import matplotlib.pyplot as plt

import numpy as np


L = 696340

p = 34800/L #this is taken from the phd thesis
omega0 = (-(-155.8/np.cos(np.rad2deg(50)) - 25.3)/1000/L)*2   # velocity is rsinth*om
R = 696340/L
B0 = 1 #unimportant as just a constant
g = np.deg2rad(40) #0.35 #gamma0 approx 20 degrees
D = 450/L**2


def A(t):
    return 0.25*(p**2)*(sin(g)**2) + 0.5*(p**2)*(cos(g)**2) + D*t + (1/3)*D*(omega0**2)*(t**3)

def B(t):
    return -0.5*(p**2)*sin(g)*cos(g) + D*omega0*(t**2)

def C(t):
    return 0.25*(p**2)*(cos(g)**2) + 0.5*(p**2)*(sin(g)**2) + D*t

def Q(t):
    return 4*A(t)*C(t) - B(t)**2

#working from x,y coords
def BZZ(x,y,t):
    x0 = 0.75
    y0 = 0.5
    u0 = 15.27/1000/L
    a1 = x - 0.5*omega0*u0*(t**2) + omega0*t*y
    a2 = y - u0*t
    A1= a1 - x0
    A2 = a2 - y0
    one = (B0*(p**3)*(e**0.5)*(2**0.5))/(Q(t)**1.5)
    two = (cos(g)*(0.5*B(t)*A2 - C(t)*A1)) - (sin(g)*(0.5*B(t)*A1 - A(t)*A2))
    three = np.exp((-C(t)*(A1**2) + B(t)*A1*A2 - A(t)*(A2**2))/Q(t))
    return one*two*three

x1 = np.linspace(0,1,256)
y1 = np.linspace(0,1,256)
xx,yy = np.meshgrid(x1,y1)
BZZ2 = np.vectorize(BZZ)
t1 = 3600*24*30 #i.e. 36 days in seconds
z = BZZ2(xx,yy,t1)


plt.contourf(xx,yy,z,700,vmax=0.07,vmin=-0.07,cmap='bwr')
plt.xlabel('x/L')
plt.ylabel('y/L')
plt.colorbar()
plt.show()