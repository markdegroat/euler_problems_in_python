__author__ = 'Hal'
import time
#purpose of script is to find the thirteen adjacent numbers
#in a list that generate the largest product and what that product is
#adjust 'adjacent_numbers' variable to change how many numbers
#in a row you're looking for

start_time = time.time()
#opening file to read numbers
with open("number_string.txt") as file:
    number_string = file.read()



#stripping \n from number_string
number_string = number_string.replace('\n', '')


l = list(number_string)


startIndexOfLargestProduct = 0
product = 1
maxProduct = 1
answerList = []
adjacent_numbers = 13

#checking up to the end of list - the number of adjacent numbers
#we're looking for to not go out of range
for i in range(0, len(l)-adjacent_numbers):
    product = 1
    for j in range(0, adjacent_numbers):
        product = product * int(l[i+j])
    if product > maxProduct:
        maxProduct = product
        startIndexOfLargestProduct = i

#print(startIndexOfLargestProduct)
print(maxProduct)
for k in range(0, adjacent_numbers):
    answerList.append(l[startIndexOfLargestProduct+k])
print(answerList)
print("Program took %s seconds to run." % (time.time() - start_time))


