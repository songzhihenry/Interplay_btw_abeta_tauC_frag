#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 13:16:37 2022

@author: zhiyuas
"""
import numpy as np
import matplotlib.pyplot as plt
fontsize_label = 20
fontsize_title = 20
fontsize_tick = 16
data = []
for path in ['f_tau_m_Ab', 'm_tau_f_Ab', 'm_tau_m_Ab']:
    #'''
    data.append(np.loadtxt(f'tauC10/{path}/ave_resct.dat').T)
    #tauC11.append(np.loadtxt(f'tauC11/{path}/ave_resct.dat').T)
    '''
    tauC10.append(np.loadtxt(f'tauC10/{path}/ave_bind.dat').T)
    #tauC11.append(np.loadtxt(f'tauC11/{path}/ave_bind.dat').T)
    '''
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
plt.figure(figsize=(12,6))
names = [r'tauC$_{seed}$ + Aβ$_{monomer}$',r'tauC$_{monomer}$ + Aβ$_{seed}$',r'tauC$_{monomer}$ + Aβ$_{monomer}$']
for j in range(3):
    plt.plot(data[j][0],data[j][1],color=colors[j],label=names[j],linewidth=3)
    plt.errorbar(data[j][0],data[j][1],yerr=(data[j][2]/16)**0.5,fmt='none',capsize=1,ecolor='lightgrey')
plt.title(r'tauC $_{E391-S400}$',fontsize=fontsize_title)
plt.ylabel('residue contacts', fontsize=fontsize_label)
plt.tick_params(axis='both',labelsize=fontsize_tick)
plt.xlabel('temperature (K)',fontsize=fontsize_label)
plt.legend(frameon=False,fontsize=fontsize_tick,loc='best')
plt.savefig('binding_probablity_vs_temp.png',dpi=220)
#plt.show()