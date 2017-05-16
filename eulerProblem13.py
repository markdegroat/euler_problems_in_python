__author__ = 'haldegroat'
import time
start_time = time.time()
with open("problem_13_number_string.txt") as file:
    number_list = []
    for line in file:
        number_list.append(line)
for i in range(0, len(number_list)):
    number_list[i] = int(number_list[i])
#print(number_list)
#print(sum(number_list))
sum_of_all_numbers = sum(number_list)
digits_as_list = list(map(int, str(sum_of_all_numbers)))
first_ten_digits = []
for i in range(0, 10):
    first_ten_digits.append(digits_as_list[i])
print(first_ten_digits)

print("----Program took %s seconds to run.----" % (time.time()-start_time))

