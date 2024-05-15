import numpy as np

from random import random

def poisson_process(T, lam):
    # Generar tiempos de arribo de los eventos
    t_arribo = []
    tiempo = 0
    while tiempo < T:
        # Generar el tiempo de arribo del próximo evento
        u = random()
        inter_arrival_time = -np.log(u) / lam
        tiempo += inter_arrival_time
        # Si el tiempo de arribo está dentro del intervalo [0, T], agregarlo a la lista
        if tiempo < T:
            t_arribo.append(tiempo)

    # Número de eventos
    num_eventos = len(t_arribo)

    return num_eventos, t_arribo

# Parámetros del proceso de Poisson
T = 10  # Unidades de tiempo
lam = 0.5  # Parámetro lambda

# Calcular el número de eventos y sus tiempos de arribo
num_eventos, t_arribo = poisson_process(T, lam)

# Imprimir resultados
print("Número de eventos en las primeras", T, "unidades de tiempo:", num_eventos)
print("Tiempo de arribo de los eventos:", t_arribo)

