higher = 0
lower = 10_000_000

for i in range(0,6):
    weight = float(input(f'Type the weight {i+1}: '))

    if weight > higher:
        higher = weight

    if weight < lower:
        lower = weight

print(f'Higher: {higher} | Lower: {lower}')        