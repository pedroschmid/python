lineA = float(input('Type the value of the line "A": '))
lineB = float(input('Type the value of the line "B": '))
lineC = float(input('Type the value of the line "C": '))

if lineA < (lineB + lineC) and lineB < (lineC + lineA) and lineC < (lineA + lineB):
    print('It is a triangle!')
else:
    print('It is not a triangle!')