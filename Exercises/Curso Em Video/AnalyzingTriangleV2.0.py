lineA = float(input('Type the value of the line "A": '))
lineB = float(input('Type the value of the line "B": '))
lineC = float(input('Type the value of the line "C": '))

if lineA < (lineB + lineC) and lineB < (lineA + lineC) and lineC < (lineA + lineB):

    if lineA == lineB == lineC:
        print('Its a equilateral triangle!')
    elif lineA == lineB or lineA == lineC or lineB == lineC:
        print('Its a isosceles triangle!')
    else:
        print('Its a scalene triangle')

else:
    print('It is not a triangle')