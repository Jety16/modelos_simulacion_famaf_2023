import numpy as np
from random import random, uniform

#Ejercicio 1b
print("\n\nEjercicio1b")
def aceptacion_rechazo(vector_probabilidades, valores_aleatorios):
    while True:
        # Usamos C == 1 ya que ambas distribuciones tienen las mismas cotas
        # Generar un índice aleatorio basado en la longitud del vector de probabilidades
        v = int(random() * len(vector_probabilidades))
        # Generar un valor aleatorio entre 0 y 1
        u = random()
        # Si el valor aleatorio es menor que la probabilidad correspondiente, aceptar
        if u < vector_probabilidades[v]:
            return valores_aleatorios[v]

# Vector de probabilidades de X y sus variables aleatorias correspondientes
probabilidades_X = [0.13, 0.22, 0.30, 0.35]
variables_X = [0, 1, 3, 2]

# Ejemplo de uso
for _ in range(10):  # Generar 10 valores aleatorios de X
    valor_X = aceptacion_rechazo(probabilidades_X, variables_X)
    print("Valor de X generado:", valor_X)
print("\n\nEjercicio2b")
#ejercicio 2b
def ej2b():
    u = random()
    if u < 2/3:
        return 0
    elif u > 2/3:
        return 2
    else:
        return 1

c=0
for _ in range(1000):
    x = ej2b()
    if x >=1:
        c +=1
print(c/1000)

print("\n\n ejercicio3")

def intensity(t):
    if 0<=t<3:
        return 5 +5*t
    elif 3<t<=5:
        return 20
    elif 5<t<=9:
        return 30-2*t
    else:
        return 0

def Poisson_adelgazamiento_mejorado(T, interv, lamda):
    j = 0 #recorre subintervalos.
    t = -np.log ( 1 - random() ) / lamda[j]
    NT = 0
    Eventos = []
    while t <= T:
        if t <= interv[j]:
            V = random()
            if V < (2 * t + 1) / lamda[j]:
                NT += 1
                Eventos.append(t)
            t += -np.log(1 - random()) / lamda[j]
        else: #t > i    nterv[j]
            t = interv[j] + (t - interv[j]) * lamda[j] / lamda[j + 1]
            j += 1
    return NT, Eventos


def hot_dog(T):
    r = []
    while 9>=T>=0:
        r.append((f"T: {T}:",
            Poisson_adelgazamiento_mejorado(T, [0,1,2,6,8,9], [5, 10, 15, 18, 14, 12])[1]
            ))
        T=T-1
    return r

for i in hot_dog(3):
    print(i[0], i[1])

#Ejercicio4
def area(N):
    count_inside = 0
    total_points = N
    rect_area = 3 * 3  # Área del rectángulo definido por los vértices

    for _ in range(N):
        x = uniform(-1.5, 1.5)
        y = uniform(-1.5, 1.5)

        # Verificar si el punto está dentro de la curva
        if x**2 + (y - abs(x)**(3/2))**2 <= 1:
            count_inside += 1

    # Calcular el área estimada
    curve_area = (count_inside / total_points) * rect_area
    return curve_area

# Estimar el área con N = 100000
estimated_area = area(100000)
print("Expected area: 3.1415", "Simulation:", round(estimated_area, 6))
# Para estimar el área encerrada por la curva podemos realizar el siguiente algoritmo basado en montecarlo pero sin tener que realizar integrales
# Definir el dominio de la curva: En este caso, el dominio de la curva es el rectángulo delimitado por los vértices (-1.5, -1.5), (-1.5, 1.5), (1.5, 1.5) y (1.5, -1.5).
# Generar puntos aleatorios dentro del rectángulo: Utilizamos un generador de números aleatorios para generar puntos aleatorios dentro del rectángulo definido en el paso 1.
# Contar puntos dentro de la curva: Para cada punto generado en el paso anterior, verificamos si está dentro de la curva dada por la ecuación x2+(y−∣x∣32)2=1x2+(y−∣x∣23​)2=1. Si el punto satisface esta ecuación, entonces está dentro de la curva.
# Calcular el área estimada: El área encerrada por la curva puede estimarse dividiendo el número de puntos dentro de la curva entre el número total de puntos generados y multiplicando por el área del rectángulo.
# El método de Monte Carlo se basa en la ley de los grandes números, que establece que, a medida que aumenta el número de muestras, la estimación converge al valor real del área encerrada por la curva.
