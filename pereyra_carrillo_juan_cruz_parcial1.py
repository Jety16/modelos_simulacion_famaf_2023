from random import random
import numpy as np
import math

# Integral Monte Carlo en el intervalo (0,1)
def MonteCarlo_01(fun, Nsim):
    Integral = 0
    for _ in range(Nsim):
        Integral += fun(random())
    return Integral / Nsim

# Integral Monte Carlo en el intervalo (0,inf)
def MonteCarlo_inf(fun, Nsim):
    Integral=0
    for _ in range(Nsim):
        u=random()
        Integral+= fun(1/u-1)/(u**2)
    return Integral / Nsim

def function_to_integrate(u):
    return 1 / ((np.log((1/u+1) +1))*(1/(u+1))**2)

def function_to_integrate2(u):
    return 1 / ((math.log(u+2))*(u)**2)


N = [1000,10000,100000]
for i in range(len(N)):
  first_integral = MonteCarlo_01(function_to_integrate, N[i])
  second_integral = MonteCarlo_inf(function_to_integrate, N[i])
  print(second_integral-first_integral)
