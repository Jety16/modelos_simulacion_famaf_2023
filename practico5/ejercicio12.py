import numpy as np
from random import random

import matplotlib.pyplot as plt
def inversa(lamda):
    u = random()
    return np.tan(u*np.pi) *lamda

print(inversa(1))
import random
import math

def cauchy(lamda):
    while True:
        U = random.random()
        V = random.random() * lamda * 2 - lamda
        if U**2 + (lamda * V)**2 < 1:
            return U, V

def normal_pdf(x):
    return math.exp(-x**2 / 2) / math.sqrt(2 * math.pi)

def normal_cdf(x):
    return (1 + math.erf(x / math.sqrt(2))) / 2

def cauchy_pdf(x, lamda):
    return 1 / (math.pi * lamda * (1 + (x / lamda)**2))

def cauchy_cdf(x, lamda):
    return (1 / math.pi) * math.atan(x / lamda) + 0.5

def accept_reject_cdf(lamda, num_samples):
    samples = []
    c = math.sqrt(2 * math.pi) * lamda  # Constante de normalización para f(x) <= c * g(x)
    while len(samples) < num_samples:
        U = random.random()
        X = normal_cdf(random.random())  # Inversa de la CDF de la normal estándar
        if U <= cauchy_pdf(X, lamda) / (c * normal_pdf(X)):
            samples.append(X)
    return samples

# Ejemplo de uso
lamda = 1
num_samples = 10000
samples = accept_reject_cdf(lamda, num_samples)

# Graficar histograma de las muestras generadas
plt.hist(samples, bins=50, density=True, color='skyblue', edgecolor='black')
plt.title('Histograma de la distribución de Cauchy utilizando aceptación y rechazo')
plt.xlabel('Valor de X')
plt.ylabel('Densidad de probabilidad')
plt.grid(True)
plt.show()

