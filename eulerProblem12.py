__author__ = 'haldegroat'
import time

# I took this tau function from: http://stackoverflow.com/questions/9076336/how-do-you-implement-the-divisor-function-in-code
# it is a heavily optimized method for finding factors of a number
def tau(n):
        sqroot,t = int(n**0.5),0
        for factor in range(1,sqroot+1):
                if n % factor == 0:
                        t += 2 # both factor and N/factor
        if sqroot*sqroot == n: t = t - 1 # if sqroot is a factor then we counted it twice, so subtract 1
        return t

# My take on the tau-like implementation of finding factors in Python, accomplishes solution ~2 seconds faster
def findFactors(x):
    factor_list = []
    for i in range(1, int((x+1)/2)+1): # this opt doubles speed of findFactor function
    #for i in range(1, x+1):
        if x % i == 0:
            factor_list.append(i)
    factor_list.append(x)
    return factor_list

def triangularNumber(x):
    answer = 0
    for i in range(1, x+1):
        answer = answer + i
    return answer

def triangularNumberOpt(x):
    n = x * (x+1) / 2
    return int(n)




print(triangularNumber(7))
print(triangularNumberOpt(7))
print(triangularNumber(8))
print(triangularNumberOpt(8))
print(triangularNumber(9))
print(triangularNumberOpt(9))

print(findFactors(130))
start_time = time.time()
print(len(findFactors(76576500)))
print("len(findFactors(x) took %s seconds to run." % (time.time()-start_time))
start_time = time.time()
print(tau(76576500))
print("tau(x) took %s seconds to run." % (time.time()-start_time))
# as x grows, tau(x) is much, much faster

answer_found = False
i = 1
num_of_divisors = 500
start_time = time.time()

#implementation using Tau(x), is much faster than the brute force
while answer_found == False:
    if tau(triangularNumberOpt(i)) > num_of_divisors:
        answer_found = True
        print('\nNumber with more than 500 factors is: %s' % triangularNumberOpt(i))
        #print('It\'s factors are: %s' % findFactors(triangularNumberOpt(i)))
    else:
        i += 1


print("Tau based program took %s seconds to run." % (time.time()-start_time))

start_time = time.time()
answer_found = False # reset answer_found
i = 1 #reset i count
while answer_found == False:
    if len(findFactors(triangularNumberOpt(i))) > num_of_divisors:
        answer_found = True
        print('\nNumber with more than 500 factors is: %s' % triangularNumberOpt(i))
        #print('It\'s factors are: %s' % findFactors(triangularNumberOpt(i)))
    else:
        i += 1


print("Brute force based program I wrote took %s seconds to run." % (time.time()-start_time))
#  optimization ideas: only check up to half the input number in find factor method