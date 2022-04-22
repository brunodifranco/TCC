# Módulo grafico

import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import norm
import numpy as np

def fazer_graficos(X,y,salvar_figura=0,a=10,b=5):
    # X são os valores propriamente do gráfico, ex: df[i]
    # y é o rótulo, ex: 'i'
    if salvar_figura==0:
        plt.figure(figsize=(a,b)) 
        plt.plot(X)
        plt.ylabel(y, fontsize=11)
        plt.xlabel('Time', fontsize=11)
        plt.show()
    elif salvar_figura==1:
        plt.figure(figsize=(a,b)) 
        plt.plot(X)
        plt.ylabel(y, fontsize=11)
        plt.xlabel('Time', fontsize=11)
        plt.savefig('{y}.pdf'.format(y=y),bbox_inches='tight')
        plt.show() 
          
def histograma(X,y,salvar_figura=0,a=10,b=5,bins=25):
    # X são os valores propriamente do gráfico, ex: df[i]
    # y é o rótulo, ex: histograma de i
    if salvar_figura==0:
        fig, ax = plt.subplots(figsize = (a,b))
        X.plot(kind = "hist", density = True, bins=bins)
        X.plot(kind = "kde")
        ax.set_xlabel(y, fontsize=11)
        plt.show()
    elif salvar_figura==1:
        fig, ax = plt.subplots(figsize = (a,b))
        X.plot(kind = "hist", density = True, bins=bins)
        X.plot(kind = "kde")
        ax.set_xlabel(y, fontsize=11)
        plt.savefig('{y}.pdf'.format(y=y),bbox_inches='tight')
        plt.show()
        
def csd_parametric(X,y,salvar_figura=0,a=10,b=5):
    # X são os valores propriamente do gráfico, ex: df[i]
    # y é o rótulo, ex: 'i'
    if salvar_figura==0:
        plt.figure(figsize=(a,b)) 
        plt.plot(X)
        plt.ylabel(y, fontsize=11)
        plt.xlabel('Time', fontsize=11)
        plt.axhline(X.mean(),color='r') # linha horizontal com a média
        plt.axhline(X.mean() + 2*X.std(),color='g') # linha horizontal com o limite superior
        plt.axhline(X.mean() - 2*X.std(),color='g') # linha horizontal com o limite inferior
        plt.show()
    elif salvar_figura==1:
        plt.figure(figsize=(a,b)) 
        plt.plot(X)
        plt.ylabel(y, fontsize=11)
        plt.xlabel('Time', fontsize=11)
        plt.axhline(X.mean(),color='r') # linha horizontal com a média
        plt.axhline(X.mean() + 2*X.std(),color='g') # linha horizontal com o limite superior
        plt.axhline(X.mean() - 2*X.std(),color='g') # linha horizontal com o limite inferior
        plt.savefig('{y}.pdf'.format(y=y),bbox_inches='tight')
        plt.show()
        
def csd_non_parametric(X,y,salvar_figura=0,a=10,b=5):
    # X são os valores propriamente do gráfico, ex: df[i]
    # y é o rótulo, ex: 'i'
    if salvar_figura==0:
        plt.figure(figsize=(a,b)) 
        plt.plot(X)
        plt.ylabel(y, fontsize=11)
        plt.xlabel('Time', fontsize=11)
        plt.axhline(X.mean(),color='r') # linha horizontal com a média
        plt.axhline(X.quantile(0.95),color='g') # linha horizontal com o limite superior
        plt.axhline(X.quantile(0.05),color='g') # linha horizontal com o limite inferior
        plt.show()
    elif salvar_figura==1:
        plt.figure(figsize=(a,b)) 
        plt.plot(X)
        plt.ylabel(y, fontsize=11)
        plt.xlabel('Time', fontsize=11)
        plt.axhline(X.mean(),color='r') # linha horizontal com a média
        plt.axhline(X.quantile(0.95),color='g') # linha horizontal com o limite superior
        plt.axhline(X.quantile(0.05),color='g') # linha horizontal com o limite inferior
        plt.savefig('{y}.pdf'.format(y=y),bbox_inches='tight')
        plt.show() 
        
def grafico_pvalor(X,y,salvar_figura=0,a=10,b=5):
    if salvar_figura==0:
        plt.figure(figsize=(a,b)) 
        plt.plot(X, '--bo')
        plt.ylabel(y, fontsize=11)
        plt.xlabel('Lags', fontsize=11)
        plt.axhline(0.05,color='g',linestyle='dashed')
        plt.yticks([0.05,0.15,0.30,0.45,0.60,0.75,0.90])  
        plt.ylim(0.005)
        plt.show()
    elif salvar_figura==1:
        plt.figure(figsize=(a,b)) 
        plt.plot(X, '--bo')
        plt.ylabel(y, fontsize=11)
        plt.xlabel('Lags', fontsize=11)
        plt.axhline(0.05,color='g',linestyle='dashed')
        plt.yticks([0.05,0.15,0.30,0.45,0.60,0.75,0.90]) 
        plt.ylim(0.005)
        plt.savefig('{y}.pdf'.format(y=y),bbox_inches='tight')
        plt.show()    
