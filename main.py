#Módulo principal

import grafico
import estacionariedade
import retornos
import testes_gerais

def main():
    global df
    df = retornos.calcular_retornos(df)
    grafico.fazer_graficos(df,"IBOVESPA")
    grafico.histograma(df.values,"IBOVESPA")
    df_estacionariedade = df.iloc[:,0].values
    estacionariedade.dickey_fuller(df_estacionariedade,'IBOVESPA FUTURES RETURNS')
    estacionariedade.kpss_teste(df_estacionariedade,'IBOVESPA FUTURES RETURNS')
    testes_gerais.shapiro_teste(df)
    print(testes_gerais.LjungBox(df))  

if __name__ == "__main__":
    main()