# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 14:01:39 2022

@author: Henry Song
"""

import numpy as np
import matplotlib.pyplot as plt
fig, axes = plt.subplots(figsize=(17,6),ncols=3)
data = []
fontsize_title = 24
fontsize_label = 24
fontsize_tick = 18
xlabel = [list('EIVYKSPVVS'),list('AEIVYKSPVVS'),list('AEIVPKSPVVS')]
name = [r'tauC $_{E391-S400}$',r'tauC $_{A390-S400}$',r'tauC mut-$_{A390-S400}$']
for i in [10,11]:
    data.append(np.loadtxt(f'tauC{i}-ctm.txt'))
data.append(np.loadtxt('mutauC11-ctm.txt'))
data = [x*15/6 for x in data]
max = max([x.max() for x in data])
print (max)
x_range = [10,11,11]
for i in range(3):
    ht = axes[i].imshow(data[i], origin='lower', vmin=0,vmax=max)
    axes[i].set_xticks(np.arange(0,x_range[i]))
    axes[i].set_xticklabels(xlabel[i],fontsize=fontsize_tick,family='Arial')
    axes[i].set_yticks(np.arange(0,x_range[i]))
    axes[i].set_yticklabels(xlabel[i],fontsize=fontsize_tick,family='Arial')
    #axes[i].set_title(name[i],fontsize=fontsize_title,family='Arial')
cbar=plt.colorbar(ht,ax=axes,shrink=0.8)
cbar.ax.tick_params(labelsize=fontsize_tick)
#cbar.set_label('Frequency',fontsize=fontsize_label,family='Arial')
plt.savefig('./figures/inter-chain_ctmap.png',dpi=220,transparent=True)
plt.show()