import math
import time

number = 600851475143
start_time = time.time()


#brute force, would take like 1000 years to finish lol
# for i in range(2,number + 1):
#     list_prime_test=[]
#     for y in range(2,i + 1): # do this because range does startnum through endnum - 1
#         if i%y == 0:
#             list_prime_test.append(y)
#         if len(list_prime_test) == 1 and list_prime_test[0] != 2 and number % list_prime_test[0]== 0:
#              list_of_prime_factors.append(list_prime_test[0])
# print(max(list_of_prime_factors))

#utilizing  Any factor less than the square root of the number we check,
# will have corresponding factor larger than the square root of the number.
# So we only need to check up to the square root of the number,
# and then we can deduct the remaining factors.

#ALSO TAKES FOREVER LISTS ARE SLOW
# list_of_prime_factors = []
# for i in range(2,number + 1):
#     list_of_factors=[] #TODO : change this to list_of_factors
#     for y in range(2,int(math.sqrt(i + 1))): # only need to check the factors between 2 and sqrt(number in range of i)
#         if i%y == 0:
#             list_of_factors.append(y)
#         if len(list_of_factors) == 1 and list_of_factors[0] != 2 and number % list_of_factors[0]== 0:
#              list_of_prime_factors.append(list_of_factors[0])
#print(max(list_of_prime_factors))

#FIGURE OUT WHY THIS IS SO MUCH FASTER, POST TO STACK OVERFLOW taken from: http://www.s-anand.net/euler.html
i = 2
while i * i < number:
    while number % i == 0:
        number = number / i
    i = i + 1
print(number)
print("--- %s seconds ---" % (time.time() - start_time))