# -*- coding: utf-8 -*-
import module_locator

myPath = module_locator.module_path()

import numpy as np




#End time
t_end=2

#Time increment
h=0.1

#points
N=int(t_end/h+1)

#Time
t=np.linspace(0,t_end,N)

#Exact solution
x_true=np.exp(t**2/2)

with open(myPath+'/practice_true.csv','w', newline='')as f:
    f.write('time,Exact solution')
    f.write('\n')
    for i in range(N):
        f.write(str(t[i])+','+str(x_true[i]))
        f.write('\n')
        