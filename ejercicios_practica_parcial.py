import numpy as np
from random import random

# Integral Monte Carlo en el intervalo (0,1)
def MonteCarlo_01(fun, Nsim):
    Integral = 0
    for _ in range(Nsim):
        Integral += fun(random())
    return Integral/Nsim

# Integral Monte Carlo en el intervalo (a,b)
def MonteCarlo_ab(fun, a, b, Nsim):
    Integral = 0
    for _ in range(Nsim):
        Integral += fun(a + (b-a)*random())
    return Integral*(b-a)/Nsim #Aquí multiplico una sola vez por (b-a)

# Integral Monte Carlo en el intervalo (0,inf)
def MonteCarlo_inf(fun, Nsim):
    Integral=0
    for _ in range(Nsim):
        u=random()
        Integral+= fun(1/u-1)/(u**2)
    return Integral/Nsim

def g_a(u):
  return (1 - u**2)**(3/2)


N = [100,1000,10000,100000,1000000]
for i in range(len(N)):
  print('Integral para Nsim =',N[i])
  print(MonteCarlo_01(g_a,N[i]))
  print('-------------------')
print('El valor real aproximado es 3pi/16 ~',3*np.pi/16)







from random import random
# Integral Monte Carlo en el intervalo (0,1)x(0,1)
def MonteCarlo_01_2(fun, Nsim):
    Integral = 0
    for _ in range(Nsim):
        Integral += fun(random(), random())
    return Integral/Nsim

# Integral Monte Carlo en el intervalo (a,b)x(c,d)
def MonteCarlo_ab_2(fun,a,b,c,d, Nsim):
    Integral = 0
    for _ in range(Nsim):
        Integral += fun(a + (b-a)*random(), c + (d-c)*random())
    return Integral*(b-a)*(d-c)/Nsim

# Integral Monte Carlo en el intervalo (0,inf)x(0,inf)
def MonteCarlo_inf_2(g, Nsim):
    Integral=0
    for _ in range(Nsim):
        u1=random()
        u2=random()
        Integral+= g(1/u1-1, 1/u2-1)/((u1**2)*(u2**2))
    return Integral/Nsim












