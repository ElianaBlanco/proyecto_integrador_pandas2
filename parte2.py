import pandas as pd
from datasets import load_dataset

# Descarga y carga el dataset
dataset = load_dataset("mstz/heart_failure")

# Accede a la partición 'train' del dataset
data = dataset["train"]

# Convertir el Dataset en un DataFrame de Pandas
df = pd.DataFrame(data)

# Separar el dataframe en dos basado en la columna 'is_dead'
perecieron = df[df['is_dead'] == 1]
no_perecieron = df[df['is_dead'] == 0]

# Calcular el promedio de edades para cada grupo
promedio_edad_perecieron = perecieron['age'].mean()
promedio_edad_no_perecieron = no_perecieron['age'].mean()

# Imprimir los resultados
print("Promedio de edades de personas que perecieron:", promedio_edad_perecieron)
print("Promedio de edades de personas que no perecieron:", promedio_edad_no_perecieron)
