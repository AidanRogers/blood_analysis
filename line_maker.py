coordinates = [(1, 1), (5, 9)]


def line_maker(coordinates):
    print("making a line")
    x1 = coordinates[0][0]
    y1 = coordinates[0][1]
    x2 = coordinates[1][0]
    y2 = coordinates[1][1]
    x3 = input("what is a new x value:  ")
    # coord1 = (x1,y1)
    # coord2 = (x2,y2)
    # t = [0,1,2,3,4,5,6,7,8,9,10]
    rise = y2-y1
    run = x2-x1
    slope = rise/run
    x3 = float(x3)
    b = y1 - slope*(x1)
    y3 = slope*x3+b
    return y3


y = line_maker(coordinates)
print('the next value of y, on the line provided is: ', y)
