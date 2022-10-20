#! /usr/bin/env python3
import pandas as pd
from datetime import datetime as dt
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr


def line_plot(t_i, t_f, crypto):
    """line_plot es una función que grafica el valor Adj Close de una
    cripto respecto al tiempo."""

    # Para hacer leible la fecha y usarlo para personalizar la gráfica.
    time_i = t_i.strftime("%Y-%m-%d")
    time_f = t_f.strftime("%Y-%m-%d")

    df = pdr.DataReader(crypto, "yahoo", start=t_i, end=t_f)
    new_df = df.reset_index()
    df1 = df["Adj Close"]
    df1.plot()
    plt.show()
    # return plt.show()


def scatter_plot(t_i, t_f, cryptoA, cryptoB):
    """scatter plot es una función para hacer el gráfico de dispersión
    de dos criptomonedas."""
    time_i = t_i.strftime("%Y-%m-%d")
    time_f = t_f.strftime("%Y-%m-%d")

    df_A = pdr.DataReader(cryptoA, "yahoo", start=t_i, end=t_f)
    df_B = pdr.DataReader(cryptoB, "yahoo", start=t_i, end=t_f)
    new_df_A = df_A.reset_index()
    new_df_B = df_B.reset_index()
    x1 = new_df_A["Adj Close"].values
    y1 = new_df_B["Adj Close"]
    plt.scatter(x1, y1)
    plt.show()
    # return plt.show()


t_i = dt(2022, 9, 1)
t_f = dt(2022, 10, 9)
line_plot(t_i, t_f, "BTC-USD")
scatter_plot(t_i, t_f, "BTC-USD", "ETH-USD")
