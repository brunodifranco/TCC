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
        plt.xlabel('Tempo', fontsize=11)
        plt.show()
    elif salvar_figura==1:
        plt.figure(figsize=(a,b)) 
        plt.plot(X)
        plt.ylabel(y, fontsize=11)
        plt.xlabel('Tempo', fontsize=11)
        plt.savefig('{y}.png'.format(y=y))
        plt.show() 
          
def histograma(X,y,salvar_figura=0,a=10,b=5):
    # X são os valores propriamente do gráfico, ex: df[i]
    # y é o rótulo, ex: histograma de i
    if salvar_figura==0:
        plt.figure(figsize=(a,b)) 
        mu, std = norm.fit(X)
        plt.hist(X,density=True)
        xmin, xmax = plt.xlim()
        x = np.linspace(xmin, xmax, 100)
        p = norm.pdf(x, mu, std)
        plt.plot(x, p, 'k', linewidth=2)
        plt.ylabel(y, fontsize=11)
        plt.show()
    elif salvar_figura==1:
        plt.figure(figsize=(a,b)) 
        mu, std = norm.fit(X)
        plt.hist(X,density=True)
        xmin, xmax = plt.xlim()
        x = np.linspace(xmin, xmax, 100)
        p = norm.pdf(x, mu, std)
        plt.plot(x, p, 'k', linewidth=2)
        plt.ylabel(y, fontsize=11)
        plt.savefig('{y}.png'.format(y=y))
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
        plt.ylim([X.min()*-1.1, X.max()*1.1])
        plt.show()
    elif salvar_figura==1:
        plt.figure(figsize=(a,b)) 
        plt.plot(X)
        plt.ylabel(y, fontsize=11)
        plt.xlabel('Time', fontsize=11)
        plt.axhline(X.mean(),color='r') # linha horizontal com a média
        plt.axhline(X.mean() + 2*X.std(),color='g') # linha horizontal com o limite superior
        plt.ylim([X.min()*-1.1, X.max()*1.1])
        plt.savefig('{y}.png'.format(y=y))
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
        plt.axhline(X.quantile(0.90),color='g') # linha horizontal com o limite superior
        plt.ylim([X.min()*-1.1, X.max()*1.1])
        plt.show()
    elif salvar_figura==1:
        plt.figure(figsize=(a,b)) 
        plt.plot(X)
        plt.ylabel(y, fontsize=11)
        plt.xlabel('Time', fontsize=11)
        plt.axhline(X.mean(),color='r') # linha horizontal com a média
        plt.axhline(X.quantile(0.90),color='g') # linha horizontal com o limite superior
        plt.ylim([X.min()*-0.5, X.max()*1.1])
        plt.savefig('{y}.png'.format(y=y))
        plt.show()               
