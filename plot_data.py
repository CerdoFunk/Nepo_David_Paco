#! /usr/bin/env python3
import pandas as pd
from datetime import datetime as dt
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
import typer

cripto = typer.Typer()


def line_plot(t_i, t_f, crypto):
    """line_plot es una función que grafica el valor Adj Close de una
    cripto respecto al tiempo."""

    # Para hacer leible la fecha y usarlo para personalizar la gráfica.
    time_i = t_i.strftime("%Y-%m-%d")
    time_f = t_f.strftime("%Y-%m-%d")
    fig, ax = plt.subplots()
    df = pdr.DataReader(crypto, "yahoo", start=t_i, end=t_f)
    new_df = df.reset_index()
    df1 = df["Adj Close"]
    df1.plot()
    fig.savefig("line_plot_from_"+time_i+"_to_"+time_f+"_of_"+crypto+".eps", format = "eps")
    plt.show()


def scatter_plot(t_i, t_f, cryptoA, cryptoB):
    """scatter plot es una función para hacer el gráfico de dispersión
    de dos criptomonedas."""
    time_i = t_i.strftime("%Y-%m-%d")
    time_f = t_f.strftime("%Y-%m-%d")
    fig, ax = plt.subplots()
    df_A = pdr.DataReader(cryptoA, "yahoo", start=t_i, end=t_f)
    df_B = pdr.DataReader(cryptoB, "yahoo", start=t_i, end=t_f)
    new_df_A = df_A.reset_index()
    new_df_B = df_B.reset_index()
    x1 = new_df_A["Adj Close"].values
    y1 = new_df_B["Adj Close"]
    plt.scatter(x1, y1)
    fig.savefig("scatter_plot_from_"+time_i+"_to_"+time_f+"_of_"+cryptoA+"_and_"+cryptoB+".eps", format = "eps")
    plt.show()


@cripto.command()
def time_serie(cripto="BTC-USD"):
    t_i = dt(2022, 9, 1)
    t_f = dt(2022, 10, 9)
    line_plot(t_i, t_f, cripto)


@cripto.command()
def scatter(cripto_1="BTC-USD", cripto_2="ETH-USD"):
    t_i = dt(2022, 9, 1)
    t_f = dt(2022, 10, 9)
    scatter_plot(t_i, t_f, cripto_1, cripto_2)


if __name__ == "__main__":
    cripto()

