#!/usr/bin/env python3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import matplotlib as mpl
import collections

#reads the csv
data = pd.read_csv('from2018-01-01to2022-09-09ofallYahooCryptoSymbols.csv')
data = data.fillna(0)
#craetes a correlation matrix
cor_matrix = data.iloc[:,1:].corr()
print(data.iloc[:, 1:])


def pos_or_neg(corr_mat, valor, cota):
    """Función para separar la matriz de correlación en parte
    positiva, negativa o dejarla como esta"""

    if valor == "positivo":
        positive_mat = corr_mat[corr_mat > cota]
        new_mat = positive_mat.fillna(0)
    elif valor == "negativo":
        negative_mat = corr_mat[corr_mat < cota]
        new_mat = negative_mat.fillna(0)
    return new_mat


def crear_red(matrix):
    """Función para generar una red apartir de la matriz de
    correlación"""
    #Extraer los índices de la matriz de correlación (nombres de los lípidos)
    nodos = matrix.index.values
    #Cambiar de dataframe a matriz, para facilitarle a Networkx la tarea
    cor_matrix = np.asmatrix(matrix)
    #Generamos el grafo usando los lípidos como nodos y su coeficiente de correlación como sus vertices (edges)
    G = nx.from_numpy_matrix(cor_matrix)
    #Le ponemos nombre a los nodos, usando los valores de nodos en la primera línea
    G = nx.relabel_nodes(G,lambda x: nodos[x])
    G.edges(data=True)
#    print(G.edges)
    return G
#print(crear_red(pos_or_neg(cor_matrix, "positivo", 0)))

def create_corr_network_1(G, corr_direction):
    """Función para generar un grafo a partir de la matriz de
    correlación."""

    # Crear una lista de edges y weights
    edges,weights = zip(*nx.get_edge_attributes(G,'weight').items())
    positions = nx.spring_layout(G)
    #Tamaño de la figura
    plt.figure(figsize=(15,15))
    #Calcular el grado o valencia de cada nodo
    d = nx.degree(G)
    #Crear una lista de nodos y una de su grado o valencia. Para ser usado después en el tamaño del nodo en el grafo. 
    nodelist, node_sizes = zip(*dict(d).items())
    #Dibujar nodos con tamaño determinado por el grado o valencia que llamamos node_sizes.
    nx.draw_networkx_nodes(G, positions, node_color='#DA70D6', nodelist = nodelist, node_size=tuple([x**1.4 for x in node_sizes]), alpha=0.8)
    #Estilo de las labels
    nx.draw_networkx_labels(G, positions, font_size=6, font_family='sans-serif')

    ###Se puede incrementar el valor de weights para hacerlos más visibles en el grafo.
    weights = tuple([x for x in weights])

    ###Color de los bordes (edges) dependiendo si son valores positivos, negativos o todos de la matriz de correlación
    if corr_direction == "positivo":
        edge_colour = plt.cm.winter
    elif corr_direction == "negativo":
        edge_colour = plt.cm.summer 

    nx.draw_networkx_edges(G, positions, edgelist=edges,style='solid', width=weights, edge_color = weights, edge_cmap = edge_colour, edge_vmin = min(weights), edge_vmax=max(weights))
    sm = plt.cm.ScalarMappable(cmap = edge_colour, norm=plt.Normalize(vmin = min(weights), vmax = max(weights)))
    sm._A = []
    plt.colorbar(sm)
    plt.axis('off')
    #Salvar imagenes en formato eps
    #plt.savefig("PSMPOPCup100_cho35_positivo.eps", format = "eps")
    return plt.show()

#create_corr_network_1(crear_red(pos_or_neg(cor_matrix, "positivo", 0)), "positivo")
create_corr_network_1(crear_red(pos_or_neg(cor_matrix, "negativo", -0.4)), "negativo")
