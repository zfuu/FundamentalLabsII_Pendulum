# -*- coding: utf-8 -*-
import module_locator

myPath = module_locator.module_path()

import numpy as np
t_end=10
h=0.0000001
N=int(t_end/h+1)

G=9.745
L=1.843337

t=np.linspace(0,t_end,N)
omega=np.linspace(0,t_end,N)
theta=np.linspace(0,t_end,N)

omega[0]=0
theta[0]=30/180*np.pi

for i in range(N-1):
    k1=h*(-G/L*np.sin(theta[i]))
    m1=h*omega[i]
    k2=h*(-G/L*np.sin(theta[i])+m1/2)
    m2=h*(omega[i]+k1/2)
    k3=h*(-G/L*np.sin(theta[i])+m2/2)
    m3=h*(omega[i]+k2/2)
    k4=h*(-G/L*np.sin(theta[i])+m3)
    m4=h*(omega[i]+k3)
    omega[i+1]=omega[i]+(k1+2*k2+2*k3+k4)/6
    theta[i+1]=theta[i]+(m1+2*m2+2*m3+m4)/6
    
with open(myPath+'/period_RungeKutta_h='+str(h)+'.csv','w',newline='')as f:
    f.write('time,h='+str(h))
    f.write('\n') 
    for i in range(N):
        # print(t[i])
        # if (t[i]%0.5 <= h):
        if (t[i]%0.5 ==0):
            f.write(str(t[i])+','+str(theta[i]))
            f.write('\n')