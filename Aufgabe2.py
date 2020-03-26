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

def func(t,a,b):
    return (a * np.exp(-t/b))

time = [0.01,3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48,51,54,57,60,63,66,69,72,75,78,81,84,87,90,93,96,99,102,105,108,111,114,117,120,123,126,129,132,135,138,141,144,147,150,153,156,159,162,165,168,171,174,177,180,183,186,189,192,195,198,201,204,207,210,213,216,219,222,225,228,231,234,237,240,243,246,249,252,255,258,261,264,267,270,273,276,279,282,285,288,291,294,297,300]
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

#cCounts_data=np.array(unumpy.nominal_values(cCounts),dtype=float)
#cTime_data=np.array(unumpy.nominal_values(cTime),dtype=float)

cCounts_data=unumpy.nominal_values(cCounts)
cTime_data=unumpy.nominal_values(cTime)


cCounts_error= unumpy.std_devs(cCounts)
cTime_error= unumpy.std_devs(cTime)

popt,pcov = curve_fit(func,cTime_data,cCounts_data)#cTime_data, cCounts_data)
perr=np.sqrt(np.diag(pcov))
print(popt)

plt.figure(1)
plt.plot(cTime_data,cCounts_data)
plt.plot(cTime_data,func(cTime_data,*popt))
plt.show()


