name = str(input('Type your name: '))

upperName = name.upper()
lowerName = name.lower()
length = len(name)
firstName = name.split()

print(f'Uppercase: {upperName}')
print(f'Lowercase: {lowerName}')
print(f'Length: {length}')
print(f'First Name: {firstName[0]}')