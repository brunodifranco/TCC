# Módulo grafico

import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import norm
import numpy as np

def graph(X,y,save_figure=0,a=10,b=5):
    if save_figure==0:
        plt.figure(figsize=(a,b)) 
        plt.plot(X)
        plt.ylabel(y, fontsize=11)
        plt.xlabel('Time', fontsize=11)
        plt.show()
    elif save_figure==1:
        plt.figure(figsize=(a,b)) 
        plt.plot(X)
        plt.ylabel(y, fontsize=11)
        plt.xlabel('Time', fontsize=11)
        plt.savefig('{y}.pdf'.format(y=y),bbox_inches='tight')
        plt.show() 
          
def histogram(X,y,save_figure=0,a=10,b=5,bins=25):
    if save_figure==0:
        fig, ax = plt.subplots(figsize = (a,b))
        X.plot(kind = "hist", density = True, bins=bins)
        X.plot(kind = "kde")
        ax.set_xlabel(y, fontsize=11)
        plt.show()
    elif save_figure==1:
        fig, ax = plt.subplots(figsize = (a,b))
        X.plot(kind = "hist", density = True, bins=bins)
        X.plot(kind = "kde")
        ax.set_xlabel(y, fontsize=11)
        plt.savefig('{y}.pdf'.format(y=y),bbox_inches='tight')
        plt.show()
        
def csd_parametric(X,y,save_figure=0,a=10,b=5):
    if save_figure==0:
        plt.figure(figsize=(a,b)) 
        plt.plot(X)
        plt.ylabel(y, fontsize=11)
        plt.xlabel('Time', fontsize=11)
        plt.axhline(X.mean(),color='r') # linha horizontal com a média
        plt.axhline(X.mean() + 2*X.std(),color='g') # linha horizontal com o limite superior
        plt.axhline(X.mean() - 2*X.std(),color='g') # linha horizontal com o limite inferior
        plt.show()
    elif save_figure==1:
        plt.figure(figsize=(a,b)) 
        plt.plot(X)
        plt.ylabel(y, fontsize=11)
        plt.xlabel('Time', fontsize=11)
        plt.axhline(X.mean(),color='r') # linha horizontal com a média
        plt.axhline(X.mean() + 2*X.std(),color='g') # linha horizontal com o limite superior
        plt.axhline(X.mean() - 2*X.std(),color='g') # linha horizontal com o limite inferior
        plt.savefig('{y}.pdf'.format(y=y),bbox_inches='tight')
        plt.show()
        
def csd_non_parametric(X,y,save_figure=0,a=10,b=5):
    if save_figure==0:
        plt.figure(figsize=(a,b)) 
        plt.plot(X)
        plt.ylabel(y, fontsize=11)
        plt.xlabel('Time', fontsize=11)
        plt.axhline(X.mean(),color='r') # linha horizontal com a média
        plt.axhline(X.quantile(0.95),color='g') # linha horizontal com o limite superior
        plt.axhline(X.quantile(0.05),color='g') # linha horizontal com o limite inferior
        plt.show()
    elif save_figure==1:
        plt.figure(figsize=(a,b)) 
        plt.plot(X)
        plt.ylabel(y, fontsize=11)
        plt.xlabel('Time', fontsize=11)
        plt.axhline(X.mean(),color='r') # linha horizontal com a média
        plt.axhline(X.quantile(0.95),color='g') # linha horizontal com o limite superior
        plt.axhline(X.quantile(0.05),color='g') # linha horizontal com o limite inferior
        plt.savefig('{y}.pdf'.format(y=y),bbox_inches='tight')
        plt.show() 
        
def graph_pvalue(X,y,save_figure=0,a=10,b=5):
    if save_figure==0:
        plt.figure(figsize=(a,b)) 
        plt.plot(X, '--bo')
        plt.ylabel(y, fontsize=11)
        plt.xlabel('Lags', fontsize=11)
        plt.axhline(0.05,color='g',linestyle='dashed')
        plt.yticks([0.05,0.15,0.30,0.45,0.60,0.75,0.90])  
        plt.ylim(0.005)
        plt.show()
    elif save_figure==1:
        plt.figure(figsize=(a,b)) 
        plt.plot(X, '--bo')
        plt.ylabel(y, fontsize=11)
        plt.xlabel('Lags', fontsize=11)
        plt.axhline(0.05,color='g',linestyle='dashed')
        plt.yticks([0.05,0.15,0.30,0.45,0.60,0.75,0.90]) 
        plt.ylim(0.005)
        plt.savefig('{y}.pdf'.format(y=y),bbox_inches='tight')
        plt.show()    
