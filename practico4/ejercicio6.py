import numpy as np

# Función de probabilidad puntual de X
probabilities = [0.15, 0.20, 0.10, 0.35, 0.20]

def simulate_X_inverse_transform():
    u = np.random.uniform(0, 1)
    cumulative_prob = 0
    for i, prob in enumerate(probabilities):
        cumulative_prob += prob
        if u < cumulative_prob:
            return i

# Realizar 10000 simulaciones
simulations_inverse = [simulate_X_inverse_transform() for _ in range(10000)]

def simulate_X_acceptance_rejection():
    while True:
        # Generar una variable binomial Y con parámetros n=4 y p=0.45
        Y = np.random.binomial(4, 0.45)
        # Generar un número aleatorio U entre 0 y 1
        u = np.random.uniform(0, 1)
        # Calcular la probabilidad de Y según la función de probabilidad puntual de X
        p_Y = probabilities[Y]
        # Si el valor de u está dentro del rango de aceptación, devolver Y
        if u < max(probabilities) / p_Y:
            print(p_Y, max(probabilities), max(probabilities) / p_Y)
            return Y

# Realizar 10000 simulaciones
simulations_acceptance_rejection = [simulate_X_acceptance_rejection() for _ in range(10000)]
print(simulations_acceptance_rejection)
import time

# Método de la transformada inversa
start_time_inverse = time.time()
simulations_inverse = [simulate_X_inverse_transform() for _ in range(10000)]
elapsed_time_inverse = time.time() - start_time_inverse

# Método de aceptación y rechazo
start_time_acceptance_rejection = time.time()
simulations_acceptance_rejection = [simulate_X_acceptance_rejection() for _ in range(10000)]
elapsed_time_acceptance_rejection = time.time() - start_time_acceptance_rejection

# Resultados
print("Tiempo de ejecución del método de la transformada inversa:", elapsed_time_inverse, "segundos")
print("Tiempo de ejecución del método de aceptación y rechazo:", elapsed_time_acceptance_rejection, "segundos")

