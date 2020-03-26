from __future__ import unicode_literals
from uncertainties import *
from uncertainties import unumpy
import matplotlib.pyplot as plt
import numpy as np
import os
import matplotlib
from scipy.optimize import curve_fit
from mpl_toolkits.mplot3d import Axes3D
import scipy.odr.odrpack as odrpack
from matplotlib import rc
rc('text', usetex=True)



def func(t,a,b):#wichtig variable also erste schreiben damit die funktion weiß was die Parameter sind
    return (a * np.exp(-t/b))

def f(B, x):
    return B[0]*x + B[1]


time = [0,3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48,51,54,57,60,63,66,69,72,75,78,81,84,87,90,93,96,99,102,105,108,111,114,117,120,123,126,129,132,135,138,141,144,147,150,153,156,159,162,165,168,171,174,177,180,183,186,189,192,195,198,201,204,207,210,213,216,219,222,225,228,231,234,237,240,243,246,249,252,255,258,261,264,267,270,273,276,279,282,285,288,291,294,297,300]
counts =[14,20,19,20,15,17,13,13,16,10,12,11,10,11,8,8,10,9,11,8,12,5,6,4,8,6,8,9,9,5,8,10,4,4,3,3,5,1,4,4,2,6,6,10,0,5,2,1,2,3,2,1,0,2,2,5,4,1,2,2,3,0,2,3,2,2,1,1,1,2,1,1,3,4,1,3,3,1,1,1,3,1,0,2,0,0,1,1,1,1,0,0,3,0,0,0,1,1,1,2,0]
counts_err=np.ones_like(counts)
counts_err[0:32]=2
cCounts=[]
cTime=[]
counts=unumpy.uarray(counts,counts_err)
#print(counts)
k=0
for i in range(len(time)):
    #print(k)
    temp=counts[k:k+4]
    cCounts=np.append(cCounts,np.sum(temp))
    cTime=np.append(cTime,time[k])
    #print(temp)
    k += 4
    if k >= len(time):
        break

cCounts_data=np.array(unumpy.nominal_values(cCounts),dtype=float)
cTime_data=np.array(unumpy.nominal_values(cTime),dtype=int)

cCounts_error= unumpy.std_devs(cCounts)
cTime_error= unumpy.std_devs(cTime)
time=np.array(time)
counts=np.array(unumpy.nominal_values(counts))

#print(time)
#print(cTime_data)

#print(counts)
#print(cCounts_data)

y=np.array([73,58,49,37,38,27,31,32,14,14,24,8,8,9,9,8,6,5,11,6,6,2,2,3,5,0])
x=np.array([0,12,24,36,48,60,72,84,96,108,120,132,144,156,168,180,192,204,216,228,240,252,264,276,288,300])

#y=np.array([73,58,49,37,38,27])
#x=np.array([0.1,12,24,36,48,60])

popt,pcov = curve_fit(func,x,y)#cTime_data, cCounts_data)
perr=np.sqrt(np.diag(pcov))
print(popt)

plt.figure(1)
plt.plot(x,y)
plt.plot(x,func(x,*popt))
plt.show()


