import numpy as np
from random import random, randint
import math

def simulate_X_inverse_transform(prob):
     u = random()
     cumulative_prob = 0
     for i in range(0, 1000):
        cumulative_prob += prob(10, i, 0.7)
        if u < cumulative_prob:
             return i

def numerador(i, lamd):
    return ((lamd**i) / math.factorial(i)) * (np.exp(-lamd))



def fun(k, i, lamd):
    denominador = 0
    for j in range(k+1):
        denominador += numerador(j, lamd)
    return numerador(i, lamd) / denominador

count = 0
print(1-(fun(10,0,0.7) + fun(10,1,0.7) + fun(10, 2, 0.7)))
for i in range(1000):
    X = simulate_X_inverse_transform(fun)
    if X <= 2:
        count += 1
print(1 - (count / 1000))


def simulate_Y(lamda):
    X = 0
    Producto = 1- random()
    cota = np.exp(-lamda)
    while Producto >= cota:
        Producto *= 1 - random()
        X += 1
    return X

def poisson(lamda, x):
   return np.exp(-lamda) * ((lamda ** x) / math.factorial(x))

def acep_rech():
    c = 1
    while True:
        Y = simulate_Y(0.7)
        U = random()
        if U < fun(10, Y, 0.7) / (c * poisson(0.7, Y)):
            return Y
count = 0
for i in range(1000):
    X = simulate_X_inverse_transform(fun)
    if X <= 2:
        count += 1
print(1-(count / 1000))

