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

def test_queue_behavior():
    """ tests if the queue follows the FIFO 
    (First In, First Out) principle correctly """

    # The code below is similar to Stacks, so in case of doubt, 
    # just read the comments of the function above.

    queue = Queues()

    queue.add_item('First')
    queue.add_item('Second')

    assert queue._items[0] == 'First'

    queue._items.pop(0)

    assert queue._items[0] == 'Second'

    return

def test_capacity_overflow():
    """ tests if the stack correctly blocks 
    elements when reaching maximum capacity """

    stack = Stacks(capacity=2) # <- creates a stack with a small capacity limit of 2

    res1 = stack.add_item(10) # { adds elements up 
    res2 = stack.add_item(20) # } to the limit

    assert res1 == True # { verifies that both 
    assert res2 == True # } additions were successful

    res3 = stack.add_item(30) # <- tries to add a third element, which should exceed capacity

    assert res3 == False # <- verifies that the addition was blocked (returns False due to overflow)

    return