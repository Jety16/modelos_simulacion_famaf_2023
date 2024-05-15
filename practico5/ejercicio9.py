import numpy as np
from random import random

# metodo basico
def gen_z_normal(mu, sigma):
    # Simulacion de v.a normal con  exponenciales
    while True:
        Y1 = -np.log(random())
        Y2 = -np.log(random())
        if Y2 >=(Y1-1) ** 2 / 2:
            if random() < 0.5:
                return Y1 * sigma + mu
            return -Y1 * sigma + mu

def Normal_composicion(mu, sigma):
    Z = gen_z_normal(mu, sigma)
    if random() < 0.5:
        return np.abs(Z)
    else:
        return -np.abs(Z)

# Metodo polar
def MetodoPolar(mu, sigma):
    Rcuadrado = -2 * np.log( 1 - random() )
    Theta = 2 * np.pi * random()
    X = np.sqrt(Rcuadrado) * np.cos(Theta)
    Y = np.sqrt(Rcuadrado) * np.sin(Theta)
    return (X * sigma + mu, Y * sigma + mu)

# Metodo razon entre uniformes
from math import exp
NV_MAGICCONST = 4 * np.exp(-0.5) / np.sqrt(2.0)

def normalvariate(mu, sigma):
    while 1:
        u1 = random()
        u2 = 1.0 - random()
        z = NV_MAGICCONST * (u1 - 0.5) / u2
        zz = z * z / 4.0
        if zz <= -np.log(u2):
            break
    return mu + z * sigma
m1 = 0
m2 = 0
m3 = 0
v1=0
v2=0
v3=0
for _ in range(10000):
    m1 += Normal_composicion(3,2)/10000
    m2 += MetodoPolar(3,2)[0]/10000
    m3 += normalvariate(3,2)/10000
    v1 += (Normal_composicion(3,2))**2
    v2 += (MetodoPolar(3,2)[0])**2
    v3 += (normalvariate(3,2))**2

print(f"Medias: original=3  m1={m1} m2={m2} m3={m3}")
print(f"Varianza: original={3**2} v1={(v1/10000)-2**2} v2={(v2/10000)-2**2} v3={(v3/10000)-2**2}")

