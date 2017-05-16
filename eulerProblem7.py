__author__ = 'Hal'
import time
def isPrime(n):
    factor_list = []
    for i in range(2, n+1):
        if n%i == 0:
            factor_list.append(i)
    if len(factor_list) == 1: #this means only n is in the list because we're not checking 1
        return True
    else:
        return False
i = 0
prime_numbers = 0
start_time = time.time()
while prime_numbers < 10001:
    if isPrime(i):
        prime_numbers += 1

    i += 1
print(i - 1)
print("----%s seconds----" % (time.time()-start_time))
