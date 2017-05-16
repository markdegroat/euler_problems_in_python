__author__ = 'Hal'
#https://en.wikipedia.org/wiki/Primality_test#Simple_methods provided a way to search for primes more efficiently
#then the brute force solution I created in eulerProblem7.py
import math
import time

def numIsPrime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    #only need to check if number is factor from 1 to sqrt(n)
    for i in range(2, int(math.sqrt(n)+1)): #was missing a single prime until I checked +1 past the sqrt
        #the int() function must round down and you have to round up from the sqrt(n) to correctly approximate
        if n%i == 0:
            return False
    #if it passes these tests then the number must be prime
    return True
start_time = time.time()
answer = 0
for i in range(0, 2000000):
    if numIsPrime(i):
        answer += i
print(answer)
print("Program took %s seconds to run." % (time.time() - start_time))