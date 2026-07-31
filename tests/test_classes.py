from src.classes import Stacks, Queues

def test_stack_behavior():
    """ tests if the stack follows the LIFO 
    (Last In, First Out) principle correctly """

    stack = Stacks() # <- # creates an empty stack instance

    stack.add_item('Pineapple') # { adds elements 
    stack.add_item('Bread') # } to the stack

    # checks if the last item added is at the top (index -1)
    assert stack._items[-1] == 'Bread'

    # simulates removing the last item (pop)
    stack._items.pop()

    # checks if the remaining item is now Apple
    assert stack._items[-1] == 'Pineapple'
    return

