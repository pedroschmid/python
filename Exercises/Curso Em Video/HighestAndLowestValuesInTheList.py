list = []

for i in range(0,5):
    list.append(int(input(f'Type a number for the position [{i+1}]: ')))

print(f'Highest value of the list: {max(list)} | Lowest value of the list: {min(list)}')    