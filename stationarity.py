# Stationarity module
import warnings
from statsmodels.tsa.stattools import adfuller, kpss

#Dickey-Fuller
def dickey_fuller(X,y):
    '''
    This function returns the ADF test;
    X is the data used for the test;
    y is the label.

    ''' 
    teste_adf = adfuller(X)
    print('{y}'.format(y=y))
    print('Estatística ADF: %f' % teste_adf[0])
    print('p-valor: %f' % teste_adf[1])
    print('Valores Críticos:')
    for key, valor in teste_adf[4].items():
        print('\t%s: %.3f' % (key, valor))
    print(f'Resultado: A série{"não" if teste_adf[1] > 0.05 else ""} é estacionária')
    print('\n')
    
#KPSS   
def kpss_test(X,y):
    '''
    This function returns the KPSS test;
    X is the data used for the test;
    y is the label.

    ''' 
    warnings.filterwarnings('ignore')
    teste_kpss = kpss(X)
    print('{y}'.format(y=y))
    print('Estatística KPSS: %f' % teste_kpss[0])
    print('p-valor: %f' % teste_kpss[1])
    print('Nº de lags: %f' % teste_kpss[2])
    print('Valores Críticos:')
    for key, valor in teste_kpss[3].items():
        print('\t%s: %.3f' % (key, valor))
    print(f'Resultado: A série{"não" if teste_kpss[1] < 0.05 else ""} é estacionária')
    print('\n')  