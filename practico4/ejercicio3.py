import random
import timeit

def throw_dice():
    return random.randint(2, 12)

def simualte():
    l = [0]*11
    steps = 0
    while not all(l):
        steps += 1
        dice = throw_dice()
        l[dice-2] = 1

    return steps


total = 0
ranges = [100, 1000, 10000, 100000]
start = timeit.default_timer()

for i in ranges:
    for _ in range(i):
        total += simualte()
    stop = timeit.default_timer()
    print(total/i, f":   {i} simulations, time: { stop - start}" )
