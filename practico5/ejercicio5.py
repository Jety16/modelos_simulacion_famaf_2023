import numpy as np
import random

def generate_variable(rate):
    return -np.log(random.random()) / rate
M = []
m = []
for _ in range(10):
    # Generar variables aleatorias exponenciales independientes
    X1 = generate_variable(1)
    X2 = generate_variable(2)
    X3 = generate_variable(3)

    # Generar M
    M.append(X1 * X2 * X3)

    # Generar m
    m.append(1 - (1 - X1) * (1 - X2) * (1 - X3))

print("Variable M:", M)
print("Variable m:", m)

