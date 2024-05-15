import numpy as np
from random import random

def discretaX(p, x):
    U = random()
    i, F = 0, p[0]
    while U >= F:
        i +=1; F += p[i]
    return x[i]

ps = [0.11, 0.14, 0.09, 0.08, 0.12, 0.1, 0.09, 0.07, 0.11, 0.09]
print(discretaX(sorted(ps),  range(10)))

def idk(Y, p, c):
    while True:
        U = random()
        if U < 0.1 / (c * p[Y]):
            return Y ## aceptaci´on: X=Y

i = idk(discretaX(sorted(ps),  range(10)), ps, 1.2)
print(i)

a = '''Primero, se crea un arreglo A de tamaño 100.
    Luego, cada valor pi en tu lista original ps se multiplica por 100 para obtener el número de posiciones que ese valor ocupará en el arreglo A. Por ejemplo, si pi = 0.11, entonces ocupará 11 posiciones en A.
    Ahora, cada posición en el arreglo A corresponde a uno de los valores originales pi. Cuantas más veces aparezca un valor en el arreglo A, mayor será la probabilidad de que se seleccione al azar.
    Finalmente, para seleccionar un elemento A[k] con una probabilidad del 0.01, simplemente se accede al índice k del arreglo A. Debido a que los valores de A están distribuidos de acuerdo con las probabilidades originales pi, seleccionar un elemento al azar de A con igual probabilidad es equivalente a seleccionar un valor pi con una probabilidad de 0.01.

Por lo tanto, el método funciona porque utiliza las probabilidades originales pi para distribuir los elementos en el arreglo A, y luego simplemente selecciona un elemento de A al azar, lo que garantiza que cada pi tenga una probabilidad de selección de 0.01'''

print(a)
