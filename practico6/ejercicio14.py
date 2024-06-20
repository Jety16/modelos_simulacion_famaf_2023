from scipy.stats import uniform, norm
import random
import math

def tstudent_gen(df):
    x = random.gauss(0, 1)
    y = 2 * random.gammavariate(0.5 * df, 2)
    return x / ((y / df) ** (1/2))

def fda_normal(x):
    return (math.erf(x / (2 ** (1/2))) / 2) + 0.5

def d_estadistico(Y, F, n): # Asumo que Y esta ordenado
    ''' Y muestra de n valores, F fda de la distribucion teorica
    '''
    d = 0
    for i in range(n):
        f_yi = F(Y[i])
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

def KS_op(Nsim, F, n, d_valor):
    ''' Nsim simulaciones, n tamaño de la muestra, d_valor obtenido de la muestra
        F fda de la distribucion teorica
    '''
    pvalor = 0
    for _ in range(Nsim):
        normales = norm.rvs(size=n)
        normales.sort()
        d_j = 0
        for j in range(n):
            f_j = F(normales[j])
            d_j = max(d_j, ((j + 1) / n) - f_j, f_j - (j / n))
        if d_j >= d_valor:
            pvalor += 1
    return pvalor/Nsim

# Genero Muestra T-Students 11 ordenadas
muestra10 = []
muestra20 = []
muestra1000 = []
for _ in range(10):
    muestra10.append(tstudent_gen(11))
for _ in range(20):
    muestra20.append(tstudent_gen(11))
for _ in range(1000):
    muestra1000.append(tstudent_gen(11))
muestra10.sort()
muestra20.sort()
muestra1000.sort()

# Obtengo Valor D del Estadistico
d10 = d_estadistico(muestra10, fda_normal, 10)
d20 = d_estadistico(muestra20, fda_normal, 20)
d1000 = d_estadistico(muestra1000, fda_normal, 1000)

# Obtengo P-Valor usando simulaciones con uniformes
p10 = KS(10000, 10, d10)
p20 = KS(10000, 20, d20)
p1000 = KS(10000, 1000, d1000)

# Obtengo P-Valor_op usando simulaciones con uniformes
p10_op = KS_op(10000, fda_normal, 10, d10)
p20_op = KS_op(10000, fda_normal, 20, d20)
p1000_op = KS_op(10000, fda_normal, 1000, d1000)

# Impresion por pantalla
print("Tamaño Muestra    Valor Estadistico D       P-valor")
print(f"    {10}            {d10}       {p10}")
print(f"    {20}            {d20}       {p20}")
print(f"   {1000}           {d1000}       {p1000}")

# Impresion por pantalla
print("\nTamaño Muestra    Valor Estadistico D       P-valor_op")
print(f"    {10}            {d10}       {p10_op}")
print(f"    {20}            {d20}       {p20_op}")
print(f"   {1000}           {d1000}       {p1000_op}")