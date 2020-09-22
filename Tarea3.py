#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from MasaResorte import *


# In[2]:


#desde t=0 hasta t=10 
#Oscilador(constante k, masa, y0, v0 , t=10seg )

P1=Oscilador(1,10,1,1,10)
Os1=Oscilador.SolucionArmonico(P1)
P2=Oscilador(10,1,1,1,10)
Os2=Oscilador.SolucionArmonico(P2)
P3=Oscilador(1,1,0,1,10)
Os3=Oscilador.SolucionArmonico(P3)
P4=Oscilador(1,1,1,0,10)
Os4=Oscilador.SolucionArmonico(P4)
P5=Oscilador(1,2,2,1.5,10)
Os5=Oscilador.SolucionArmonico(P5)

Os=[Os1,Os2,Os3,Os4,Os5]
P=[P1,P2,P3,P4,P5]
colors=['red','green','blue','gray','yellow']

#grafiquemos
plt.figure(figsize=(7.5,7.5))
for i in np.arange(0,5,1):
    plt.subplot(5,1,i+1)
    plt.plot(P[i].t,Os[i][:,0],color=colors[i],label="y(0)={} m , y'(0)={} m/s".format(P[i].ini[0],P[i].ini[1]))
    plt.title(' Oscilador {}, M= {} kg, K={} kg / $s^2$'.format(i+1,P[i].m,P[i].k))
    plt.xlabel("tiempo (s)")
    plt.ylabel("y (m)")
    plt.legend(loc=1)
plt.tight_layout()

plt.figure()
plt.figure(figsize=(14,6))
for i in np.arange(0,5,1):
    plt.subplot(1,5,i+1)
    plt.plot(Os[i][:,0],Os[i][:,1],color=colors[i],label="y(0)={} m , y'(0)={} m/s".format(P[i].ini[0],P[i].ini[1]))
    plt.title("Diag Fase, Osc. {}".format(i+1))
    plt.xlabel("y (m)")
    plt.ylabel("$V_y$ (m/s)")
    plt.legend(loc=1)
plt.tight_layout()



    


# In[8]:


#desde t=0 hasta t=10 

#osciladorAmortiguado(constante k, coeficiente de amortig b ,masa,  y0, v0 , t)

A1=OsciladorAmortiguado(1.5,1.5,1,3,2,10)
Oa1=OsciladorAmortiguado.SolucionAmort(A1)
A2=OsciladorAmortiguado(7,1.5,1,1,1,10)
Oa2=OsciladorAmortiguado.SolucionAmort(A2)
A3=OsciladorAmortiguado(5,2,4,1,10,10)
Oa3=OsciladorAmortiguado.SolucionAmort(A3)
A4=OsciladorAmortiguado(2,2,2,1,0,10)
Oa4=OsciladorAmortiguado.SolucionAmort(A4)
A5=OsciladorAmortiguado(5,1,5,2,5,10)
Oa5=OsciladorAmortiguado.SolucionAmort(A5)

#Grafiquemos
Oa=[Oa1,Oa2,Oa3,Oa4,Oa5]
A=[A1,A2,A3,A4,A5]
plt.figure(figsize=(7.5,7.5))
for i in np.arange(0,5,1):
    plt.subplot(5,1,i+1)
    plt.plot(A[i].t,Oa[i][:,0],color=colors[i],label="y(0)={} m , y'(0)={} m/s".format(A[i].ini[0],A[i].ini[1]))
    plt.title(' Oscilador Amort. {}, M= {} kg, K={} kg / $s^2$, b={} kg/s'.format(i+1,A[i].m,A[i].k,A[i].b))
    plt.xlabel("tiempo (s)")
    plt.ylabel("y (m)")
    plt.legend(loc=1)
plt.tight_layout()

plt.figure()
plt.figure(figsize=(14,6))
for i in np.arange(0,5,1):
    plt.subplot(1,5,i+1)
    plt.plot(Oa[i][:,0],Oa[i][:,1],color=colors[i],label="y(0)={} m , y'(0)={} m/s".format(A[i].ini[0],A[i].ini[1]))
    plt.title("Diag Fase, Osc. Amor. {}".format(i+1))
    plt.xlabel("y (m)")
    plt.ylabel("$V_y$ (m/s)")
    plt.legend(loc=1)
plt.tight_layout()



# In[24]:





# In[25]:





# In[ ]:




