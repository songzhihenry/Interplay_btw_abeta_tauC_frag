#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 13:18:21 2022

@author: zhiyuas
"""

import numpy as np
import matplotlib.pyplot as plt

#colors = ('#313695','#4575b4','#74add1','#abd9e9','#e0f3f8','#ffffbf','#fee090','#fdae61','#f46d43','#d73027','#a50026')
font_title = 24
font_label = 22
font_tick = 16
#levels =  np.arange(0,12)

names = [10,11]
names1=[r'tauC $_{E391-S400}$',r'tauC $_{A390-S400}$',r'tauC mut-$_{A390-S400}$']
pmf = [np.loadtxt('./pmf_beta_cl_{}.txt'.format(i)) for i in names]
pmf.append(np.loadtxt('pmf_beta_cl_mu11.txt'))
pmf = [x-x[0,0] for x in pmf]
pmf = [x-x.min() for x in pmf]
pmf = [np.vstack((np.ones(len(x[0]))*50,x)) for x in pmf]
pmf = [np.hstack((np.ones((len(x),1))*50,x)) for x in pmf]
#print (pmf[0])
#Z = [np.loadtxt('./prob_beta_cl_{}.txt'.format(i)) for i in names]
#print (np.size(pmf[0]))
#print ("f: ",np.sum(Z[1][4:8,4:8]))
#print ("g", np.sum(Z[1][4:9,9:]))
#'''
fig,axes = plt.subplots(figsize=(20,6),nrows=1,ncols=3)
axes = axes.flatten()

for i in range(3):
    #heatmap = axes[i].contourf(pmf[i],extent=[0,17,-10,100],cmap='jet',levels=np.arange(15))
    heatmap = axes[i].contourf(pmf[i],cmap='jet',levels=np.arange(15))
    axes[i].set_title(names1[i],fontsize=font_title,family='Arial')
    axes[i].set_xticks(np.arange(0,17,2))
    axes[i].set_xticklabels(np.arange(0,17,2),family='Arial')
    if i == 0:
       axes[i].set_yticks(np.arange(0,11)+0.5) 
       axes[i].set_yticklabels(np.arange(0,11)*10,family='Arial') 
    else:
        axes[i].set_yticks(np.arange(0,12)+0.5*10/11)
        axes[i].set_yticklabels(['%.1f'%x for x in np.arange(0,12)*100/11],family='Arial') 
    axes[i].spines['top'].set_visible(False)
    axes[i].spines['right'].set_visible(False)
    axes[i].tick_params(axis='both',labelsize=font_tick)
    axes[i].set_xlabel(r'$n_{cluster}$',fontsize=font_label,family='Arial')
axes[0].set_ylabel('β sheet content (%)',fontsize=font_label,family='Arial')
cb = plt.colorbar(heatmap,ax=axes[i],fraction=0.1,shrink=0.7)
cb.set_label(r'$k_{B}T$',fontsize=font_label,family='Arial')
cb.ax.tick_params(labelsize=font_tick)
#plt.show()
plt.savefig('beta_cluster_kinetics.png',dpi=300)
#'''