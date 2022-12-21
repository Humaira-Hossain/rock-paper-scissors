from modes import *


def main():
    main_title()
    while True:
        mode = choose_mode()
        if mode == '1':
            best_of(3)
        elif mode == '2':
            indefinite_mode()
        elif mode == '3':
            user_number = custom_rounds()
            best_of(user_number)


if __name__ == "__main__":
    main()
