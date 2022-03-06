# Módulo testes_gerais
#Shapiro        
def shapiro_teste(X):
    from scipy.stats import shapiro
    estatistica, p = shapiro(X)
    print('Statistics=%.8f, p=%.8f' % (estatistica, p))
    alpha = 0.05
    if p > alpha:
        print('Fail to reject H0 - Data are normally distributed')
    else:
        print('Reject H0 - Data are not normally distributed')

#Ljung-Box        
def LjungBox(X):
    from statsmodels.stats.diagnostic import acorr_ljungbox
    import pandas as pd
    a = acorr_ljungbox(X, return_df=False)[0]
    b = acorr_ljungbox(X, return_df=False)[1]
    return pd.DataFrame({'lb_stat': a, 'lb_pvalue': b})              
