__author__ = 'Hal'
def sumOfSquares(n):
    sum = 0
    for i in range(0, n+1):
        sum += i**2
    return sum
def squareOfSums(n):
    sum = 0
    for i in range(0, n+1):
        sum += i
    return sum**2
print(sumOfSquares(10))
print(squareOfSums(10))
print(squareOfSums(100)-sumOfSquares(100))