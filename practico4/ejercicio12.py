import numpy as np

def SimularVariable(p1, p2):
    r = np.random.random()  # Genera un número aleatorio entre 0 y 1
    X = int(np.log(1 - r) / np.log(1 - p1)) + 1
    Y = int(np.log(1 - r) / np.log(1 - p2)) + 1
    return min(X, Y)

# Ejemplo de uso para simular una variable con los parámetros dados
resultado = SimularVariable(0.05, 0.2)
print("Variable simulada:", resultado)

# El algoritmo dado simula una variable aleatoria que devuelve el mínimo de dos variables, donde cada variable es una variable aleatoria geométrica.

# La variable aleatoria geométrica modela el número de ensayos de Bernoulli independientes y
# de idéntica distribución de probabilidad requeridos antes de obtener el primer éxito. Es decir, si p es la
# probabilidad de éxito en un solo ensayo de Bernoulli, entonces la variable aleatoria geométrica X con parámetro p
# tiene como posibles valores 1, 2, 3, ... con probabilidades (1-p)*p^(x-1).


