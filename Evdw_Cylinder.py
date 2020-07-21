#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tuesday July 20 05:07:01 2020

@author: Tanvir Chowdury
"""
import numpy as np
from scipy.special import ivp, kvp, kn, iv
import matplotlib.pyplot as plt


flag = eval(input('Press 1 if the adsorbate is NH3 or 0 if it is NO2: '))
# read data
din, Edft = np.loadtxt('type_1_NH3_PBE.txt',skiprows=5,unpack=True)
#E = np.empty(len(din))
Evdw = np.zeros(len(din))

a = 7.398 # tube radius
D = din*1.8897 # convert distance from Angstorm to au

w_p = 1.5834 # plasma frequency square
if flag == 1:
    w_1 = 2.6504 # molecular frequency square of NH3
    a_0 = 14.191 # static polarizibility of NH3
elif flag == 0:
    w_1 = 2.7003 # molecular frequency square of NO2
    a_0 = 19.6367 # static polarizibility of NO2
else:
    print('Invalid number. Please press either 0 or 1.')

N = 0.001 # number of increment
k = np.arange(N,30,N)
# for m from 1 to 30 images
for m in range(0,21):
    for j in range(len(k)): # integration over k
        C = iv(m,k[j]*a)/kn(m,k[j]*a)
        hm = (iv(m,k[j]*a)*kvp(m,k[j]*a))/(ivp(m,k[j]*a)*kn(m,k[j]*a))
        demon = w_p - (1 - hm) * w_1 # the denominator (w_p and w_1 are already squared)
        A = (a_0 * w_1 * w_p)/demon
        B = (-1) * (a_0 * w_1 * w_p * (1 - hm))/demon
        xi = kvp(m, k[j] * (D + a)) * k[j] # xi is an array same size as D
        if m==0:
            Evdw += (-1) * N * ( ( A/np.sqrt(w_1) ) + ( B/(np.sqrt(w_p*(1-hm))) ) ) * C * xi**2
        else:
            Evdw += (-2) * N * ( ( A/np.sqrt(w_1) ) + ( B/(np.sqrt(w_p*(1-hm))) ) ) * C * xi**2

E_reference =
b = np.arange(5,9,0.1)
absolute_error = np.zeros(len(b))
# from Hartress to eV
for i in range(len(b)):
    Evdw = Evdw * (1-np.exp(-D/b[i]))* 27.2114
    E_total = Edft + Evdw
    absolute_error[i] = abs(E_total.min() - E_reference)
    # store somewhere
    # another system calculate MAE again and add to this MAE
    # do this for all 8 systems and then you get the total MAE for this b
    # do the same for all b
    # plot b vs MAE and find optimal b


'''print('Total Energy (eV) = ',E_total)
print('E_b (meV) = ', 1000 * E_total.min())
# grab the index where Energy is minimum
ii = np.argmin(E_total)
# find d_min there
print('D_eq (A) = ', din[ii])

# this section will create a plot of the energies
plt.plot(din,Edft,linestyle='dashdot',linewidth=4,label='E_dft')
plt.plot(din,Evdw,linewidth=4,label='E_vdw')
plt.plot(din,E_total,linestyle='dashed',linewidth=4,label='E_total')
plt.xlabel('Distance (Angstrom)',fontsize=26)
plt.ylabel('Energy (meV)',fontsize=26)
plt.legend(loc='upper right',fontsize=17)
plt.rc('xtick',labelsize=26)
plt.rc('ytick',labelsize=26)
plt.show()
# write in a file
info = 'Absolute Errors'
info += '\nAuthor: Tanvir Chowdhury'
np.savetxt('error_type_1_NH3_PBE.txt',list(absolute_error), header=info,fmt='%20.8f')'''
