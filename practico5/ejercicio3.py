import numpy as np
import random

def generate_mixture_random_variable(probabilities):
    # Define the exponential distributions
    random_variables = [exponential(3), exponential(5), exponential(7)]
    mixture_random_variable = 0

    for i in range(len(random_variables)):
        mixture_random_variable += probabilities[i] * random_variables[i]
    return mixture_random_variable

def exponential(lamda):
    V1 = 1-random.random()
    t = -np.log(V1) / lamda
    return t

# Define the probabilities for each distribution
probabilities = [0.5, 0.3, 0.2]

mixture_random_variable = 0
# Generate a mixture random variable
for i in range(10000):
    mixture_random_variable += generate_mixture_random_variable(probabilities)
mixture_random_variable *= 1/10000

# Calculate the mean of the mixture random variable
estimated_mean = np.mean(mixture_random_variable)

print("Estimated mean with 10,000 repetitions:", estimated_mean)
print(f"exact value: {probabilities[0]*1/3 + probabilities[1]*1/5 + probabilities[2]*1/7}")
