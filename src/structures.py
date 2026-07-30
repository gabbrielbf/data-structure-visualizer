# data structure
from .menu import numbered_menu, clear_terminal, display_stacks_or_queues, select_stacks_or_queues, return_formatted # { we use a "." after "from" to be able to import these functions and methods
from .classes import Stacks, Queues # for the "main" file and thus make it work 
from .lessons import * # } in the cleanest way possible, displaying to the user only what is necessary

import time, sys, ast # <- this 3 libraries work together in teach_user to print lessons.py character-by-character

def get_capacity():
    """ function to read the maximum capacity defined by the user """

    while True:
        try:
            user_input = input('Enter the maximum capacity (or press ENTER for unlimited): ').strip()
            if user_input == '' or not user_input.strip():
                return None # <- no limit
            
            capacity = int(user_input)

            if capacity <= 0:
                print('\n[ERROR] Capacity must be greater than zero!\n')
                continue
            return capacity
        
        except ValueError:
            print('\n[ERROR] Invalid number!\n')
            continue

def get_element(structure):
    """ function created only to make
    method 1 of the "run_code" function cleaner """

    while True:
        user_input = input('Which element would you like to add: ')
        if user_input == '' or not user_input.strip(): # <- Block responsible for preventing the user from introducing empty spaces into the list
            print('\n[ERROR] Empty spaces are not allowed!\n')
            continue
        else:
            try: # <- tries to convert to native primitive type (int, float, bool, etc)

                converted_input = ast.literal_eval(user_input.strip())

            except (ValueError, SyntaxError): # <- if it doesn't convert, it means it's a normal string!

                converted_input = user_input.strip() # <- this .strip() method ensures that even after passing through the first empty spaces check
                                                    # <- the user will not be able to add a string with empty space at the beginning or end of the input

            data_type = type(converted_input).__name__ # <- this variable gets the name of the data type written in the input above and displays it to the user below
            structure_name = structure.__class__.__name__ # <- this variable only serves to make a dynamic list name display

            print(f'\nThe element {converted_input} ({data_type}) was added to the {structure_name} list ✔\n') # saw to the user about which list we are manipulating
            break

    return converted_input

def teach_user():
    """ dynamic and animated display for
    user immersion into the content """

    clear_terminal()
    print(DIVIDER)
    for char in BANNER: # <- this block displays letter by letter of the header
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.06)
    print()
    print(DIVIDER)
    print(INTRO_TEXT)

    clear_terminal()

    print(DIVIDER)
    for char in STACK_THEORY:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    print()
    print(DIVIDER)

    input('Press ENTER to continue...')

    print(DIVIDER)
    for char in QUEUE_THEORY:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    print()
    print(DIVIDER)

    return

def exit_program():
    """ function that exits (or not) the program
    according to a user interaction """

    while True:
        try:

            certainty = str(input('Are you sure you want to exit?[Y/N]: ')).lower().strip()

            if certainty != 'y' and certainty != 'n': # <- Checks if the user typed something other than Y or N
                print('\n[ERROR] Only [Y/N]!')
                continue

        except ValueError:
            print('\n[ERROR] Invalid value.\n')
            continue
        break

    if certainty == 'y':
        print('\nProgram ended.\n') # <- EXITS
        return True

    elif certainty == 'n':
        print('\nThen let\'s go back!\n') # <- GOES BACK TO THE MENU

    return False

def set_structure(stacks, queues):
    """ function designated to select the manipulation flow of the lists between stacks or
    queues only once, removing the need to always choose which list to manipulate """

    current_structure = None

    display_stacks_or_queues()
    option = select_stacks_or_queues() # <- selects which list to manipulate between STACKS or QUEUES

    if option == 1: # <- CASE 1 - STACKS
        current_structure = stacks
    else: # OTHER CASE (in this case 2) - QUEUES
        current_structure = queues

    formatted_name = return_formatted(option)

    print('-'*30)
    print(f'We will work with {formatted_name}')

    return current_structure # <- returns the current structure to continue with the program working on its respective list

def run_code():
    """ function responsible for taking all functions defined above and making them work together with
    a code block that defines the user's path through decisions made based on the "numbered_menu" """

    teach_user()
    input('Press ENTER to continue...')
    print(DIVIDER)
    print('Configuration of Structure Capacity'.center(60))
    print(DIVIDER)
    max_capacity = get_capacity()

    # pass capacity as a parameter inside the created objects
    stacks = Stacks(capacity=max_capacity) # { objects created to work together with the "set_structure" function, it will take them as parameters
    queues = Queues(capacity=max_capacity) # } and switch in real time according to the decision from (match - option == 4)
    
    current_structure = set_structure(stacks, queues)
    input('Press ENTER to continue...')

    while True:

        clear_terminal()
        print('-'*30)
        print(f'Working with: {current_structure.__class__.__name__}')
        option = numbered_menu()

        match option:
            case 1:
                element = get_element(current_structure)
                current_structure.add_item(element)
            case 2:
                current_structure.remove_item()
            case 3:
                current_structure.display_items()
            case 4:
                if isinstance(current_structure, Stacks): # <- # if the current structure is a Stack, switch to Queue (and vice versa)
                    current_structure = queues
                else:
                    current_structure = stacks
                print(f"\nSwitched!\nNow we will work with: {current_structure.__class__.__name__}\n")
            case 5:
                if exit_program() == True:
                    break
                else:
                    continue

    return