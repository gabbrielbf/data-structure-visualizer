import os

def read_numeric_option():
    """ function responsible for returning a numeric option to avoid
    handling try-except blocks individually throughout the code """

    while True:
        try:
            return int(input('Choose one of the options above -> '))
        except ValueError:
            print('[ERROR] Invalid option\n')
            continue

def clear_terminal():
    """ clears the terminal screen to keep the interface organized """

    input('Press ENTER to continue...')
    os.system('cls' if os.name == 'nt' else 'clear')

def numbered_menu():
    """ displays the numbered menu and returns the valid selected option """

    options = [
        'Add element',
        'Remove element',
        'View next element (Peek)', # <- new option
        'View current state',
        'Switch Stack/Queue',
        'Exit'
    ]  # <- list created for dynamic menu rendering

    print('-'*30)
    for index, option in enumerate(options, start=1):
        print(f'{index} - {option}') # <- this block was made this way just to
    print('-'*30)                   # save space and not clutter the start of the function with 'prints'

    while True:
        
        option = read_numeric_option()

        if (option < 1 or 
            option > 6): # <- this block checks if the user entered something within the suggested options before returning the function value
            print('[ERROR] option not found\n')
            continue
        else:
            break

    return option

def display_stacks_or_queues():
        """ method responsible only for displaying which list type will be used """

        options = ['Stacks', 'Queues'] # <- list created only for dynamic display
        
        print('\nWhat would you like to work with:')
        print('-'*30)
        for index, list_type in enumerate(options, start=1):
            print(f'{index} - {list_type}')
        print('-'*30)

        return

def select_stacks_or_queues():
    """ method responsible for returning a numeric value and working based on this return """

    while True:

        stack_or_queue = read_numeric_option()

        if (stack_or_queue < 1 or
            stack_or_queue > 2): # <- this while true block only serves to define which path will be taken by the user after
            print('[ERROR] option not found\n') # deciding which option among the options, from here on we will know if they want to work with stacks or queues
            continue
        else:
            break

    return stack_or_queue

def return_formatted(option):
    """ separate and "irrelevant" method created only
    to return a formatted and dynamic display to the user """

    if option == 1:
        stack_and_queue = 'Stacks'
    else:  # <- this else block only serves to make a dynamic display in the main file
        stack_and_queue = 'Queues'

    return stack_and_queue

