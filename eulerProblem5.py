__author__ = 'Hal'
import time
def isDivisibleBy1ThroughN(n, testNumber):
    for i in range(2, n+2):
        if i == n+1:
            return True
        elif(testNumber%i == 0):
            i += 1
        else:
            return False


print(isDivisibleBy1ThroughN(10, 2520))#WORKS
trigger = False
x = 20
start_time = time.time()
while(trigger == False):
    if isDivisibleBy1ThroughN(20, x):
        trigger = True
        print(x)
    x += 1
print("--- %s seconds ---" % (time.time() - start_time))
#SUCCESS BUT SO SLOW NEED TO OPTIMIZE