import random

random.seed(3)

# call the function here
distribution = random.betavariate(alpha=0.9, beta=0.1)
print(distribution)
