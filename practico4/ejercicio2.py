import random
import math
def approx_exp_sum(N):
    total = 0
    for k in range(1, N + 1):
        total += math.exp(k / N)
    return total

def random_approx_exp_sum(N, num_samples):
    total = 0
    for _ in range(num_samples):
        k = random.randint(1, N)
        total += math.exp(k / N)
    return total

def exact_exp_sum(N):
    total = sum(math.exp(k / N) for k in range(1, N+1))
    return total


N = 100
num_samples = N
exact_value = exact_exp_sum(N)
random_approximation = random_approx_exp_sum(N, num_samples)
sequential_approximation = approx_exp_sum(N)

print("Exact value:", exact_value)
print("Random approximation:", random_approximation)
print("Sequential approximation:", sequential_approximation)

