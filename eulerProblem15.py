__author__ = 'haldegroat'
import math
def latticePathSteps(x, y):
    numerator = x * 2
    print(numerator)
    for i in range(1, x):
        numerator = numerator * ((x*2)-i)
        print(numerator)
    print(math.factorial(y))
    return numerator/(math.factorial(y))

print(latticePathSteps(20, 20))


