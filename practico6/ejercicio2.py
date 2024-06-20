import numpy as np
from random import random

def monte_carlo_integral_i(n_min=100, sigma_max=0.01):
    n = 0
    valores = []
    while True:
        x = random()
        fx = np.exp(x) / np.sqrt(2 * x)
        valores.append(fx)
        n += 1
        if n >= n_min:
            estimador = sum(valores) / n
            S = round(np.std(valores, ddof=1), 4)
            if round(np.sqrt(S)/np.sqrt(n), 4)  < 0.01:
                break
    return estimador, n, S

def monte_carlo_integral_ii(n_min=100, sigma_max=0.01):
    n = 0
    valores = []
    while True:
        x = np.random.normal(0,1)
        fx = x**2 * np.exp(-x**2)
        valores.append(fx)
        n += 1
        if n >= n_min:
            estimador = np.mean(valores) * np.sqrt(np.pi)
            S = np.std(valores, ddof=1) * np.sqrt(np.pi)
            if S / np.sqrt(n) < sigma_max:
                break
    return estimador, n, S

# Estimación de la primera integral
estimador_i, n_i, S_i = monte_carlo_integral_i()
print(f"Integral i) estimada: {estimador_i}, con {n_i} muestras, desviación estándar: {S_i}")

# Estimación de la segunda integral
estimador_ii, n_ii, S_ii = monte_carlo_integral_ii()
print(f"Integral ii) estimada: {estimador_ii}, con {n_ii} muestras, desviación estándar: {S_ii}")

