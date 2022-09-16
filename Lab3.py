#Where the look begins so youl be able to restart as long as you type in y.
again = "-"
while again != 'n':
#The greeting of the program
    print('\nWelcome to the FLarsheim Guesser!\n')
#lets user think of the number he wants
    print('Please think of a number between and including 1 amd 100.\n')
#user gives the input of the first remainder of the number they are thinking
    rem_3 = int(input('What is the remainder when your number is divided by 3 ?'))
    rem3 = rem_3 % 3
#lets the user know if the input they used is acceptable and will repeat until it is
    while True:
        if rem_3 <= 0:
            print('The value entered must be 0 or greater')
            rem_3 = int(input('What is the remainder when your number is divided by 3 ?'))
        elif rem_3 > 2:
            print('The value you entered must be less than 3')
            rem_3 = int(input('What is the remainder when your number is divided by 3 ?'))       
        else:
            break
#user gives the input of the second remainder of the number they are thinking
    rem_5 = int(input('\nWhat is the remainder when your number is divided by 5 ?'))
    rem5 = rem_5 % 5
#lets the user know if the input they used is acceptable and will repeat until it is
    while True:
        if rem_5 <= 0:
            print('The value entered must be 0 or greater')
            rem_5 = int(input('What is the remainder when your number is divided by 5 ?'))
        elif rem_5 > 4:
            print('The value you entered must be less than 5')
            rem_5 = int(input('What is the remainder when your number is divided by 5 ?'))
#Allows program to end when the inputs are valid
        else:
            break
#user gives the input of the second remainder of the number they are thinking
    rem_7 = int(input('\nWhat is the remainder when your number is divided by 7 ?'))
    rem7 = rem_7 % 7
#lets the user know if the input they used is acceptable and will repeat until it is
    while True:
        if rem_7 <= 0:
            print('The value entered must be 0 or greater')
            rem_7 = int(input('What is the remainder when your number is divided by 7 ?'))
        elif rem_7 > 6:
            print('The value you entered must be less than 7')
            rem_7 = int(input('What is the remainder when your number is divided by 7 ?'))
        else:
            break
#Allows program to end when the inputs are valid
    for rem in range(1,101):
        if rem % 3 == rem3 and rem % 5 == rem5 and rem % 7 == rem7:
            print(f'Your number was {rem}')
    print('How amazing is that?\n')    
#allows the user decide to go on or not
    again = input('Do you want to play again? Y to continue, N to quit  ==> ')


