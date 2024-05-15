import random
import math

def generar_muestra(tamano_muestras, num_muestras):
    muestras = []
    while len(muestras) < num_muestras:
        # Generar números aleatorios U y V
        U = random.uniform(0, 1)
        V = random.uniform(0, 1)  # V en el intervalo [0,1]

        # Evaluar si se acepta la muestra
        if V <= U**tamano_muestras:
            muestras.append(U)
    return muestras

# Tamaño de las muestras
tamano_muestras = 1000 # Por ejemplo, tamaño 3

# Generar 1000 muestras usando el método de aceptación y rechazo
muestras = generar_muestra(tamano_muestras, 1000)

print("Muestras generadas:", len(muestras))
print("Muestras ejemplo:", muestras[:10])
import matplotlib.pyplot as plt
import numpy as np
import time

def fmasa(x, n):
    return n * x ** (n - 1)

def fdistribucion(x, n):
    return x ** n

def transformada_inversa(n):
    u = random.random()
    return u ** (1 / n)

def aceptacion_y_rechazo1(n):
    us = [random.random() for _ in range(n)]
    return max(us)

def aceptacion_y_rechazo2(n):
    us = [1 - random.random() for _ in range(n)]
    return 1 - min(us)

def obtener_probabilidades(funcion, num_simulaciones, *args):
    random.seed(1000)
    acumulados = []

    start = time.perf_counter()
    for _ in range(num_simulaciones):
        resultado = funcion(*args)
        acumulados.append(resultado)

    end = time.perf_counter()

    tiempo_ejecucion = end - start
    return acumulados, tiempo_ejecucion

def graficar_probabilidades(variables, num_simulaciones):
    x = np.arange(0, 1, 0.1)
    for nombre, funcion, argumentos in variables:
        print(75 * '-')
        print(nombre)

        acumulados, tiempo_ejecucion = obtener_probabilidades(funcion, num_simulaciones, *argumentos)
        print(acumulados)
        print(f'Tiempo de ejecución: {tiempo_ejecucion:.5f} segundos')

        y = []
        for i in x:
            f_le = list(filter(lambda k: k <= i, acumulados))
            probabilidad = len(f_le) / num_simulaciones
            y.append(probabilidad)

        plt.plot(x, y, label=nombre)

    plt.xlabel('x')
    plt.ylabel('Probabilidad')
    plt.title('Probabilidad acumulada de X')
    plt.legend()
    plt.show()

# Variables de métodos y sus argumentos
variables = [
    ("Transformada Inversa", transformada_inversa, (3,)),
    ("Aceptación y Rechazo 1", aceptacion_y_rechazo1, (3,)),
    ("Aceptación y Rechazo 2", aceptacion_y_rechazo2, (3,))
]

# Graficar probabilidades acumuladas
graficar_probabilidades(variables, 10000)

