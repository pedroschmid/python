value = int(input('Type the value do you want to cash out: '))

total = value
ballot = 50
totalBallot = 0

while True:
    if total >= ballot:
        total -= ballot
        totalBallot += 1
    else:
        if totalBallot > 0:
            print(f'Total of {totalBallot} ballots of ${ballot}')
        if ballot == 50:
            ballot = 20
        elif ballot == 20:
            ballot = 10
        elif ballot == 10:
            ballot = 1

        totalBallot = 0
        
        if total == 0:
            break                    