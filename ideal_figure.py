#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 01:28:31 2020

@author: tanvir
"""
import numpy as np
import matplotlib.pyplot as plt

# read csv file
d, oneL, twoL, fourL = np.loadtxt("corona.csv", skiprows=1 , unpack=True, delimiter=',')
plt.plot(d,oneL,linestyle='dashdot',linewidth=4,label='MoS2 1 Layer; c = 3.1 Angstrom')
plt.plot(d,twoL,linewidth=4,label='MoS2 2 Layers; c = 9.2 Angstrom')
plt.plot(d,fourL,linestyle='dashed',linewidth=4,label='MoS2 4 Layers; c = 21.5 Angstrom')
plt.xlabel('Adsorption Distance (D/Angstrom)',fontsize=26)
plt.ylabel('vdw Power Law',fontsize=26)
plt.ylim(-4.1, -2.8)
plt.legend(frameon=False,loc='upper right',fontsize=17)
plt.rc('xtick',labelsize=26)
plt.rc('ytick',labelsize=26)
plt.show()
