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
dvalor = d_estadistico(M, 12, mediaM, desviacionM)
pvalor = KS(10000, 12, dvalor)
print(f"Usando KS tenemos que el p-valor es {pvalor}")