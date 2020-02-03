import math
def quadratic_equation(a, b, c):

    x = ((b/a) /-2) + math.sqrt((b/2)**2 - (c/a))
    return x

print(quadratic_equation( 1, -12, -28))
