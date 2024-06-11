import numpy as np
from scipy.integrate import quad

def f(x):
    return np.exp(-x ** 2)

result, error = quad(f, -np.inf, np.inf)

print(f"Result: {result}")
print(f"Error: {error}")