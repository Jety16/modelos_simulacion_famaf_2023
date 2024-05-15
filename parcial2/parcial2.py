from random import random
import numpy as np
import math

def generarX():
    U=random()
    if U<0.22:
       return 1
    elif U<0.55:
       return 4
    elif U<0.72:
       return 9
    elif U<0.9999:
       return 16
    else:
        return 100**2
e = 0
for _ in range(10000):
    e += generarX() / 10000
print(e)
