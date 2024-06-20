from random import random

def ejercicio6a():
    enCirculo = 0
    # Calculo el primer valor
    u = 2 * random() - 1
    v = 2 * random() - 1
    if (u ** 2 + v ** 2 <= 1):
        enCirculo += 1
    # Inicializo variables del loop
    n = 1
    Scuad = 0
    Media = (4 * enCirculo) / n
    while (n < 100 or (Scuad/n) ** (1/2) >= 0.01):
        n += 1
        # Calculo nuevo valor
        u = 2 * random() - 1
        v = 2 * random() - 1
        if (u ** 2 + v ** 2 <= 1):
            enCirculo += 1
        # Actualizo valores
        MediaAnt = Media
        Media = (4 * enCirculo) / n
        Scuad = Scuad * (1 - 1 / (n - 1)) + n * (Media - MediaAnt) ** 2
    return n, Media, Scuad

def ejercicio6b():
    enCirculo = 0
    # Calculo el primer valor
    u = 2 * random() - 1
    v = 2 * random() - 1
    if (u ** 2 + v ** 2 <= 1):
        enCirculo += 1
    # Inicializo variables del loop
    n = 1
    Scuad = 0
    Media = (4 * enCirculo) / n
    while (n < 100 or (Scuad/n) ** (1/2) >= 5/196):
        n += 1
        # Calculo nuevo valor
        u = 2 * random() - 1
        v = 2 * random() - 1
        if (u ** 2 + v ** 2 <= 1):
            enCirculo += 1
        # Actualizo valores
        MediaAnt = Media
        Media = (4 * enCirculo) / n
        Scuad = Scuad * (1 - 1 / (n - 1)) + n * (Media - MediaAnt) ** 2
    return n, Media, Scuad


respuestaA = ejercicio6a()
print("\nSe necesitaron N =", respuestaA[0], "valores para obtener una aproximacion de Pi ~", respuestaA[1],
      "con desviacion menor a 0.01\n")

respuestaB = ejercicio6b()
print("Se necesitaron N =", respuestaB[0], "valores para obtener una aproximacion de Pi ~", respuestaB[1],
      "con un intervalo de confianza del 95%\n")