from random import random, randint

def q(x):
    return 1/5

def p(x):
    if x == 4:
        return  0.35
    elif x == 3:
        return 0.3
    elif x == 2:
        return 0.2
    elif x == 1:
        return 0.1
    return 0


def ejercicio1a():
    '''U = random()
    if U<=0.05:
        return 0
    elif U<=0.15:
        return 1
    elif U<=0.35:
        return 2
    elif U<=0.65:
        return 3
    return 4'''
    while 1:
        U = random()
        Y = randint(0, 4)
        c = 1.75
        if U < p(Y) / (c * q(Y)):
            return Y

def ejercicio1b(N):
    e = 0
    for _ in range(N):
        e += ejercicio1a() / N
    return e

print(ejercicio1b(10000))
