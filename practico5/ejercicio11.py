import random
import math
import numpy as np

import matplotlib.pyplot as plt
# Ejemplo de uso
def cauchy(lamda):
    while True:
        #U = random.random() *math.sqrt(1/math.pi)
        #V = (random.random() *2* math.sqrt(1/math.pi)) - math.sqrt(1/math.pi)
        U = random.random()
        V = random.random() *lamda*2 -lamda
        if U**2 + (lamda*V)**2 < 1:
            return U, V
values = [cauchy(3) for _ in range(10000)]
U_values, V_values = zip(*values)

# Crear puntos en el semicírculo para graficar
theta = np.linspace(0, np.pi, 100)
#U_circle = np.cos(theta) * np.sqrt(1/np.pi)
#V_circle = np.sin(theta) * np.sqrt(1/np.pi)
plt.figure(figsize=(10, 10))
plt.scatter(U_values, V_values, s=5, alpha=0.5, label='Puntos generados')
#plt.plot(U_circle, V_circle, color='red', label='Semicírculo derecho')
plt.title('Semicírculo derecho y Puntos Generados')
plt.xlabel('U')
plt.ylabel('V')
#plt.xlim(0,1) # eje x al semicírculo derecho
#plt.ylim(-1, 1) #  # Limitar el eje y al semicírculo
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.grid(True)
plt.show()

def gen_X(n):
    ret = []
    for _ in range(n):
        X, Y = cauchy(1)
        ret.append(Y/X)
    return ret

print(sum(gen_X(10000)) /10000)
