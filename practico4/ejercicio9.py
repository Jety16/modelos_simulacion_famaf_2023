import numpy as np
from random import random

def geom_transformada_inversa(p, n):
    valores = []
    for _ in range(n):
        i = 1
        U = random()
        while U > (1 - p)**i:
            i += 1
        valores.append(i)
    return valores


def geom_ensayos(p, n):
    valores = []
    for _ in range(n):
        ensayos = 1
        while random() > p:
            ensayos += 1
        valores.append(ensayos)
    return valores

# Parámetros
p_values = [0.8, 0.2]
n_simulaciones = 10000

for p in p_values:
    print(f"Para p = {p}:")
    breakpoint()
    # Método a) Usando transformada inversa
    valores_a = geom_transformada_inversa(p, n_simulaciones)
    promedio_a = np.mean(valores_a)
    valor_esperado_a = 1 / p
    print("Método a): Promedio obtenido:", promedio_a, ", Valor esperado:", valor_esperado_a)

    # Método b) Simulando ensayos
    valores_b = geom_ensayos(p, n_simulaciones)
    promedio_b = np.mean(valores_b)
    valor_esperado_b = 1 / p
    print("Método b): Promedio obtenido:", promedio_b, ", Valor esperado:", valor_esperado_b, "\n")

