import math
import random
import time

# Parte a) Métodos para generar la variable aleatoria X

# Método de Transformada Inversa
def generar_variable_transformada_inversa():
    u = random.random()  # Generar número aleatorio uniforme en (0,1)
    return math.exp(u)  # Aplicar la transformada inversa

# Método de Aceptación y Rechazo
def generar_variable_aceptacion_rechazo():
    C = math.e  # Constante de envolvente
    while True:
        x = random.uniform(1, math.e)  # Generar x uniformemente en el intervalo [1, e]
        y = random.uniform(0, C)  # Generar y uniformemente en el intervalo [0, C]
        if y <= 1 / x:
            return x

# Parte b) Comparación de eficiencia

def comparar_eficiencia():
    num_simulaciones = 10000

    # Medir tiempo y obtener promedio para el método de Transformada Inversa
    start_time = time.time()
    promedio_transformada_inversa = sum(generar_variable_transformada_inversa() for _ in range(num_simulaciones)) / num_simulaciones
    tiempo_transformada_inversa = time.time() - start_time

    # Medir tiempo y obtener promedio para el método de Aceptación y Rechazo
    start_time = time.time()
    promedio_aceptacion_rechazo = sum(generar_variable_aceptacion_rechazo() for _ in range(num_simulaciones)) / num_simulaciones
    tiempo_aceptacion_rechazo = time.time() - start_time

    print("Eficiencia:")
    print("Transformada Inversa - Promedio:", promedio_transformada_inversa, "Tiempo:", tiempo_transformada_inversa)
    print("Aceptación y Rechazo - Promedio:", promedio_aceptacion_rechazo, "Tiempo:", tiempo_aceptacion_rechazo)

# Parte c) Estimación de la probabilidad P(X <= 2)

def estimar_probabilidad():
    num_simulaciones = 100000
    conteo_transformada_inversa = sum(1 for _ in range(num_simulaciones) if generar_variable_transformada_inversa() <= 2)
    conteo_aceptacion_rechazo = sum(1 for _ in range(num_simulaciones) if generar_variable_aceptacion_rechazo() <= 2)

    probabilidad_transformada_inversa = conteo_transformada_inversa / num_simulaciones
    probabilidad_aceptacion_rechazo = conteo_aceptacion_rechazo / num_simulaciones

    print("\nEstimación de la probabilidad P(X <= 2):")
    print("Transformada Inversa:", probabilidad_transformada_inversa)
    print("Aceptación y Rechazo:", probabilidad_aceptacion_rechazo)

# Llamar a las funciones para ejecutar el ejercicio completo
comparar_eficiencia()
estimar_probabilidad()

