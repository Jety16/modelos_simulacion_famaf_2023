import random
import time

def binomial_transformada_inversa(n, p):
    U = random.random()  # Generar una variable aleatoria uniforme entre 0 y 1
    cumulative_prob = 0
    k = 0
    while cumulative_prob <= U:
        cumulative_prob += (1 - p) ** k * p ** (n - k) * (factorial(n) / (factorial(k) * factorial(n - k)))
        k += 1
    return k - 1

def binomial_simulacion(n, p):
    successes = sum(1 for _ in range(n) if random.random() < p)  # Simulando n ensayos y contando los éxitos
    return successes

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Parámetros
n = 10
p = 0.3
num_simulaciones = 10000

# Tiempo para transformada inversa
start_time = time.time()
resultados_transformada_inversa = [binomial_transformada_inversa(n, p) for _ in range(num_simulaciones)]
tiempo_transformada_inversa = time.time() - start_time

# Tiempo para simulación
start_time = time.time()
resultados_simulacion = [binomial_simulacion(n, p) for _ in range(num_simulaciones)]
tiempo_simulacion = time.time() - start_time

print("Tiempo necesario para realizar 10000 simulaciones:")
print("Usando transformada inversa:", tiempo_transformada_inversa, "segundos")
print("Usando simulación:", tiempo_simulacion, "segundos")
# Valor con mayor ocurrencia
valor_mas_comun = max(set(resultados_transformada_inversa), key=resultados_transformada_inversa.count)
ocurrencias_valor_mas_comun = resultados_transformada_inversa.count(valor_mas_comun)

# Proporción de veces que se obtuvieron los valores 0 y 10
proporcion_0 = resultados_transformada_inversa.count(0) / num_simulaciones
proporcion_10 = resultados_transformada_inversa.count(10) / num_simulaciones

print("Valor con mayor ocurrencia:", valor_mas_comun)
print("Número de ocurrencias del valor más común:", ocurrencias_valor_mas_comun)
print("Proporción de veces que se obtuvo el valor 0:", proporcion_0)
print("Proporción de veces que se obtuvo el valor 10:", proporcion_10)

# Probabilidades teóricas de la binomial
probabilidad_0_teórica = (1 - p) ** n
probabilidad_10_teórica = p ** 10 * (1 - p) ** (n - 10) * (factorial(n) / (factorial(10) * factorial(n - 10)))

print("\nProbabilidades teóricas:")
print("Probabilidad teórica de obtener el valor 0:", probabilidad_0_teórica)
print("Probabilidad teórica de obtener el valor 10:", probabilidad_10_teórica)

