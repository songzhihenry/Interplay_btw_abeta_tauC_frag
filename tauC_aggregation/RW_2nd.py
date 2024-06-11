#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 14:08:25 2022

@author: zhiyuas
"""

import numpy as np
import matplotlib.pyplot as plt
fontsize_title = 20
fontsize_label = 20
fontsize_tick = 25
data = []
err = []
for i in [10,11]:
    data.append(np.loadtxt(f'./RW_2nd_tauC{i}.txt')[:,[1,3,5,7]].T)
    err.append(np.loadtxt(f'./RW_2nd_tauC{i}.txt')[:,[2,4,6,8]].T)
data.append(np.loadtxt('./RW_2nd_mutauC11.txt')[:,[1,3,5,7]].T)
err.append(np.loadtxt('./RW_2nd_mutauC11.txt')[:,[2,4,6,8]].T)
fig,axes = plt.subplots(figsize=(14,6),nrows=2,ncols=2)
fig.subplots_adjust(hspace=0.5)
axes = axes.flatten()
names = ['helices','β sheets','coils','turns']
label = [r'tauC $_{E391-S400}$',r'tauC $_{A390-S400}$',r'tauC mut-$_{A390-S400}$']
mu_list = ['A','E','I','V','Y(P)','K','S','P','V','V','S']
xlabel = [list('EIVYKSPVVS'),mu_list,mu_list]
x_range = [1,0,0]
for i in range(4):
    axes[i].spines['top'].set_visible(False)
    axes[i].spines['right'].set_visible(False)
    #axes[i].set_title(names[i],fontsize=fontsize_title)
    for j in range(3):
        axes[i].plot(np.arange(x_range[j],11),data[j][i],label=label[j],linewidth=3)
        axes[i].errorbar(np.arange(x_range[j],11),data[j][i],yerr=err[j][i],fmt='none',capsize=1,ecolor='grey')
        axes[i].set_xticks(np.arange(x_range[j],11))
        axes[i].set_xticklabels(xlabel[j],fontsize=fontsize_tick)
#for i in range(2):
#    axes[i*2].set_ylabel('proensity(%)',fontsize=fontsize_label)
#plt.legend(frameon=False,fontsize=16,bbox_to_anchor=(0.65, 3.0),ncol=3)
plt.savefig('RW_2ndst.png',dpi=220,transparent=True)