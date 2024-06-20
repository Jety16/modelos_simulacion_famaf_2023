import random
import numpy as np


def simulation():
    ret = 0
    n = 0
    while True:
        n = n+1
        ret += random.random()
        if ret > 1:
            return n
# a esto se debe a que u toma valores (0, 1) 
# Por ende para sumar mayor que uno por lo menos debemos sumar 2 numeros
# ---> min n = 2
# esto ocurre si U_1 = x y U_2 > 1-x 


def ejercicio4b():
    Media = simulation()
    varianza = 0
    n = 1
    while (n < 1000):
        n += 1
        X = simulation()
        MediaAnt = Media
        Media = MediaAnt + (X - MediaAnt) / n
        varianza = varianza * (1 - 1 / (n - 1)) + n * (Media - MediaAnt) ** 2
    return Media, (varianza/n)
print(ejercicio4b())


from random import random

def generarN():
    sum = random()
    N = 1
    while (sum <= 1):
        sum += random()
        N += 1
    return N     

# Revisar el estimador de maxima verosimilitud y la derivacion de expresion de varianza

def ejercicio4b():
    Media = generarN()
    Scuad = 0
    n = 1
    while (n < 1000):
        n += 1
        X = generarN()
        MediaAnt = Media
        Media = MediaAnt + (X - MediaAnt) / n
        Scuad = Scuad * (1 - 1 / (n - 1)) + n * (Media - MediaAnt) ** 2
    return Media, (Scuad/n)

# Revisar intervalos de confianza
def ejercicio4c():
    Media = generarN()
    Scuad = 0
    n = 1
    while (n < 100 or (Scuad/n) ** (1/2) >= 5/784):
        n += 1
        X = generarN()
        MediaAnt = Media
        Media = MediaAnt + (X - MediaAnt) / n
        Scuad = Scuad * (1 - 1 / (n - 1)) + n * (Media - MediaAnt) ** 2
    I95_izq = Media - 1.96 * (Scuad/n) ** (1/2)
    I95_der = Media + 1.96 * (Scuad/n) ** (1/2)
    return Media, I95_izq, I95_der

respuestab = ejercicio4b()
print("\nCon 1000 simulaciones tenemos que la media muestral es", respuestab[0], "y su varianza es", respuestab[1])

respuestac = ejercicio4c()
print("\nCon IC del 95 y intervalo a lo sumo 0.025, la media muestral es", respuestac[0], "y el intervalo es de largo", 
      respuestac[2] - respuestac[1], "\n")