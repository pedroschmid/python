number = int(input('Type a number: '))

unity = (number // 1) % 10
dozen = (number // 10) % 10
hundred = (number // 100) % 10
thousand = (number // 1000) % 10

print(f'Analyzing number {number}')
print(f'Unity: {unity}')
print(f'Dozen:: {dozen}')
print(f'Hundred: {hundred}')
print(f'Thousand: {thousand}')
