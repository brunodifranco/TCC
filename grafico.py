# Módulo grafico

import matplotlib.pyplot as plt

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
        plt.hist(X)
        plt.ylabel(y, fontsize=11)
        plt.show()
    elif salvar_figura==1:
        plt.figure(figsize=(10,5)) 
        plt.hist(X)
        plt.ylabel(y, fontsize=11)
        plt.savefig('{y}.png'.format(y=y))
        plt.show()
        
def grafico_csd(X,y,salvar_figura=0,a=10,b=5):
    # X são os valores propriamente do gráfico, ex: df[i]
    # y é o rótulo, ex: 'i'
    if salvar_figura==0:
        plt.figure(figsize=(a,b)) 
        plt.plot(X)
        plt.ylabel(y, fontsize=11)
        plt.xlabel('Tempo', fontsize=11)
        plt.axhline(X.mean(),color='r') # linha horizontal com a média
        plt.axhline(X.mean() + 2*X.std(),color='g') 
        plt.axhline(X.mean() - 2*X.std(),color='g')  
        plt.ylim([-0.015, 0.12])
        plt.show()
    elif salvar_figura==1:
        plt.figure(figsize=(a,b)) 
        plt.plot(X)
        plt.ylabel(y, fontsize=11)
        plt.xlabel('Tempo', fontsize=11)
        plt.axhline(X.mean(),color='r') # linha horizontal com a média
        plt.axhline(X.mean() + 2*X.std(),color='g') 
        plt.axhline(X.mean() - 2*X.std(),color='g')  
        plt.ylim([-0.015, 0.12])
        plt.savefig('{y}.png'.format(y=y))
        plt.show()        