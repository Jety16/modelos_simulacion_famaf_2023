import numpy as np
from random import random

def Poisson_con_exp(lamda):
    X = 0
    Producto = 1- random()
    cota = np.exp(-lamda)
    while Producto >= cota:
        Producto *= 1 - random()
        X += 1
    return X

# Estimar P(Y > 2)
lambd = 10
simulations_common = 1000
samples_common = 0
r = 0
for i in range(simulations_common):
    samples_common = Poisson_con_exp(lambd)
    if samples_common <= 2:
        r += samples_common
    print(samples_common)

print (1-(r/1000))
