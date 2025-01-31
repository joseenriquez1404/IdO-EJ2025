import itertools
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Se generan el número de caras que tienen los dados
caras = range(1, 21)

# Se generan todas las combinaciones de las caras de los dados
espacio_muestral = list(itertools.product(caras, repeat=3))

# Extraer las coordenadas para x, y, z
x, y, z = zip(*espacio_muestral)

# Crear la primera figura y gráfico en 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Graficar los puntos en 3D
ax.scatter(x, y, z, c='b', marker='o', alpha=0.5, s=5)

# Títulos y etiquetas de los ejes
ax.set_title('Espacio Muestral de 3 Dados de 20 Caras')
ax.set_xlabel('Dado 1')
ax.set_ylabel('Dado 2')
ax.set_zlabel('Dado 3')

# Configuración de los ticks de los ejes
ax.set_xticks(np.arange(1, 21, 1))
ax.set_yticks(np.arange(1, 21, 1))
ax.set_zticks(np.arange(1, 21, 1))

# Mostrar la primera gráfica (3D)
plt.show()

# Calcular la variable aleatoria X (la suma de los valores de los 3 dados)
X = [sum(tirada) for tirada in espacio_muestral]

# Obtener los valores únicos de X (suma de los dados) y sus frecuencias
valores_unicos, frecuencias = np.unique(X, return_counts=True)

# Calcular la probabilidad de cada valor de X
probabilidades = frecuencias / len(espacio_muestral)

# Crear una nueva figura para la segunda gráfica
plt.figure(figsize=(12, 6))

# Graficar la distribución de probabilidades de la suma de los 3 dados
plt.bar(valores_unicos, probabilidades, color='skyblue', edgecolor='black')

# Etiquetas y título de la gráfica
plt.xlabel("Valor de X (Suma de los 3 dados)")
plt.ylabel("Probabilidad")
plt.title("Distribución de Probabilidad de la Suma de 3 Dados de 20 Caras")

# Ajustar los ticks del eje X
plt.xticks(range(3, 61, 2))  # Mostrar solo valores pares en el eje X

# Mostrar una cuadrícula en el eje Y
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Mostrar la segunda gráfica (histograma de probabilidades)
plt.show()
