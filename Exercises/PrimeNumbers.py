number = int(input('Type a number: '))
divider = 0

for i in range(1, number+1):
    if number % i == 0:
        divider += 1

if divider == 2:
    print(f'{number} is prime!')
else:
    print(f'{number} is not prime!')           
