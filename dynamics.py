"""
Created on Fri Apr  3 10:03:25 2020

@author: benja

This code generates some figures which are used in my teaching class in 
"Advanced Macroecnomics". 
In the figures, different dynamic adjustment cases for first-order difference
equations are shown
"""

# Load libraries
import numpy as np
import matplotlib.pyplot as plt
import os

# define time index
t = np.arange(0,11)

# lam = lambda captures the eigenvalues
lam     = [0.7, 1.3, -0.7, -1.3]
# Define labels for the dynamic adjustments
labs    = ['Monotonic Stable (MS)', 'Monotonic Unstable (MUS)',
           'Oscillatory Stable (OS)', 'Oscillatory Unstable (OUS)']
# Starting value
Y_0     = 110
# Steady State
Y_bar   = 100


def IRF(x0, xbar, t, l, lab):
# Compute general solution 
    x = (x0 - xbar)*np.power(l,t)+xbar
    x = np.array(x)
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
# Compute and Plot for the eigenvalues depicted in lam
for i,j,k in zip(lam, labs, np.arange(len(lam))): 
    Y = np.hstack((Y,IRF(Y_0, Y_bar, t, i, j)))
del i, j ,k  
# Brint the state variable in shape
Y = Y.reshape(len(lam), len(t)).T
