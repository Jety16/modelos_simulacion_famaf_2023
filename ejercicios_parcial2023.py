#ej1
#  x: vector de valores posibles de X
# p: vector de probabilidades

from random import random

p = [0.24,0.09,0.31,0.36]

def discretaX(p):
  U = random()
  i, F = 0, p[0]
  while U >= F:
    i +=1; F += p[i]
  return i

#Ej2
from random import random

def G(u) :
  if(u <= 0.5) :
    return u*4
  else :
    return 1/(1-u)

def Tinversa():
  U=random()
  return G(U) # G = F −1

def ej2b() :
  exitos = 0
  for _ in range(10000) :
    if (Tinversa() <= 3) :
      exitos +=1
  print (f'P(x<= 3) = {exitos/10000}')

ej2b()

#Ej3
from random import random
import math

p = 0.6

def geometrica(p):
  U = random()
  return int(math.log(1-U)/math.log(1-p))+1

def GenX() :
  while True :
    y = geometrica()
    if( y <= 20) :
      return y

#Ej4
import math

def eventosPoisson(lamda):
  t = 0
  NT = 0
  Eventos = []
  T = 50
  while NT < T :
    U = 1 - random()
    t = - math.log(U) / lamda
    if NT <= T:
      NT += 1
      Eventos.append(t)
  return Eventos


print(f'{eventosPoisson(1/800)}')

def simulacion(Nsim) :
  exitos = 0
  for i in range(Nsim) :
    x = sum(eventosPoisson(1/800))
    #print({x})
    if (sum(eventosPoisson(1/800)) > 50_000) :
      exitos +=1

  print(f'la prob de que los reclamos salgan mas de 50000 en el mes siguiente es de {exitos/Nsim}')

simulacion(10_000)
