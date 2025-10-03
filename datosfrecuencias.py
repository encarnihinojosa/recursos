import pandas as pd
import numpy as np

# Cargar el dataset desde archivo
df = pd.read_csv("/Users/ehinojosa/Desktop/espectro_piquituerto.txt", sep="\t")

# Número de bloques deseados
n_bloques = 40
n_filas = len(df)

# Calcular tamaño de bloque (aprox.)
tam_bloque = n_filas / n_bloques

# Asignar cada fila a un grupo proporcionalmente
df["grupo"] = (np.floor(np.arange(n_filas) / tam_bloque)).astype(int)
df["grupo"] = df["grupo"].clip(upper=n_bloques-1)

# Calcular promedios por grupo
df_promedio = df.groupby("grupo", as_index=False).mean()

# Eliminar la columna auxiliar
df_promedio = df_promedio.drop(columns=["grupo"])

# Guardar el resultado a CSV
df_promedio.to_csv("dataset_promediado.csv", index=False)

print(df_promedio)