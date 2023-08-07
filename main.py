from main_helper.user_actions.print_possible_actions import print_possible_actions
from main_helper.user_actions.scan_for_patterns import scan_for_patterns
from main_helper.user_options import UserOptions

import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    user_options = UserOptions()
    user_options.initialise_options() # get user input

    clear_terminal()

    while True:
        action = input("please select an action (type \"actions\" for all possible actions): ")

        clear_terminal()

        if action == "actions":
            print_possible_actions()
        elif action == "scan":
            scan_for_patterns(user_options)
        elif action == "options":
            user_options.initialise_options() # TODO change to reinitialise when implemented
            clear_terminal()
        elif action == "quit" or action == "q":
            break
        else:
            print("Action not recognised, type \"actions\" for all possible actions")

if __name__ == '__main__':
    main()