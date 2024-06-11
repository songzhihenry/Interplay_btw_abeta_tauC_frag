#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 16:56:37 2022

@author: zhiyuas
"""

import numpy as np
import matplotlib.pyplot as plt
fontsize_label = 20
fontsize_title = 20
fontsize_tick = 16
fontsize_legend = 14
fig,axes = plt.subplots(figsize=(8,12),ncols=1,nrows=3)
fig.subplots_adjust(hspace=0.3)
data = {'cv':{},'end':{},'side':{},'resct':{}}
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
for path in ['f_tau_m_Ab','m_tau_f_Ab']:
    data['cv'].update({path:np.loadtxt(f'tauC10/{path}/cv.dat').T})
    for f in ['end','side']:
        data[f].update({path:np.loadtxt(f'tauC10/{path}/ave_{f}ct.dat').T})
data['cv'].update({'m_tau_m_Ab':np.loadtxt(f'tauC10/m_tau_m_Ab/cv.dat').T })
data['resct'].update({'m_tau_m_Ab':np.loadtxt(f'tauC10/m_tau_m_Ab/ave_resct.dat').T}) 
#titles = [r'tauC$_{seed}$ + Aβ$_{monomer}$',r'tauC$_{monomer}$ + Aβ$_{seed}$'] 
names = [r'tauC$_{seed}$ + Aβ$_{monomer}$',r'tauC$_{monomer}$ + Aβ$_{seed}$']#,r'tauC$_{monomer}$ + Aβ$_{seed}$']
labels = ['Elongation','Lateral']#,'Monomers']
linewidth=2
for ax in axes:
    ax.spines[['right', 'top']].set_visible(False)
    ax.tick_params(axis='both',labelsize=fontsize_tick)
for i,path in enumerate(['f_tau_m_Ab','m_tau_f_Ab',]):
    axes[0].plot(data['cv'][path][0],data['cv'][path][1]*500,color = colors[i],linewidth=linewidth,label=names[i])
    axes[i+1].set_title(names[i],fontsize=fontsize_title, color=colors[i],loc='right')
    axes[i+1].set_ylabel('Residue contacts', fontsize=fontsize_label)
    for j,F in enumerate(['end','side']):
        axes[i+1].plot(data[F][path][0],data[F][path][1],color = colors[3+j],label=labels[j],linewidth=linewidth)
        axes[i+1].errorbar(data[F][path][0],data[F][path][1], yerr=(data[F][path][2]/16)**0.5,\
        fmt='none',capsize=1,ecolor='lightgrey')
    axes[i+1].plot(data['resct']['m_tau_m_Ab'][0],data['resct']['m_tau_m_Ab'][1],color = 'darkgrey',label='Monomers',linewidth=linewidth)
    axes[i+1].errorbar(data['resct']['m_tau_m_Ab'][0],data['resct']['m_tau_m_Ab'][1], yerr=(data[F][path][2]/16)**0.5,\
        fmt='none',capsize=1,ecolor='lightgrey') 
axes[0].plot(data['cv']['m_tau_m_Ab'][0],data['cv']['m_tau_m_Ab'][1]*500,color = colors[2],linewidth=linewidth,label=r'tauC$_{monomer}$ + Aβ$_{monomer}$')
axes[2].set_xlabel('Temperature (K)',fontsize=fontsize_label)
axes[0].legend(frameon=False,fontsize=fontsize_legend)
axes[1].legend(frameon=False,fontsize=fontsize_legend+2)
axes[0].set_ylabel(r'$C_{V}, k_{B}$', fontsize=fontsize_label)
'''
for i,path in enumerate(['f_tau_m_Ab','m_tau_f_Ab']):
    axes[0,0].plot(data['cv'][path][0],data['cv'][path][1],color = colors[i])
    #axes[0,i].errorbar(data['cv'][path][0],data['cv'][path][1], yerr=(data['cv'][path][2]/16)**0.5,\
    #    fmt='none',capsize=1,ecolor='lightgrey')
    for j,F in enumerate(['end','side']):
        axes[1,i].plot(data[F][path][0],data[F][path][1],color = colors[2+j],label=labels[j])
        axes[1,i].errorbar(data[F][path][0],data[F][path][1], yerr=(data[F][path][2]/16)**0.5,\
        fmt='none',capsize=1,ecolor='lightgrey')
        axes[i,j].tick_params(axis='both',labelsize=fontsize_tick)
    axes[1,i].set_title(names[i],fontsize=fontsize_title, color=colors[i])
    axes[1,i].set_xlabel('temperature (K)',fontsize=fontsize_label)
axes[1,0].legend(frameon=False,fontsize=fontsize_label)
axes[0,0].set_ylabel(r'$C_{V}, k_{B}$', fontsize=fontsize_label)
axes[1,0].set_ylabel('residue contacts', fontsize=fontsize_label)
'''

#plt.savefig('E_L_binding.png',dpi=400)
plt.show()