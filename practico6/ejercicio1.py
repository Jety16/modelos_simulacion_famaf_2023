import numpy as np
from math import log, sqrt, exp
from random import random

def Normal_rechazo(mu, sigma):
    while True:
        Y1 = -log(random())
        Y2 = -log(random())
        if Y2 >= (Y1 - 1) ** 2 / 2:
            if random() < 0.5:
                return Y1 * sigma + mu
            return -Y1 * sigma + mu

NV_MAGICCONST = 4 * exp(-0.5) / sqrt(2.0)
def normalvariate(mu, sigma):
    while 1:
        u1 = random()
        u2 = 1.0 - random()
        z = NV_MAGICCONST * (u1 - 0.5) / u2
        zz = z * z / 4.0
        if zz <= -log(u2):
            break
    return mu + z * sigma

def generar_datos(n_min=100, sigma_max=0.1):
    datos = []
    n = 0
    while True:
        dato = normalvariate(0, 1)
        print(dato)
        datos.append(dato)
        n += 1
        if n >= n_min:
            S = np.std(datos, ddof=1)
            if S / sqrt(n) < sigma_max:
                break
    return np.array(datos)

# Generar los datos
datos = generar_datos()

# Calcular los resultados requeridos
n_generados = len(datos)
media_muestral = np.mean(datos)
varianza_muestral = np.var(datos, ddof=1)

print(f"Número de datos generados: {n_generados}")
print(f"Media muestral: {media_muestral}")
print(f"Varianza muestral: {varianza_muestral}")

