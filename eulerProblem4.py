__author__ = 'Hal'
def isAPalindrome(number):
    numAsString = str(number)
    stringAsList = []
    for digit in numAsString: #breaks number into a list
        stringAsList.append(int(digit))
    #start = stringAsList[0]
    #end = stringAsList[-1] #-1 loops back around to give you the last element... super convenient
    start = 0
    #print(len(stringAsList))
    end = len(stringAsList) - 1
    palindromeFound = False
    for i in range(0, int(len(stringAsList)/2)): #seems to be working
        if stringAsList[start] == stringAsList[end]:
            palindromeFound = True
            #print('test')
            i += 1
            start += 1
            end -= 1
        else:
            palindromeFound = False
            #print('test2')
    return palindromeFound






#print(isAPalindrome(123321)) #used for testing
largestPalindrome = 0
for i in range(0, 1000):
    for j in range(0, 1000):
        if isAPalindrome(i*j) and i*j > largestPalindrome:
            largestPalindrome = i * j
            print(largestPalindrome)
            largest_i = i
            largest_j = j


print(largestPalindrome)
print('largest i:' + str(largest_i))
print('largest j:' + str(largest_j))




