#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


# In[30]:


class Oscilador:
    def __init__(self, k0, m0, y0,v0,t0):
        self.k=float(k0)
        self.m=float(m0)
        self.w=(self.k/self.m)**(0.5)
        self.t=np.linspace(0,t0,100)
        self.ini=np.array([y0,v0])
    def SolucionArmonico(self):
        def f1(y, t):
            return np.array([y[1], -(self.w**2.)*y[0]])
        return odeint(f1,self.ini,self.t)
    
class OsciladorAmortiguado:
    def __init__(self, k0,b0, m0, y0,v0,t0):
        self.gamma=b0/(2*m0)
        self.k=float(k0)
        self.m=float(m0)
        self.w=(self.k/self.m)**(0.5)
        self.t=np.linspace(0,t0,100)
        self.ini=np.array([y0,v0])
        self.b=b0
    def SolucionAmort(self):
        def f2(y, t):
            return np.array([y[1], -(self.w**2.)*y[0]-2*self.gamma*y[1]])
        return odeint(f2,self.ini,self.t)


# In[ ]:




