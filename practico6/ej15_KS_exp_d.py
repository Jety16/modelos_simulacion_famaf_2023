from scipy.stats import expon, uniform

def media_muestral(xs):
    media = 0
    for x in xs:
        media += x
    return media/len(xs)
 
def d_estadistico(Y, n, theta): # Asumo que Y esta ordenado
    ''' Y muestra de n valores, n tamaño muestra
        theta es auxiliar para este ejercicio (es la media muestral)
    '''
    d = 0
    for i in range(n):
        f_yi = expon.cdf(Y[i], scale=theta)
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


M = [1.6, 10.3, 3.5, 13.5, 18.4, 7.7, 24.3, 10.7, 8.4, 4.9, 7.9, 12, 16.2, 6.8, 14.7]
M.sort()
mediaM = media_muestral(M)
dvalor = d_estadistico(M, 15, mediaM)
pvalor = KS(10000, 15, dvalor)
print(f"Usando KS tenemos que el p-valor es {pvalor}")