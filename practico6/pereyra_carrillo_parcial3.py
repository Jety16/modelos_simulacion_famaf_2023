# Ejercicio2
print("Running Ejercicio2 :D")

from scipy.stats import norm, uniform

def media_muestral(xs):
    media = 0
    for x in xs:
        media += x
    return media/len(xs)

def desviacion_muestral(xs, media): # xs no puede tener un solo elemento
    desviacion = 0
    for x in xs:
        desviacion += (x - media) ** 2
    return (desviacion/(len(xs) - 1)) ** (1/2)  
 
def d_estadistico(Y, n, theta1, theta2): # Asumo que Y esta ordenado
    ''' Y muestra de n valores, n tamaño muestra
        theta1, theta2 son auxiliares para este ejercicio (es la media muestral)
    '''
    d = 0
    for i in range(n):
        f_yi = norm.cdf(Y[i], loc=theta1, scale=theta2) # loc es la media y scale es la desviacion
        d = max(d, ((i + 1) / n) - f_yi, f_yi - (i/n))
    return d

def KS(Nsim, n, d_valor):
    ''' Nsim simulaciones, n tamaño de la muestra, d_valor obtenido de la muestra
    '''
    pvalor = 0
    for _ in range(Nsim):
        uniformes = uniform.rvs(size=n)
        uniformes.sort()
        d_j = 0
        for j in range(n):
            u_j = uniformes[j]
            d_j = max(d_j, ((j + 1) / n) - u_j, u_j - (j / n))
        if d_j >= d_valor:
            pvalor += 1
    return pvalor/Nsim


M = [1.628, 1.352, 1.800, 1.420, 1.594, 2.132, 1.614, 1.924, 1.692]
M.sort()
mediaM = media_muestral(M)
desviacionM = desviacion_muestral(M, mediaM)
dvalor = d_estadistico(M, len(M), mediaM, desviacionM)
pvalor = KS(10000, len(M), dvalor)
print(f"Usando KS tenemos que el p-valor es {pvalor}")
print(f"Media muestral {mediaM}")
print(f"Desviacion Estandar {desviacionM}")
print("D_valor observado", dvalor)

# Variables uniformes simuladas
U = [0.23, 0.12, 0.45, 0.67, 0.01, 0.51, 0.38, 0.92, 0.84]

# Convertir uniformes a la distribución normal N(mu_hat, sigma_hat)
simulated_data = norm.ppf(U, loc=mediaM, scale=desviacionM)

# Realizar el test de Kolmogorov-Smirnov en los datos simulados
D_simulated = d_estadistico(simulated_data, len(simulated_data), mediaM, desviacionM)

print("D Valor con variables uniformes: ", D_simulated)

print("\n Runing Ejercicio3 e.e")
from scipy.stats import chi2, binom
import numpy as np

def pvalor_chi2(N, P, n, k):
    ''' N frecuencias, P probabilidades de F teorica, n tamaño muestra, k valores que toma la variable '''
    t = 0
    for i in range(k):
        t += ((N[i] - n * P[i]) ** 2) / (n * P[i])
    pvalor = 1 - chi2.cdf(t, k-2)
    return pvalor

def t_estadistico(N, P, n, k):
    ''' N frecuencias, P probabilidades de F teorica, n tamaño muestra, k valores que toma la variable '''
    t = 0
    for i in range(k):
        t += ((N[i] - n * P[i]) ** 2) / (n * P[i])
    return t

def pvalor_sim(Nsim, P, n, k, t_valor):
    ''' Nsim numeros de simulaciones, P probabilidades de F teorica, n tamaño muestra, 
        k valores que toma la variable, t_valor de la muestra original '''
    N = np.zeros(k, int)    # Frecuencias observadas
    pvalor = 0
    for _ in range(Nsim):
        # Calculo las frecuencias observadas
        n_rest = n
        p_acum = 0
        for j in range(k):
            p_rest = P[j] / (1 - p_acum)
            N[j] = binom.rvs(n_rest, p_rest)
            n_rest = n_rest - N[j] if N[j] < n_rest else 0
            p_acum += P[j]
        # Calculo el valor t_i
        t_i = 0
        for i in range(k):
            t_i += ((N[i] - n * P[i]) ** 2) / (n * P[i])
        # Verifico si es mayor al t_valor
        if (t_i >= t_valor):
            pvalor += 1
    return pvalor / Nsim

# Datos específicos del problema
frecuencias_observadas = [490, 384, 111, 15]
probabilidades_teoricas = [0.4804, 0.3998, 0.1041, 0.0157]
total_macetas = 1000
num_valores = 4

# Calcular el p-valor usando la aproximación de chi-cuadrado
pvalor_chi2_aprox = pvalor_chi2(frecuencias_observadas, probabilidades_teoricas, total_macetas, num_valores)
print(f"Usando la aproximación de chi-cuadrado tenemos que el p-valor es {pvalor_chi2_aprox}")

# Calcular el valor del estadístico t
t_valor = t_estadistico(frecuencias_observadas, probabilidades_teoricas, total_macetas, num_valores)

# Calcular el p-valor usando simulaciones
pvalor_simulado = pvalor_sim(10000, probabilidades_teoricas, total_macetas, num_valores, t_valor)
print(f"Usando simulaciones tenemos que el p-valor es {pvalor_simulado}")



#EJercicio4
print("\n\n Running Ejercicio4, em se tarda bastante pero tengale paciencia..." )
import numpy as np
from random import random

# Definimos la función que corresponde a la integral transformada
def gI(u):
    return u / ((1 - u)**3 + u**4 * (1 - u))


def ejercicio4a(fun, d):
    Media = fun(random())   # Genero una g(U)
    Scuad = 0
    n = 1
    while (n < 100 or (Scuad/n) ** (1/2) >= d):
        n += 1
        X = fun(random())   # Genero una g(U)
        MediaAnt = Media
        Media = MediaAnt + (X - MediaAnt) / n
        Scuad = Scuad * (1 - 1 / (n - 1)) + n * (Media - MediaAnt) ** 2
        print((Scuad/n)**1/2)
    I95_izq = Media - 1.96 * (Scuad/n) ** (1/2)
    I95_der = Media + 1.96 * (Scuad/n) ** (1/2)
    return n, Media, Scuad ** (1/2), I95_izq, I95_der

#respuestaI = ejercicio4a(gI, 0.001)
#print("\nEl numero de datos generados para la integral I es", respuestaI[0])
#print("La aproximacion de la integral I es", respuestaI[1])
print("El valor exacto de la integral I es", "no llegue a calcularlo gg")   # Usando integracion numerica

def ejercicio4b(fun, N):
    Media = fun(random())   # Genero una g(U)
    Scuad = 0
    n = 1
    while (n < N):
        n += 1
        X = fun(random())   # Genero una g(U)
        MediaAnt = Media
        Media = MediaAnt + (X - MediaAnt) / n
        Scuad = Scuad * (1 - 1 / (n - 1)) + n * (Media - MediaAnt) ** 2
    I95_izq = Media - 1.96 * (Scuad/n) ** (1/2)
    I95_der = Media + 1.96 * (Scuad/n) ** (1/2)
    return Media, Scuad ** (1/2), I95_izq, I95_der

print("\nIntregal I")

respuestaI_1000 = ejercicio4b(gI, 1000)
print("\nPara N = 1000, los valores de la integral I son: ")
print("Media muestral es", respuestaI_1000[0])
print("Desviacion estandar muestral es", respuestaI_1000[1])
print("Intervalo de Confianza 95 es (", respuestaI_1000[2], ",", respuestaI_1000[3], ")")

respuestaI_5000 = ejercicio4b(gI, 5000)
print("\nPara N = 5000, los valores de la integral I son: ")
print("Media muestral es", respuestaI_5000[0])
print("Desviacion estandar muestral es", respuestaI_5000[1])
print("Intervalo de Confianza 95 es (", respuestaI_5000[2], ",", respuestaI_5000[3], ")")

respuestaI_7000 = ejercicio4b(gI, 7000)
print("\nPara N = 7000, los valores de la integral I son: ")
print("Media muestral es", respuestaI_7000[0])
print("Desviacion estandar muestral es", respuestaI_7000[1])
print("Intervalo de Confianza 95 es (", respuestaI_7000[2], ",", respuestaI_7000[3], ")")
