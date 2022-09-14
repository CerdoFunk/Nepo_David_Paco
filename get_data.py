#! /usr/bin/env python3

import pandas as pd
import datetime
#pandas_datareader tiene acceso a distintas fuentes de internet para descargar series de tiempo. 
from pandas_datareader import data as pdr 

#Fechas en formato (AAAA, M, D) usando paqueteria datetime.
initial_t = datetime.datetime(2022, 9, 1)
final_t = datetime.datetime(2022, 9, 9)
#Habra que buscar una forma de obtener nombres sin que se tenga que escribir una lista.
raw_data = ['BTC-USD', 'GE']


def data_to_csv(start, end, symbol):
    """Función para probar la descarga de datos de yahoo finance
    (pero se pueden usar otras fuentes de internen. Listadas en:
    https://pandas-datareader.readthedocs.io/en/latest/remote_data.html)
    Dicha función necesita una fecha inicial y final (start y end)
    y una lista (symbol) con los nombres que se quieren descargar 
    en dicho intervalo de tiempo."""


    #Para hacer leible la fecha y usarla en el nombre del archivo.csv de salida.
    time_i = start.strftime('%Y-%m-%d')
    time_f = end.strftime('%Y-%m-%d')
    df = pdr.DataReader(symbol, 'yahoo', start = start, end = end)

    return df.to_csv("from" + time_i + "to" + time_f + "of" + str(raw_data) + ".csv")

data_to_csv(initial_t, final_t, raw_data)

