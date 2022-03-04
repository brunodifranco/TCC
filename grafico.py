# Módulo grafico
#Gráficos

def fazer_graficos(X,y,salvar_figura=0):
    import matplotlib.pyplot as plt
    # X são os valores propriamente do gráfico, ex: df[i]
    # y é o rótulo, ex: i
    if salvar_figura==0:
        plt.figure(figsize=(10,5)) 
        plt.plot(X)
        plt.ylabel(y, fontsize=11)
        plt.xlabel('Tempo', fontsize=11)
        plt.show()
    elif salvar_figura==1:
        plt.figure(figsize=(10,5)) 
        plt.plot(X)
        plt.ylabel(y, fontsize=11)
        plt.xlabel('Tempo', fontsize=11)
        plt.savefig('{y}.png'.format(y=y))
        plt.show()  
        
#Histograma        
def histograma(X,y,salvar_figura=0):
    import matplotlib.pyplot as plt
    # X são os valores propriamente do gráfico, ex: df[i]
    # y é o rótulo, ex: histograma de i
    if salvar_figura==0:
        plt.figure(figsize=(10,5)) 
        plt.hist(X)
        plt.ylabel(y, fontsize=11)
        plt.show()
    elif salvar_figura==1:
        plt.figure(figsize=(10,5)) 
        plt.hist(X)
        plt.ylabel(y, fontsize=11)
        plt.savefig('{y}.png'.format(y=y))
        plt.show()
