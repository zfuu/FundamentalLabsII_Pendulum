# -*- coding: utf-8 -*-
import module_locator

myPath = module_locator.module_path()

import numpy as np

#End time
t_end=2

#Time increment
# h=0.1
h=0.01

#points
N=int(t_end/h+1)

#Time
t=np.linspace(0,t_end,N)

#Exact solution
x=np.linspace(0,t_end,N)

x[0]=1
for i in range(N-1):
    k=h*t[i]*x[i]
    x[i+1] = x[i]+k

# with open(myPath+'/practice_Euler1.csv','w',newline='')as f:
with open(myPath+'/practice_Euler1_smaller_h.csv','w',newline='')as f:
    f.write('time,h='+str(h))
    f.write('\n')
    for i in range(N):
        f.write(str(t[i])+','+str(x[i]))
        f.write('\n')