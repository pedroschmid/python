# functions
def mainMenu():

    msg = 'WELCOME TO PYNU!'
    print('=-' * 30)

    print(f'\033[1;33m{msg.center(55)}\033[m')

    print('=-' * 30)

def chooseMenu():
    print('=-' * 30)

    print(f'\033[1;33m[1] To add a person\033[m')
    print(f'\033[1;33m[2] To list all person\033[m')
    print(f'\033[1;33m[3] Show menu again\033[m')
    print(f'\033[1;33m[0] To exit the programm\033[m')

    print('=-' * 30 + '\n')

def openFile():
    try:
        file = open('D:\\Development\\Python\\Curso Em Video\\Exercicios\\TestFiles\\Data.txt', 'r')
    except IOError:
        file = open('D:\\Development\\Python\\Curso Em Video\\Exercicios\\TestFiles\\Data.txt', 'w')
        print(f'\033[1;31mERROR! File does not appear to exist, will be created one with the same name!.\033[m')
    else:
        print('\033[1;32mFile successfully opened!\033[m')
    finally:
        file.close()
        print('\033[1;32mClosing the file!\033[m\n')

def addPerson():
    with open('D:\\Development\\Python\\Curso Em Video\\Exercicios\\TestFiles\\Data.txt', 'wb') as file:
        while True:
            try:
                name = str(input('Type your name: '))
                age = int(input('Type your age: '))

                file.write(name.encode('utf-8', 'ignore') + b'\n')
                file.write(str(age).encode('utf-8', 'ignore') + b'\n')
            except KeyboardInterrupt:
                print(
                    f'\033[1;31mERROR! the user did not type anything, please type something!\033[0;31m')
                continue
            else:
                print('\033[1;32mSuccessfully registered person!\033[m')

            answer = str(input('Want to add another person? [Y/N] ')).strip().upper()[0]
            if answer == 'N':
                break 
            else:
                continue

def listPerson():
    with open('D:\\Development\\Python\\Curso Em Video\\Exercicios\\TestFiles\\Data.txt', 'rb') as file:
        for i in file:
            print(f'%s' % i)

# calling functions
openFile()
mainMenu()
chooseMenu()

while True:
    choose = int(input('What is your choice? '))

    if choose == 1:
        addPerson()
    elif choose == 2:
        listPerson()
    elif choose == 3:
        chooseMenu()   
    else:
        print(f'\033[1;35mThanks for using the program!\033[m') 
        print(f'\033[1;31mExiting...\033[m')
        break  