#! /usr/bin/env python3
# Programa para calcular la matriz de correlación de Pearson, utilizando sólo los
# valores significativos, es decir, para cada coef. de Pearson (c_P) calculamos el p_value
# tal que si el p_value > 0.05 para algún valor c_P, no lo consideramos significativo y lo hacemos cero.
# Para generar la matriz necesitas generar un archivo.csv con get_data.py

import pandas as pd
import scipy.stats as ss
from scipy import stats
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr as pr
from sklearn.preprocessing import power_transform

data1 = pd.read_csv('from2018-01-01to2022-09-09ofallYahooVolumeCryptoSymbols.csv') # Leemos el archivo generado por get_data.py
dataframe1 = data1.iloc[:,1:] # Consideramos sólo las columnas de cripto valores y excluimos la columna de tiempo
dataframe1 = dataframe1.fillna(0.0) # Convertimos Nan's a ceros para que no falle el análisis de correlaciones
print(dataframe1)

### Copiar dataframe1 para generar una matriz normalizada por medio de box-cox o yeo-johnson, 
# dependiendo de si existen valores negativos en la data. Al final se genera un dataframe; norm_df
data_tf = dataframe1.copy()
columns = data_tf.columns
norm_data = power_transform(data_tf, method = "yeo-johnson")
norm_df = pd.DataFrame(norm_data, columns = columns )


def significant_value_mat(norm_df):
    """Función alimentada de un dataframe normalizado para que sea valido el tratamiento.
    Si los datos son normales, podemos calcular significancia usando el test de p_value.
    Esto lo hacemos calculando cada coeff. de corr. Pearson con su p_value, tal que si no pasa la prueba,
    el valor se vuelve cero (no es significativo, lo borramos)"""  
  
    df_corr = pd.DataFrame() # Matriz de correlación vacía
    df_p = pd.DataFrame()  # Matriz de p-values vacía
    for x in norm_df.columns:
        for y in norm_df.columns:
            corr = stats.pearsonr(norm_df[x], norm_df[y])
            df_corr.loc[x,y] = corr[0] #coef de correlación en cada celda del df
            df_p.loc[x,y] = corr[1] # p-value en cada celda
            mask = (df_p <= 0.05) # Generando una matriz mascara con valores True o False dependiendo si se cumple la condición
            significant_values = np.zeros_like(df_corr)
            significant_values = df_corr[mask] # Genero una matriz con los valores de pears_corr_mat y NaN las celdas que no cumple con mask
            significant_values.fillna(0.0) # Cambiar NaN por 0's
            print(significant_values)
    return significant_values

# Las tres lineas sig. son para llamar a la función y plotear los valores significativos en un heatmap
sign_value_mat = significant_value_mat(norm_df)
sns.heatmap(sign_value_mat, vmin = -1, vmax = 1, cmap = "PRGn")
plt.show()
