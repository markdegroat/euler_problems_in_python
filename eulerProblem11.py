__author__ = 'Hal'
Matrix = {} #using dict as matrix
consecutive_numbers = 4
with open("number_array.txt") as file:
    first_line = file.readline()
    file.seek(0)
    y_count = sum(1 for line in file)
    x_count = first_line.count(' ') + 1
    file.seek(0)
    list_of_lists = []
    for i in range(0, y_count):
        list_of_lists.append(file.readline().split()) #now the file has been converted to a list of lists matrix

for x in range(0, x_count):
    for y in range(0, y_count):
        list_of_lists[y][x] = int(list_of_lists[y][x])

product = 1
max_product = 1
max_x = 0
max_y = 0
direction = 'empty'
print(y_count)
print(first_line)
print(x_count)
print(list_of_lists)
print(list_of_lists[2][2])
print(list_of_lists[0][2])
print(list_of_lists[2][0])
#this method of making 2d array makes the form list_of_lists[y][x]
for x in range(x_count):
    for y in range(y_count):
        if x < 3 and y < 3:  # top left corner case, need E,S,SE
            product = 1
            for i in range(0, consecutive_numbers):
                product = product * list_of_lists[y][x+i]
            if product > max_product:
                max_product = product
                max_x = x
                max_y = y
                direction = 'E'
            product = 1
            for i in range(0, consecutive_numbers):
                product = product * list_of_lists[y+i][x]
            product = 1
            if product > max_product:
                max_product = product
                max_x = x
                max_y = y
                direction = 'S'
            product = 1
            for i in range(0, consecutive_numbers):
                product = product * list_of_lists[y+i][x+i]
            if product > max_product:
                max_product = product
                max_x = x
                max_y = y
                direction = 'SE'
            product = 1
        elif x < 3 and y > 2 and y < 17:  # left side case, need N,S,E,NE,SE
            for i in range(0, consecutive_numbers):
                product = product * list_of_lists[y-i][x]
            if product > max_product:
                max_product = product
                max_x = x
                max_y = y
                direction = 'N'
            product = 1
            for i in range(0, consecutive_numbers):
                product = product * list_of_lists[y+i][x]
            if product > max_product:
                max_product = product
                max_x = x
                max_y = y
                direction = 'S'
            product = 1
            for i in range(0, consecutive_numbers):
                product = product * list_of_lists[y][x+i]
            if product > max_product:
                max_product = product
                max_x = x
                max_y = y
                direction = 'E'
            product = 1
            for i in range(0, consecutive_numbers):
                product = product * list_of_lists[y-i][x+i]
            if product > max_product:
                max_product = product
                max_x = x
                max_y = y
                direction = 'NE'
            product = 1
            for i in range(0, consecutive_numbers):
                product = product * list_of_lists[y+i][x+i]
            if product > max_product:
                max_product = product
                max_x = x
                max_y = y
                direction = 'SE'
            product = 1
        elif x < 3 and y > 16:  # bottom left corner case, look N,NE,E
            for i in range(0, consecutive_numbers):
                product = product * list_of_lists[y-i][x]
            if product > max_product:
                max_product = product
                max_x = x
                max_y = y
                direction = 'N'
            product = 1
            for i in range(0, consecutive_numbers):
                product = product * list_of_lists[y-i][x+i]
            if product > max_product:
                max_product = product
                max_x = x
                max_y = y
                direction = 'NE'
            product = 1
            for i in range(0, consecutive_numbers):
                product = product * list_of_lists[y][x+i]
            if product > max_product:
                max_product = product
                max_x = x
                max_y = y
                direction = 'E'
            product = 1
        elif x > 2 and x < 17 and y > 16: #bottom edge case, look W,NW,N,NE,E
            for i in range(0, consecutive_numbers):
                product = product * list_of_lists[y][x-i]
            if product > max_product:
                max_product = product
                max_x = x
                max_y = y
                direction = 'W'
            product = 1
            for i in range(0, consecutive_numbers):
                product = product * list_of_lists[y-i][x-i]
            if product > max_product:
                max_product = product
                max_x = x
                max_y = y
                direction = 'NW'
            product = 1
            for i in range(0, consecutive_numbers):
                product = product * list_of_lists[y-i][x]
            if product > max_product:
                max_product = product
                max_x = x
                max_y = y
                direction = 'N'
            product = 1
            for i in range(0, consecutive_numbers):
                product = product * list_of_lists[y-i][x+i]
            if product > max_product:
                max_product = product
                max_x = x
                max_y = y
                direction = 'NE'
            product = 1
            for i in range(0, consecutive_numbers):
                product = product * list_of_lists[y][x+i]
            if product > max_product:
                max_product = product
                max_x = x
                max_y = y
                direction = 'E'
            product = 1
        elif x > 16 and y > 16:  # bottom right corner case, look W,NW,N
            for i in range(0, consecutive_numbers):
                product = product * list_of_lists[y][x-i]
            if product > max_product:
                max_product = product
                max_x = x
                max_y = y
                direction = 'W'
            product = 1
            for i in range(0, consecutive_numbers):
                product = product * list_of_lists[y-i][x-i]
            if product > max_product:
                max_product = product
                max_x = x
                max_y = y
                direction = 'NW'
            product = 1
            for i in range(0, consecutive_numbers):
                product = product * list_of_lists[y-i][x]
            if product > max_product:
                max_product = product
                max_x = x
                max_y = y
                direction = 'N'
            product = 1
        elif x > 16 and y > 2 and y < 17:  # right side case, look N,NW,W,SW,S
            for i in range(0, consecutive_numbers):
                product = product * list_of_lists[y-i][x]
            if product > max_product:
                max_product = product
                max_x = x
                max_y = y
                direction = 'N'
            product = 1
            for i in range(0, consecutive_numbers):
                product = product * list_of_lists[y-i][x-i]
            if product > max_product:
                max_product = product
                max_x = x
                max_y = y
                direction = 'NW'
            product = 1
            for i in range(0, consecutive_numbers):
                product = product * list_of_lists[y][x-i]
            if product > max_product:
                max_product = product
                max_x = x
                max_y = y
                direction = 'W'
            product = 1
            for i in range(0, consecutive_numbers):
                product = product * list_of_lists[y+i][x-i]
            if product > max_product:
                max_product = product
                max_x = x
                max_y = y
                direction = 'SW'
            product = 1
            for i in range(0, consecutive_numbers):
                product = product * list_of_lists[y+i][x]
            if product > max_product:
                max_product = product
                max_x = x
                max_y = y
                direction = 'S'
            product = 1
        elif x > 16 and y < 3:  # top right corner case, look W,SW,S
            for i in range(0, consecutive_numbers):
                product = product * list_of_lists[y][x-i]
            if product > max_product:
                max_product = product
                max_x = x
                max_y = y
                direction = 'W'
            product = 1
            for i in range(0, consecutive_numbers):
                product = product * list_of_lists[y+i][x-i]
            if product > max_product:
                max_product = product
                max_x = x
                max_y = y
                direction = 'SW'
            product = 1
            for i in range(0, consecutive_numbers):
                product = product * list_of_lists[y+i][x]
            if product > max_product:
                max_product = product
                max_x = x
                max_y = y
                direction = 'S'
            product = 1
        elif x > 2 and x < 17 and y < 3:  # top edge case, look W,SW,S,SE,E
            for i in range(0, consecutive_numbers):
                product = product * list_of_lists[y][x-i]
            if product > max_product:
                max_product = product
                max_x = x
                max_y = y
                direction = 'W'
            product = 1
            for i in range(0, consecutive_numbers):
                product = product * list_of_lists[y+i][x-i]
            if product > max_product:
                max_product = product
                max_x = x
                max_y = y
                direction = 'SW'
            product = 1
            for i in range(0, consecutive_numbers):
                product = product * list_of_lists[y+i][x]
            if product > max_product:
                max_product = product
                max_x = x
                max_y = y
                direction = 'S'
            product = 1
            for i in range(0, consecutive_numbers):
                product = product * list_of_lists[y+i][x+i]
            if product > max_product:
                max_product = product
                max_x = x
                max_y = y
                direction = 'SE'
            product = 1
            for i in range(0, consecutive_numbers):
                product = product * list_of_lists[y][x+i]
            if product > max_product:
                max_product = product
                max_x = x
                max_y = y
                direction = 'E'
            product = 1
        else:  # case where were not on an edge or corner, look N,S,E,W,NE,NW,SE,SW
            for i in range(0, consecutive_numbers):
                product = product * list_of_lists[y-i][x]
            if product > max_product:
                max_product = product
                max_x = x
                max_y = y
                direction = 'N'
            product = 1
            for i in range(0, consecutive_numbers):
                product = product * list_of_lists[y+i][x]
            if product > max_product:
                max_product = product
                max_x = x
                max_y = y
                direction = 'S'
            product = 1
            for i in range(0, consecutive_numbers):
                product = product * list_of_lists[y][x+i]
            if product > max_product:
                max_product = product
                max_x = x
                max_y = y
                direction = 'E'
            product = 1
            for i in range(0, consecutive_numbers):
                product = product * list_of_lists[y][x-i]
            if product > max_product:
                max_product = product
                max_x = x
                max_y = y
                direction = 'W'
            product = 1
            for i in range(0, consecutive_numbers):
                product = product * list_of_lists[y-i][x+i]
            if product > max_product:
                max_product = product
                max_x = x
                max_y = y
                direction = 'NE'
            product = 1
            for i in range(0, consecutive_numbers):
                product = product * list_of_lists[y-i][x-i]
            if product > max_product:
                max_product = product
                max_x = x
                max_y = y
                direction = 'NW'
            product = 1
            for i in range(0, consecutive_numbers):
                product = product * list_of_lists[y+i][x+i]
            if product > max_product:
                max_product = product
                max_x = x
                max_y = y
                direction = 'SE'
            product = 1
            for i in range(0, consecutive_numbers):
                product = product * list_of_lists[y+i][x-i]
            if product > max_product:
                max_product = product
                max_x = x
                max_y = y
                direction = 'SW'
            product = 1
print("Max product is: %s" % max_product)
print("Product is located at x coordinate: %s" % max_x)
print("Product is located at y coordinate: %s" % max_y)
print("Product is going the direction: %s" % direction)
