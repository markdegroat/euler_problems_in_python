__author__ = 'haldegroat'
import time
def collatzSequence(x):
    list_to_return = []
    n = x
    list_to_return.append(x)
    while n != 1:
        if n % 2 == 0:  # n is even
            n /= 2
            list_to_return.append(n)
        else:         # n is odd
            n = (3*n) + 1
            list_to_return.append(n)
    return list_to_return

start_time = time.time()
largest_starting_number = 1
i = 1
longest_chain = []
while i < 1000000:
    test_chain = collatzSequence(i)
    if len(test_chain) > len(longest_chain):
        longest_chain = test_chain
        largest_starting_number = i
    i += 1

print("Longest Chain found was %s" % longest_chain)
print("Starting number under 1,000,000 with longest chain is %s" % largest_starting_number)
print("---Program took %s seconds to run.---" % (time.time()-start_time))
"""
    NEEDS HEAVY OPTIMIZATION, FINISHES IN JUST UNDER 1 MINUTE
"""