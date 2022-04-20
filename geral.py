# Módulo geral

import pandas as pd
from scipy.stats import shapiro
from statsmodels.stats.diagnostic import acorr_ljungbox
import numpy as np

#Shapiro  
 
def shapiro_teste(X):
    '''
    Essa função retorna o teste de Shapiro-Wilk de normalidade;
    X são os dados em que o teste será realizado.

    '''  
    estatistica, p = shapiro(X)
    print('Statistics=%.8f, p=%.8f' % (estatistica, p))
    alpha = 0.05
    if p > alpha:
        print('Fail to reject H0 - Data are normally distributed')
    else:
        print('Reject H0 - Data are not normally distributed')
    

#Ljung-Box        
def LjungBox(X):
    return pd.DataFrame({'lb_stat': acorr_ljungbox(X)[0], 'lb_pvalue': acorr_ljungbox(X)[1]})              

# Volume de Notícias com Volatilidade anormal

def volume_noticias_volatilidade(df_volatilidade,df_volume_noticias):
    '''
    Essa função retorna o volume de notícias correspondente com a volatilidade do dia;
    df_volatilidade é o DataFrame com a volatilidade do período em questão;
    df_noticias é o DataFrame com o volume de notícias total;
    Retorna df_Noticias_Volatilidade.  
    
    '''
    lista = []
    for i in range(len(df_volatilidade)): 
        lista.append(str(df_volatilidade.index[i]).rstrip('00:00:00').strip()) # Pegar as datas

    lista2 = []
    for i in lista:
        lista2.append(df_volume_noticias.loc[df_volume_noticias.index=='{}'.format(i)])
    df_Noticias_Volatilidade = pd.concat(lista2) 
    return(df_Noticias_Volatilidade) # 


# Notícias com volatilidade anormal

def noticias_volatilidade(df_abnormal_vol,df_noticias):     
    '''
    Essa função retorna as notícias nas datas em que há volatilidade anormal;
    df_abnormal_vol é o DataFrame com os períodos de volatilidade anormal;
    df_volume_noticias é o DataFrame com as manchetes e links de todas as notícias;
    Retorna df_news.
    
    '''
    lista1 = []
    for i in range(len(df_abnormal_vol)): 
        lista1.append(str(df_abnormal_vol.index[i]).rstrip('00:00:00').strip())    
    df_news = []   
    for i in lista1:
        df_news.append(df_noticias.filter(like='{}'.format(i), axis=0))
    df_news = pd.concat(df_news)
    return(df_news)

# Retornos
 
def calcular_retornos(X):
    '''
    Essa função calcula os retornos de um DataFrame;
    Ex de uso: df = calcular_retornos(df).
    
    ''' 
    a = np.log(X).diff().dropna()
    return a
  

# Limite paramétrico
def limite_parametrico(X,coluna):
    '''
    Essa função retorna o limite paramétrico da volatilidade;
    X é o DataFrame com as volatililidades;
    coluna é o nome da coluna do DataFrame onde estão as volatilidades.
    
    '''
    upper_limit_parametric = X.mean() +2*X.std()
    lower_limit_parametric = X.mean() -2*X.std()
    
    print('Upper Limit Parametric = {}'.format(float(upper_limit_parametric.values)))
    print('Lower Limit Parametric = {}'.format(float(lower_limit_parametric.values)))
    
    df_abnormal_vol_parametric = X.loc[((X[coluna] > float(upper_limit_parametric))|(X[coluna] < float(lower_limit_parametric)))]
    print(df_abnormal_vol_parametric.count())
    return(df_abnormal_vol_parametric)

# Limite não paramétrico
def limite_nao_parametrico(X,coluna,Y,Z):
    '''
    Essa função retorna o limite não paramétrico da volatilidade;
    X é o DataFrame com as volatililidades;
    Y é o percentil do limite superior (ex:0.95);
    Z é o percentil do limite inferior (ex:0.05);
    coluna é o nome da coluna do DataFrame onde estão as volatilidades.
    '''
    upper_limit_non_parametric = X.quantile(Y)
    lower_limit_non_parametric = X.quantile(Z)
    
    print('Upper Limit Non Parametric = {}'.format(float(upper_limit_non_parametric.values)),'|','Lower Limit Non Parametric  = {}'.format(float(lower_limit_non_parametric.values)))
    df_abnormal_vol_non_parametric = X.loc[((X[coluna] > float(upper_limit_non_parametric))) | ((X[coluna] < float(lower_limit_non_parametric)))]
    print(df_abnormal_vol_non_parametric.count())
    return(df_abnormal_vol_non_parametric)
