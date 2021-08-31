while True:
    number = int(input('Type the number you want to know the multiplication table: '))

    if number < 0:
        print('You typed a negative number, ending the program...')
        break
    else:
        for i in range(1,11):
            print(f'{i} X {number} = {i*number}')
