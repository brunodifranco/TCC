# Módulo retornos
def calcular_retornos(X):
    # Ex de uso: df = calcular_retornos(df)
    import pandas as pd
    import numpy as np
    a = np.log(X).diff().dropna()
    return a