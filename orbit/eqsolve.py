import numpy as np
from scipy.optimize import fsolve

# Example: Solve x^2 - 2 = 0
def equation(x):
    return x**2 - 2

solution = fsolve(equation, x0=1.0)  # initial guess
print(solution)  # ~1.41421356 (sqrt(2))
