__author__ = 'Hal'
#Facts: every odd number is the a side of a Pythagorean triplet
# b side is (a**2-1)/2
#c side is b + 1

# a = 3
# answer = 0
# first_ten = 0
#while answer != 1000:
# while first_ten != 100:
#used for testing first 10 outputs and checking against handwritten table
#     a += 1
#     while answer < 1000:
#
#         b = a + 1
#         c = b + 1
#         if a**2 + b**2 == c**2:
#             answer = a + b + c
#             print("answer = %s" % str(answer))
#             print("a in loop = %s" % str(a))
#             print("b in loop = %s" % str(b))
#             print("c in loop = %s" % str(c))
#
#     a += 2
#     first_ten += 1
# print("a = %s" % str(a))
# print("b = %s" % str(b))
# print("c = %s" % str(c))

#used solution on http://www.s-anand.net/euler.html because I couldn't figure out the math
#I will explain how this works to show I understand it

for a in range(0, 1000):
#max value of a = 1000 because if a is greater than that than a + b + c would have to be > 1000
    for b in range(a,1000):
#same reasoning as above, except starting range at a since a has to be greater than b
        c = 1000 - a - b
#we use the fact that c has to be greater than both b and a and it's max number would also be 1000 (same reasoning)
        if c > 0:
#as long as c isn't negative we'll still test the case
            if c**2 == a**2 + b**2:
                print("a = %s" % str(a))
                print("b = %s" % str(b))
                print("c = %s" % str(c))
                print(a + b + c)
                print(a*b*c)
                break


