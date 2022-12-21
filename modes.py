from functions import *
from headers import *


def indefinite_mode():
    indefinite_mode_title()
    user_score = 0
    cpu_score = 0
    while True:
        user = user_choice()
        cpu = cpu_choice()

        line_break()
        print(f'You chose {user.upper()}')
        print(f'Computer chose {cpu.upper()}')

        if user == cpu:
            print("It's a tie!")
        elif user_wins(user, cpu):
            print('You won!')
            user_score += 1
        else:
            print('Computer won!')
            cpu_score += 1
        line_break()

        if not wants_to_play_again():
            break

    line_break()
    print(f'Your score: {user_score}')
    print(f'Computer score: {cpu_score}')
    line_break()


def best_of(num):
    user_score = 0
    cpu_score = 0
    round_number = 1
    while round_number < num + 1:
        round_title(round_number)
        user = user_choice()
        cpu = cpu_choice()

        line_break()
        print(f'You chose {user.upper()}')
        print(f'Computer chose {cpu.upper()}')

        if user == cpu:
            print("It's a tie! Let's redo this round")
            continue
        elif user_wins(user, cpu):
            print(f'You won round {round_number}!')
            user_score += 1
            round_number += 1
        else:
            print(f'Computer won round {round_number}!')
            cpu_score += 1
            round_number += 1

    line_break()
    print(f'Your score: {user_score}')
    print(f'Computer score: {cpu_score}')

    if user_score > cpu_score:
        print('Congratulations! You won!!')
    else:
        print('You lost!')
    line_break()


def custom_rounds():
    while True:
        no_of_rounds = input('Please enter an odd number for the number of rounds you want to play.'
                             '\nOr enter Q to quit.\n')
        if no_of_rounds.lower().strip() in ['q', 'quit']:
            print('Goodbye!')
            exit()
        elif no_of_rounds.isalpha():
            print('Please enter an odd number')
        elif no_of_rounds.strip().isdigit():
            if is_odd(int(no_of_rounds)):
                break

    return int(no_of_rounds)
