import numpy as np
from random import randint, random

def simular_llegada_aficionados():
    # Generar el número de autobuses que llegan en una hora (proceso de Poisson)
    num_autobuses = poisson_process(1, 5)[0]

    # Generar capacidades aleatorias para los autobuses
    capacidades_autobuses = [randint(20, 40) for _ in range(num_autobuses)]

    # Calcular el número total de aficionados
    num_aficionados = sum(capacidades_autobuses)
    print(capacidades_autobuses, "con un total de ", num_autobuses, "autobusses")
    return num_aficionados

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
# Simular la llegada de aficionados al encuentro en el instante t = 1 hora
num_aficionados_t1 = simular_llegada_aficionados()

print("Número total de aficionados que llegan al encuentro en el instante t = 1hora es", num_aficionados_t1)
