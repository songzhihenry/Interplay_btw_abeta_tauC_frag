#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 14:03:01 2022

@author: zhiyuas
"""

import numpy as np
import matplotlib.pyplot as plt
import os
def dssp_content(data):
    data_t = np.zeros((4,len(data)))
    for i in range(len(data)):
        hang = [x for x in list(data[i]) if x != '!']
        helix = hang.count('H') + hang.count('G') + hang.count('I')
        beta = hang.count('E')
        turn = hang.count('T')
        unstr = len(hang) - helix - beta - turn
        data_t[0][i] = helix
        data_t[1][i] = beta
        data_t[2][i] = turn
        data_t[3][i] = unstr
    return data_t/len(hang)*100
tau = []
content = []
content_err = []
fontsize_tick = 16
fontsize_label = 20
posi = 0
#stru_type: 0:helix; 1:beta; 2:turn; 3:unstru
stru_type = 1
stru_name = ['helix', 'β sheet','turn','coil']
min_len = min([int(x) for x in os.popen("wc -l data_all/*.dssp | awk '{print $1}'").read().split('\n')[:-1]])
#time evo
for path in ['16tauC11', '16tauC10','16mutauC11']:
    #stru_time_evo = np.zeros((1500,50))
    #sec_con = np.zeros(50)
    stru_time_evo = []
    sec_con = []
    for i in range(50):
        data = dssp_content([line.strip('\n').split()[1] for line in open('data_all/{}-{}.dssp'.format(path,i+1))][:min_len:100])[stru_type]
        sec_con.append(np.mean(data[800:]))
        stru_time_evo.append(data)
    tau.append(np.array(stru_time_evo))
    content.append(np.mean(np.array(sec_con)))
    content_err.append(np.std(sec_con)/len(sec_con)**0.5)

time = np.arange(1,len(stru_time_evo[0])+1)*0.5
#content

#setup distribution
fig = plt.figure(figsize=(22,6))
grid = plt.GridSpec(6,22,hspace=0,wspace=0)
axes = []
axes.append(fig.add_subplot(grid[:, :13]))
axes.append(fig.add_subplot(grid[:, 14:],sharey=axes[0]))
#defaut colors=['#1f77b4','#ff7f0e','#2ca02c','#d62728','#9467bd','#8c564b', '#e377c2']
colors=['#1f77b4','#ff7f0e','#2ca02c','#d62728']#,'#9467bd','#8c564b', '#e377c2']
#names=[r'tau$_{390-400}$Y394P',r'tau$_{390-400}$',r'tau$_{391-400}$Y394P',r'tau$_{391-400}$']
names=[r'tauC $_{A390-S400}$', r'tauC $_{A391-S400}$',r'mut-tauC $_{E390-S400}$']
for k in range(3):
    axes[0].errorbar(time, np.mean(tau[k],axis=0),yerr = np.std(tau[k],axis=0)/50**0.5,fmt='none',\
                 ecolor='lightgrey',elinewidth=1,capsize=1)
    axes[0].plot(time, np.mean(tau[k],axis=0),label=names[k],linewidth=2,color=colors[k])
for k in range(2):
    axes[k].spines['top'].set_visible(False)
    axes[k].spines['right'].set_visible(False)
    axes[k].tick_params(axis='both', labelsize=fontsize_tick)
axes[1].bar([r'tauC$_{A390-S400}$', r'tauC$_{E391-S400}$',r'mut-tauC$_{A390-S400}$'],\
            content,color=colors,yerr=content_err,error_kw = {'ecolor' : 'k', 'capsize' :2})
axes[0].set_xlabel('Time (ns)', fontsize=fontsize_label)
axes[0].set_ylabel(stru_name[stru_type]+' content (%)', fontsize=fontsize_label)
#axes[0].legend(frameon=False,fontsize=fontsize_tick,ncol=2)
#axes[0].set_xlabel('Time (ns)', fontsize=fontsize_label)
#axes[0].set_ylabel(stru_name[stru_type]+' content (%)', fontsize=fontsize_label)
plt.savefig('{}-time-evo.png'.format(stru_name[stru_type]),dpi=220)