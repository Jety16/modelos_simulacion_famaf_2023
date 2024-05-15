import numpy as np
import random

def generate_variable():
    # Step 1: Generate Y from exponential distribution
    Y = -np.log(random.random())

    # Step 2: Generate a uniform random variable U2
    U2 = random.random()

    # Step 3: Calculate X
    X = U2 ** (1/Y)

    return X

# Generate 10,000 samples of X
samples = [generate_variable() for _ in range(10000)]

# Calculate the mean of the samples
mean = np.mean(samples)
print("Mean of the generated variable X:", mean)

