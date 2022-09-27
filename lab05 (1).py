########################################################################
##
## CS 101 Lab
## Program #4
## Name Isaiah Walker
## Email: Idwgmh@umsystem.edu
##
## PROBLEM : none
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

import random
#accounts for chips started, turns, and highest chips per game!
bank_lis = [0]
chip_lis = [0]


#allows user to restart program using Y/YES/N/NO
def play_again() -> bool:
    while True:
        answer = str(input('Do you want to play again?'))
        if answer == 'Y' or answer == 'YES':
            return wager
        elif answer == 'N' or answer == 'NO':
            break
        else:
            print("You must enter Y/YES/N/NO to continue. Please try again")

# Allows user to bet chip amounts and lets them know if it is an acceptable number
def get_wager(bank: int) -> int:
    while True:
        wager = int(input('How many chips do you want to wager? ==> '))
        if wager <= 0:
            print('The wager amount must be greater than 0.')
        elif wager > bank:
            print(f'The wager cannot be greater than how much you have. {bank}')
#allows for the count of highest chip count
        else:
            if bank > max(chip_lis):
                chip_lis.append(bank)
            break
    return wager

#Randomizes numbers for the slots
def get_slot_results() -> tuple:
    reel1 = random.randint(1, 10)
    reel2 = random.randint(1, 10)
    reel3 = random.randint(1, 10)
    return [reel1, reel2, reel3]

#Confirms how many of the Randomized numbers are matching
def get_matches(reela, reelb, reelc) -> int:
    if reel1 == reel2 and reel1 == reel3:
        matches = 3
        return matches
    elif reel1 != reel2 and reel1 == reel3:
        matches = 2
        return matches
    elif reel1 == reel2 and reel1 != reel3:
        matches = 2
        return matches
    elif reel1 != reel2 and reel1 != reel3:
        matches = 0
        return matches

#Starts the program by asking how many chips the user wants to start with and tells them if the value you input is unacceptable
def get_bank() -> int:
    while True:
        bank = int(input('How many chips do you want to start with? ==> '))
        if bank < 1:
            print('Too low a value, you can only choose 1 - 100 chips')
        elif bank > 100:
            print('Too high a value, you can only choose 1 - 100 chips')
#Used to calculate starting amount
        else:
            if bank > max(bank_lis):
                bank_lis.append(bank)
            break
    return bank

#Calculates the payout ffor the user
def get_payout(wager, matches):
    if matches == 3:
        payout = wager * 10
        return payout
    elif matches == 2:
        payout = wager * 3
        return payout
    elif matches == 0:
        payout = wager * -1
        return payout


if __name__ == "__main__":

    playing = True
    while playing:
        spins = 0
        bank = get_bank()

        while bank != 0:  

            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()

            spins += 1

        print("You lost all", max(bank_lis), "in", spins, "spins")
        print("The most chips you had was", max(chip_lis))
        playing = play_again()


