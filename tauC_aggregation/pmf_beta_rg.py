#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 16:50:00 2022

@author: zhiyuas
"""

import numpy as np
import matplotlib.pyplot as plt

#colors = ('#313695','#4575b4','#74add1','#abd9e9','#e0f3f8','#ffffbf','#fee090','#fdae61','#f46d43','#d73027','#a50026')
font_title = 17
font_label = 20
font_tick = 10
#levels =  np.arange(0,12)

names = [10,11]
names1=[r'tau$_{391-400}$',r'tau$_{390-400}$','mut-tau$_{390-400}$']
rgrange = [np.loadtxt('./rg_range_{}.txt'.format(i)) for i in names]
pmf = [np.loadtxt('./pmf_beta_rg_{}.txt'.format(i)) for i in names]
rgrange.append(np.loadtxt('./rg_range_mu11.txt'))
pmf.append(np.loadtxt('pmf_beta_rg_mu11.txt'))
pmf = [x-x[0,0] for x in pmf]
pmf = [x-x.min() for x in pmf]

fig,axes = plt.subplots(figsize=(16,12),nrows=1,ncols=3)
axes = axes.flatten()
rg_max = max(rgrange[0][-1],rgrange[1][-1])
rg_min = min(rgrange[0][0],rgrange[1][0])
for i in range(3):
    heatmap = axes[i].contourf(pmf[i],extent=[rgrange[i][0],rgrange[i][-1],0,100],cmap='jet',levels=np.arange(15))
    axes[i].set_title(names1[i],fontsize=font_title)
    #axes[i].set_xticks(rgrange[i])
    axes[i].set_yticks(np.arange(0,11)*10)
    axes[i].spines['top'].set_visible(False)
    axes[i].spines['right'].set_visible(False)
    axes[i].tick_params(axis='both',labelsize=font_tick)
    axes[i].set_xlabel('rg',fontsize=font_label)
    axes[i].set_xlim(rg_min,rg_max)
axes[0].set_ylabel('β sheet content (%)',fontsize=font_label)
cb = plt.colorbar(heatmap,ax=axes[i],fraction=0.1,shrink=0.7)
cb.set_label(r'$k_{B}T$',fontsize=font_label)
cb.ax.tick_params(labelsize=font_tick)
plt.savefig('beta_rg_kinetics.png',dpi=220)