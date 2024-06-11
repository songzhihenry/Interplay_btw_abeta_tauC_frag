#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 11:18:52 2022

@author: zhiyuas
"""

import numpy as np
def get_oligomer_beta_size(data_cluster,data_stru):
    data_cl = []
    for i in data_cluster:
        data_cl.append([j.split(',') for j in i])
    beta_size = []
    oli_size = []
    for i in range(len(data_stru)):
        for group in data_cl[i]:
            no_chains = len(group)
            no_beta = 0
            len_group = 0
            for chain in group:
                no_beta = no_beta + data_stru[i][int(chain)].count('E')
                len_group = len_group + len(data_stru[i][int(chain)])
            for chain in group:
                oli_size.append(no_chains)
                beta_size.append(no_beta/len_group*100)
    return oli_size, beta_size
def oli_rg_beta(data,data_stru):
    oli_size = []
    rg = []
    beta_size = []
    for i in range(len(data)):
        for group in data[i]:
            chains = group.split(':')[0].split(',')
            chains_rg = group.split(':')[1]
            no_beta = 0
            len_group = 0
            for chain in chains:
                no_beta = no_beta + data_stru[i][int(chain)].count('E')
                len_group = len_group + len(data_stru[i][int(chain)])
                oli_size.append(len(chains))
                rg.append(float(chains_rg))
            for chain in chains:
                beta_size.append(no_beta/len_group*100)
    return oli_size, rg, beta_size
#'''
for path in [10,11]:
    stru = []
    cluster = []
    for i in range(50):
        stru.extend([line.strip('\n').split()[1].split('!') for line in open('./data_all/16tauC{}-{}.dssp'.format(path,i+1))][-120000:])
        cluster.extend([line.strip('\n').split()[1:] for line in open('./data_all/16tauC{}-{}.cl'.format(path,i+1))][-120000:])
        #data.extend([line.strip('\n').split()\
         #            for line in open('./data_all/16tauC{}-{}.rg'.format(path,i+1))][-100000:])
    oli_size, beta_size = get_oligomer_beta_size(cluster,stru)
    a,_,_ = np.histogram2d(beta_size,oli_size,bins=[path,16],range=[[0,100],[1,17]])
    a = a/np.sum(a)
    #np.savetxt('prob_beta_cl_{}.txt'.format(path),a)
    np.savetxt('pmf_beta_cl_{}.txt'.format(path),-np.log(np.where(a == 0, 1e-10, a)))
    '''
    a,b,_ = np.histogram2d(rg,oli_size,bins=[30,16],range=[[min(rg)*0.99,max(rg)*1.01],[1,17]])
    a = a/np.sum(a)
    np.savetxt('pmf_rg_cl_{}.txt'.format(path),-np.log(np.where(a == 0, 1e-10, a)))
    np.savetxt(f'rg_range_{path}.txt',b)
    a,_,_ = np.histogram2d(beta_size,rg,bins=[path,30],range=[[0,100],[min(rg)*0.99,max(rg)*1.01]])
    np.savetxt('pmf_beta_rg_{}.txt'.format(path),-np.log(np.where(a == 0, 1e-10, a)))
    '''
#'''
path = 11
stru = []
cluster = []
for i in range(50):
    stru.extend([line.strip('\n').split()[1].split('!') for line in open('./data_all/16mutauC{}-{}.dssp'.format(path,i+1))][-120000:])
    cluster.extend([line.strip('\n').split()[1:] for line in open('./data_all/16mutauC{}-{}.cl'.format(path,i+1))][-120000:])
    #data.extend([line.strip('\n').split()\
     #            for line in open('./data_all/16mutauC{}-{}.rg'.format(path,i+1))][-100000:])
oli_size, beta_size = get_oligomer_beta_size(cluster,stru)
a,_,_ = np.histogram2d(beta_size,oli_size,bins=[path,16],range=[[0,100],[1,17]])
a = a/np.sum(a)
np.savetxt('pmf_beta_cl_mu{}.txt'.format(path),-np.log(np.where(a == 0, 1e-10, a)))
#a,b,_ = np.histogram2d(rg,oli_size,bins=[30,16],range=[[min(rg)*0.99,max(rg)*1.01],[1,17]])
#a = a/np.sum(a)
#np.savetxt('pmf_rg_cl_mu{}.txt'.format(path),-np.log(np.where(a == 0, 1e-10, a)))
#np.savetxt(f'rg_range_mu{path}.txt',b)
#a,_,_ = np.histogram2d(beta_size,rg,bins=[path,30],range=[[0,100],[min(rg)*0.99,max(rg)*1.01]])
#np.savetxt('pmf_beta_rg_mu{}.txt'.format(path),-np.log(np.where(a == 0, 1e-10, a)))
#'''