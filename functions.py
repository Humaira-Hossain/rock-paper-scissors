import random
from headers import *

options = ['rock', 'paper', 'scissors']


def choose_mode():
    while True:
        mode = input('Which mode would you like to play?'
                     '\n[1] Best of 3'
                     '\n[2] Indefinite Mode'
                     '\n[3] Custom Number of Rounds'
                     '\n[4] Quit\n')
        if mode == '4':
            print('Goodbye!')
            exit()

        elif mode in ['1', '2', '3']:
            return mode
        else:
            print('Please enter 1, 2, or 3. Or enter 4 to quit')


def user_choice():
    while True:
        user_input = input('Which do you choose: ROCK / PAPER / SCISSORS or Q to quit: ').strip().lower()
        if user_input in ['q', 'quit']:
            print('Goodbye!')
            exit()
        elif user_input not in options:
            print('Please enter a valid option')
            continue
        else:
            break

    return user_input


def cpu_choice():
    random_number = random.randint(0, 2)
    cpu = options[random_number]
    return cpu


def user_wins(user, cpu):
    if user == 'rock' and cpu == 'scissors':
        return True
    elif user == 'paper' and cpu == 'rock':
        return True
    elif user == 'scissors' and cpu == 'paper':
        return True
    else:
        return False


def wants_to_play_again():
    while True:
        again = input('Play again? y/n: ').lower().strip()
        if again == 'y':
            return True
        elif again == 'n' or 'q':
            return False
        else:
            print('Please enter either y or n')


def is_odd(num):
    if num % 2 == 1:
        return True
    else:
        return False



