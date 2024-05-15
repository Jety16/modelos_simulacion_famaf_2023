import random
'''
Parte a) Demostración de la densidad triangular de X=U+VX=U+V:

Dado que U y V son variables aleatorias uniformes en el intervalo (0,1)(0,1), la densidad de probabilidad conjunta
de U y V es constante dentro del cuadrado unitario.
La suma X=U+V varía linealmente a medida que U y V varían de 0 a 1.
Por lo tanto, XX tiene una densidad triangular como se describe en la parte (a) del ejercicio.
'''


# i) Usando la propiedad de que X es la suma de dos uniformes
def generar_x_suma_uniformes():
    u = random.random()
    v = random.random()
    return u + v

# ii) Aplicando transformada inversa
def generar_x_transformada_inversa():
    return random.uniform(0, 1) + random.uniform(0, 1)

# iii) Con el método de rechazo
def generar_x_aceptacion_rechazo():
    while True:
        u = random.uniform(0, 1)
        v = random.uniform(0, 1)
        x = u + v
        if 0 <= x < 1:
            return x
        elif 1 <= x < 2:
            return 2 - x

def comparar_eficiencia():
    num_simulaciones = 10000

    # Método i) Usando la propiedad de que X es la suma de dos uniformes
    promedio_suma_uniformes = sum(generar_x_suma_uniformes() for _ in range(num_simulaciones)) / num_simulaciones

    # Método ii) Aplicando transformada inversa
    promedio_transformada_inversa = sum(generar_x_transformada_inversa() for _ in range(num_simulaciones)) / num_simulaciones

    # Método iii) Con el método de rechazo
    promedio_aceptacion_rechazo = sum(generar_x_aceptacion_rechazo() for _ in range(num_simulaciones)) / num_simulaciones

    print("Comparación de eficiencia:")
    print("Promedio - Suma de uniformes:", promedio_suma_uniformes)
    print("Promedio - Transformada inversa:", promedio_transformada_inversa)
    print("Promedio - Aceptación y rechazo:", promedio_aceptacion_rechazo)

comparar_eficiencia()

