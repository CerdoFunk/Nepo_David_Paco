#! /usr/bin/env python3

import pandas as pd
import datetime

# pandas_datareader tiene acceso a distintas fuentes de internet para descargar series de tiempo.
from pandas_datareader import data as pdr
from yahooquery import Screener

# Fechas en formato (AAAA, M, D) usando paqueteria datetime.
initial_t = datetime.datetime(2022, 9, 8)
final_t = datetime.datetime(2022, 9, 9)


def get_symbols():
    """Función para obtener todos los nombres de las criptos
    en yahoo finance usando la class Screener de yahooquery."""
    s = Screener()
    data = s.get_screeners("all_cryptocurrencies_us", count=250)
    dicts = data["all_cryptocurrencies_us"]["quotes"]
    symbols = [name["symbol"] for name in dicts]
    print(symbols)
    return symbols


def data_to_csv(start, end, symbol, valor):
    """Función para probar la descarga de datos de yahoo finance
    (pero se pueden usar otras fuentes de internet. Listadas en:
    https://pandas-datareader.readthedocs.io/en/latest/remote_data.html)
    Dicha función necesita una fecha inicial y final (start y end)
    y una lista (symbol) con los nombres que se quieren descargar
    en dicho intervalo de tiempo. Al final la función puede devolver
    los precios de Adj Close, Volume, Close u Open, dependiendo de cómo
    se defina el argumento valor en esta función (debe ser type(str)). 
    Todo estopara cada cripto seleccionada por get_symbols() 
    o por una lista con nombres. 
    Al final todo se escribe en un archivo.csv"""

    # Para hacer leible la fecha y usarla en el nombre del archivo.csv de salida.
    time_i = start.strftime("%Y-%m-%d")
    time_f = end.strftime("%Y-%m-%d")
    df = pdr.DataReader(symbol, "yahoo", start=start, end=end)
    print(df.head())
    print("-----------------------------")
    print(df[valor])

    # La función devuelve todas los precios de Adj Close para cada cripto en un archivo.csv.
    # Adj Close es sólo uno de los atributos de la data descargada. Modificando el return por
    # Volume, Close, Open generara un archivo.csv pero considerando esos atributos.
    return df[valor].to_csv(
        "from" + time_i + "to" + time_f + "of" + valor + "allYahooCryptoSymbols"+".csv"
    )

print(get_symbols())
data_to_csv(initial_t, final_t, get_symbols(), "Volume")
