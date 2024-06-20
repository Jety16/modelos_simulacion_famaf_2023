from random import random
import numpy as np

def Poisson_no_homogeneo_adelgazamiento(T, lamda, lamda_t):
    # 'Devuelve el n´umero de eventos NT y los tiempos en Eventos'
    # 'lamda_t(t): intensidad, lamda_t(t)<=lamda'
    NT = 0
    Eventos = []
    U = 1 - random()
    t = -np.log(U) / lamda
    while t <= T:
        V = random()
        if V < lamda_t(t) / lamda:
            NT += 1
            Eventos.append(t)
            t += -np.log(1 - random()) / lamda
    return NT, Eventos

def intensity(t):
    if 0<=t<3:
        return 5 +5*t
    elif 3<t<=5:
        return 20
    elif 5<t<=9:
        return 30-2*t

#print(Poisson_no_homogeneo_adelgazamiento(2, 4, a))
#print(Poisson_no_homogeneo_adelgazamiento(2, 1, b))
# print(Poisson_no_homogeneo_adelgazamiento(4, 1, c))

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

print(Poisson_adelgazamiento_mejorado(2, [1,2,3], [5, 3+4/3, 4]))
print(Poisson_adelgazamiento_mejorado(2, [2,3,5], [7, 2, 1]))
print(Poisson_adelgazamiento_mejorado(3, [0,3,6], [0, 0.5, 0.5]))


