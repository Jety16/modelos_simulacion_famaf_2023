import numpy as np
import random
import math

def pareto(a,x):
    return a*(x**(-a+1))

def inverse_method(a):
    # Paso 1: Calcular la función de distribución acumulativa
    def pareto_integral(a,x):
        return 1-((1/x)**a)
    # Paso 2: Invertir la CDF
    def pareto_inverse(a, x):
        return np.sqrt(-1/(x-1))
        # Paso 3: Generar variables aleatorias uniformes
    u = random.random()

    # Paso 4: Calcular las variables aleatorias según la densidad de probabilidad
    return pareto_inverse(a, u)

a = 2
r = 0
for i in range(10000):
    random_variable_b = inverse_method(a)
    r =+ random_variable_b * pareto(2, random_variable_b)
print(r)


#Erlang

def DosExp(lamda):
    V1, V2 = 1-random.random(), 1-random.random()
    t = -np.log(V1 * V2) / lamda
    U = random.random()
    X = t * U
    Y = t - X
    return X, Y

def sum_exps(n,lam) :
    X, Y = DosExp(lam)
    return X+Y
r = 0
for _ in range(10000) :
    r += sum_exps(2, 1/2)
print(r/10000)

