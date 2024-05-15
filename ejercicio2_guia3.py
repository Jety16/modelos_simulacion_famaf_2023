import random

def simulacion():
    U = random.random()
    if U < 0.5:
        X = random.random() + random.random()
    else:
        X = random.random() + random.random() + random.random()

    return X

experimentos = 100000
positivos = 0
for _ in range(experimentos):
    X = simulacion()
    if X >= 1:
        positivos += 1

print(positivos / experimentos)


