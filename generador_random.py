def von_neumann(u):
    return (u**2 // 100) % 10000


def von_neumann_gen(seed, iterations):
    u = seed
    for _ in range(iterations):
        u = von_neumann(u)
    return u
