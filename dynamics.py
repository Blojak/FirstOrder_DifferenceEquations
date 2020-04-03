# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 10:03:25 2020

@author: benja

This code generate some figures which are used in my teaching class in 
"Advanced Macroecnomics". 
In the figures, different dynamic adjustment cases for first-order difference
equations are shown
"""

import numpy as np
import matplotlib.pyplot as plt
import os


t = np.arange(0,11)

lam     = [0.7, 1.3, -0.7, -1.3]
labs    = ['Monotonic Stable (MS)', 'Monotonic Unstable (MUS)',
           'Oscillatory Stable (OS)', 'Oscillatory Unstable (OUS)']
Y_0     = 110
Y_bar   = 100

def IRF(x0, xbar, t, l, lab):
# Compute general solution 
    x = (x0 - xbar)*np.power(l,t)+xbar
    x = np.array(x)
    # print(x.dtype)
# plot
    fig, ax = plt.subplots()
    ax.plot(t,x, lw = 2)
    ax.scatter(t,x, color = 'black')
    ax.set_xlabel(r'$t=$time')
    ax.set_ylabel(r'$Y_t$', rotation =0)
    ax.set_xlim([0,t[-1]])
    ax.set_title(lab)
    ax.grid('on')
    ax.hlines(y=xbar, xmin = 0, xmax = t[-1], lw=1.0, color = 'black')
    a    = ax.get_yticks().tolist()
    a[1] = r'$\bar{Y}=$'+str(xbar)
    # print(a)
    if float(x0) in a:
        a_x0 = a.index(float(x0))
        a[a_x0] = r'$Y_{0}=$'+str(x0)
    ax.set_yticklabels(a)
    
    if not os.path.exists('fig'):
        os.makedirs('fig')
    fig.savefig('./fig/IRF'+lab + '.eps', bbox_inches='tight',dpi=50)
    return x

# Initialize    
Y = []
for i,j,k in zip(lam, labs, np.arange(len(lam))): 
    Y = np.hstack((Y,IRF(Y_0, Y_bar, t, i, j)))
del i, j ,k  
Y = Y.reshape(len(lam), len(t)).T
# 
# In newer versions of matplotlib, if you do not set the tick labels with a bunch of str values, they are '' by default (and when the plot is draw the labels are simply the ticks values). Knowing that, to get your desired output would require something like this:

# >>> from pylab import *
# >>> a=axes.get_xticks().tolist()
# >>> a[1]='change'
# >>> axes.set_xticklabels(a)