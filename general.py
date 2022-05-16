# general module

import pandas as pd
from scipy.stats import shapiro
from statsmodels.stats.diagnostic import acorr_ljungbox
import numpy as np

#Shapiro  
 
def shapiro_test(X):
    '''
    This function returns the Shapiro-Wilk test;
    X is the data used for the test.
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

# News volume with abnormal volatility 

def volume_news_volatility(df_volatility,df_news_volume):
    '''
    This function returns the news volume over time that matches the volatility for each day;
    df_volatility is the DataFrame with the volatility period;
    df_news_volume is the DataFrame with the total news volume;
    df_noticias é o DataFrame com o volume de notícias total;
    Retorna df_Noticias_Volatilidade.  
    
    '''
    lista = []
    for i in range(len(df_volatility)): 
        lista.append(str(df_volatility.index[i]).rstrip('00:00:00').strip()) # Get the dates

    lista2 = []
    for i in lista:
        lista2.append(df_news_volume.loc[df_news_volume.index=='{}'.format(i)])
    df_news_volatility = pd.concat(lista2) 
    return(df_news_volatility)


# News is abnormal volatility

def news_volatility(df_abnormal_vol,df_news):     
    '''
    This function returns the news on which abnormal volatility is present;
    df_abnormal_vol is the DataFrame with the abnormal volatility periods;
    df_news is the DataFrame with links and headlines.
    '''
    lista1 = []
    for i in range(len(df_abnormal_vol)): 
        lista1.append(str(df_abnormal_vol.index[i]).rstrip('00:00:00').strip())    
    df_news1 = []   
    for i in lista1:
        df_news1.append(df_news.filter(like='{}'.format(i), axis=0))
    df_news1 = pd.concat(df_news1)
    return(df_news1)

# Returns
 
def returns(X):
    '''
    This function returns the logaritmic returns for a given DataFrame.    
    ''' 
    a = np.log(X).diff().dropna()
    return a
  

# Parametric limit
def limit_parametric(X,coluna):
    '''
    This function returns the volatility parametric limit;
    X is the DataFrame with the volatility;
    coluna é is the DataFrame's column name where the volatility is.
    
    '''
    upper_limit_parametric = X.mean() +2*X.std()
    lower_limit_parametric = X.mean() -2*X.std()
    
    print('Upper Limit Parametric = {}'.format(float(upper_limit_parametric.values)))
    print('Lower Limit Parametric = {}'.format(float(lower_limit_parametric.values)))
    
    df_abnormal_vol_parametric = X.loc[((X[coluna] > float(upper_limit_parametric))|(X[coluna] < float(lower_limit_parametric)))]
    print(df_abnormal_vol_parametric.count())
    return(df_abnormal_vol_parametric)

# Non parametric limit
def limit_non_parametric(X,coluna,Y,Z):
    '''
    This function returns the volatility nonparametric limit;
    X is the DataFrame with the volatility;
    Y is the upper limit percentile;
    Z is the lower limit percentile;
    coluna é is the DataFrame's column name where the volatility is.
    '''
    upper_limit_non_parametric = X.quantile(Y)
    lower_limit_non_parametric = X.quantile(Z)
    
    print('Upper Limit Non Parametric = {}'.format(float(upper_limit_non_parametric.values)),'|','Lower Limit Non Parametric  = {}'.format(float(lower_limit_non_parametric.values)))
    df_abnormal_vol_non_parametric = X.loc[((X[coluna] > float(upper_limit_non_parametric))) | ((X[coluna] < float(lower_limit_non_parametric)))]
    print(df_abnormal_vol_non_parametric.count())
    return(df_abnormal_vol_non_parametric)
