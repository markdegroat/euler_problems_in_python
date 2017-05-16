__author__ = 'haldegroat'
def digitsToList(x):
    digits_as_list = list(map(int, str(x)))
    return digits_as_list
def ones_place_to_str(x, actual_num):
    if actual_num == 0:
        return "zero"
    elif x == 0:
        return ""
    elif x == 1:
        return "one"
    elif x == 2:
        return "two"
    elif x == 3:
        return "three"
    elif x == 4:
        return "four"
    elif x == 5:
        return "five"
    elif x == 6:
        return "six"
    elif x == 7:
        return "seven"
    elif x == 8:
        return "eight"
    elif x == 9:
        return "nine"

def tens_place_to_str(x, y):
    if x == 0:
        return ""
    if x == 1:
        if y == 0:
            return "ten"
        if y == 1:
            return "eleven"
        if y == 2:
            return "twelve"
        if y == 3:
            return "thirteen"
        if y == 4:
            return "fourteen"
        if y == 5:
            return "fifteen"
        if y == 6:
            return "sixteen"
        if y == 7:
            return "seventeen"
        if y == 8:
            return "eighteen"
        if y == 9:
            return "nineteen"
        return "one"
    if x == 2:
        return "twenty"
    if x == 3:
        return "thirty"
    if x == 4:
        return "forty"
    if x == 5:
        return "fifty"
    if x == 6:
        return "sixty"
    if x == 7:
        return "seventy"
    if x == 8:
        return "eighty"
    if x == 9:
        return "ninety"

def hundreds_place_to_str(x):
    if x == 0:
        return ""
    if x == 1:
        return "one hundred"
    if x == 2:
        return "two hundred"
    if x == 3:
        return "three hundred"
    if x == 4:
        return "four hundred"
    if x == 5:
        return "five hundred"
    if x == 6:
        return "six hundred"
    if x == 7:
        return "seven hundred"
    if x == 8:
        return "eight hundred"
    if x == 9:
        return "nine hundred"
temp_list = digitsToList(1456)
temp_list.reverse()
print(temp_list)

def numsToLetters(x):
    num_list = digitsToList(x)
    if len(num_list) == 1:
        hundreds_place_digit = 0
        tens_place_digit = 0
        ones_place_digit = num_list[0]

    elif len(num_list) == 2:
        hundreds_place_digit = 0
        tens_place_digit = num_list[0]
        ones_place_digit = num_list[1]
    elif len(num_list) == 3:
        hundreds_place_digit = num_list[0]
        tens_place_digit = num_list[1]
        ones_place_digit = num_list[2]
    else:
        return "Number can't be greater than 999"
    num_list = [0,0,0] #using zeroes as placeholders
    num_list[0] = hundreds_place_to_str(hundreds_place_digit)
    num_list[1] = tens_place_to_str(tens_place_digit, ones_place_digit)
    if x < 11 or x > 20:
        num_list[2] = ones_place_to_str(ones_place_digit, x) #need to pass actual number to test if zero, special case
    else:
        num_list[2] = ''
    if x > 100 and (ones_place_digit > 0 or tens_place_digit > 0):
        num_list.insert(1, "and")
    return num_list
for i in range(0, 1000):
    print(numsToLetters(i))
