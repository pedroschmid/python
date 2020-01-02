tupla = ('Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten')

while True:
    number = int(input('Type a number (Between 0-10): '))

    if 0 < number <= 10:
        break
    number = int(input('You typed an invalid number, try again: '))

print(f'You typed the number {tupla[number]}')