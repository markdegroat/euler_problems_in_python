x , y = 0 , 1
#print(x)
list_of_multiples = []
while (y < 4000000):
    z = y
    x , y = z , x + y

    if(y%2 == 0):
        list_of_multiples.append( y )
    # elif(y%5 == 0):
    #     list_of_multiples.append( y )

# for y in range(1,1000):
#     if(y%3 == 0):
#         list_of_multiples.append( y )
#     elif(y%5 == 0):
#         list_of_multiples.append( y )

print(list_of_multiples)
print(sum(list_of_multiples))


