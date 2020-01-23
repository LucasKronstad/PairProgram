import math
def christmas(x):
   y = 0.17*x**3 + 0.43*x**2 + 0.51*x
   return math.ceil(y)

print(christmas(12))