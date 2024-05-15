import numpy as np
import random

# PASAR A LAS ACUMULADOS LRPM
def inverse_method_a():
    # Paso 1: Calcular la función de distribución acumulativa (CDF)
    def cdf_a(x):
        if 2 <= x < 3:
            return ((x - 2) ** 2) / 4
        elif 3 <= x <= 6:
            return ((x ** 2) / 6) - (x / 3) + 1/2
        else:
            return 0

    # Paso 2: Invertir la CDF
    def inverse_cdf_a(p):
        if 0 <= p < 1/4:
            return 2 * np.sqrt(p) + 2
        elif 1/4 <= p <= 1:
            return 3 - np.sqrt(3 - 2 * (2 * p - 1))

    # Paso 3: Generar variables aleatorias uniformes
    u = random.random()

    # Paso 4: Calcular las variables aleatorias según la densidad de probabilidad
    return inverse_cdf_a(u)

    # Ejemplo de uso
random_variables_a = inverse_method_a()
print(random_variables_a)



def inverse_method_b():
    # Paso 1: Calcular la función de distribución acumulativa (CDF)
    def cdf_a(x):
        if 0 <= x < 1:
            return 6*((x**2)/2 + 3*x) / 35
        elif 1 <= x <= 2:
            return (2*x**3)/35
        else:
            return 0

    # Paso 2: Invertir la CDF
    def inverse_cdf_a(p):
        if 0 <= p <= 0.6:
            return (3*p + np.sqrt(9*p**2 + 1680*p)) / 420
        else:
            return np.cbrt(35*p/2)

    # paso 3: Generar variables aleatorias uniformes
    u = random.random()

    # Paso 4: Calcular las variables aleatorias según la densidad de probabilidad
    return inverse_cdf_a(u)

random_variable_b = inverse_method_b()
print(random_variable_b)


def inverse_method_c():
    # Paso 1: Calcular la función de distribución acumulativa (CDF)
    def cdf_a(x):
        if x <= 0:
            return np.exp(4*x)/16
        elif 0 < x <= 15/4:
            return x/4
        else:
            return 0

    # Paso 2: Invertir la CDF
    def inverse_cdf_a(p):
        if 0 <= p <= 0.0625:
            return np.log(p*16)/4
        else:
            return 4*p
    #Paso 3: Generar variables aleatorias uniformes
    u = random.random()

    # Paso 4: Calcular las variables aleatorias según la densidad de probabilidad
    return inverse_cdf_a(u)

random_variable_b = inverse_method_b()
print(random_variable_b)
