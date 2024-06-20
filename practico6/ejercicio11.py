from scipy.stats import chi2, binom
import numpy as np

def generarPi_agrupado():
    Pi = np.zeros(8, float)
    Pi[0] = binom.pmf(k=0, n=8, p=89/144) + binom.pmf(k=1, n=8, p=89/144)
    for i in range(7):
        Pi[i+1] = binom.pmf(k=i+2, n=8, p=89/144)
    return Pi

def generarPi():
    Pi = np.zeros(9, float)
    for i in range(9):
        Pi[i] = binom.pmf(k=i, n=8, p=89/144)
    return Pi


def pvalor_chi2_m(N, P, n, k, m):
    ''' N frecuencias, P probabilidades de F teorica, n tamaño muestra, k valores que toma la variable,
        m parametros estimados
    '''
    t = 0
    for i in range(k):
        t += ((N[i] - n * P[i]) ** 2) / (n * P[i])
    pvalor = 1 - chi2.cdf(t, k-1-m)
    return pvalor

P = generarPi()
pvalor = pvalor_chi2_m([0, 1, 2, 4, 1, 1, 2, 5, 2], P, 18, 9, 1)
print(f"Usando la aproximacion de chi-cuadrada tenemos que el p-valor es {pvalor}")