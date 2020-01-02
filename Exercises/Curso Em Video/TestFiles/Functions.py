def mainMenu():

    msg = 'WELCOME TO PYNU!'
    print('=-' * 30)
    print(f'{msg.center(55)}')
    print('=-' * 30)

def chooseMenu():
    print('=-' * 30)
    print('[1] To add a person')
    print('[2] To list all person')
    print('[0] To exit the programm')
    print('=-' * 30)

def createFile(file):
    file = open('D:\\Development\\Python\\Curso Em Video\\Exercicios\\TestFiles\\Data.txt', 'w')
    file.close()

def openFile(file):
    try:
        file = open('D:\\Development\\Python\\Curso Em Video\\Exercicios\\TestFiles\\Data.txt', 'r')
        return 1
    except IOError:
        print(f'\033[0;31mERROR! File does not appear to exist.\033[m')    
        return 0
    else:
        print('File successfully opened.') 
        file.close()    

def addPerson(choose):
    while True:
        try:
            file.write('Type your name: ')
            file.write('Type your age: ')
        except KeyboardInterrupt:
            print(f'\033[0;31mERROR! the user did not type anything, please type something!\033[0;31m')
            continue
        else:
            print('Successfully registered person!')

        answer = str(input('Want to add another person? [Y/N] ')).strip().upper()[0]
        if answer == 'N':
            break
        else:
            continue
        
def listPerson(choose):
    file.read()