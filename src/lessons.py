DIVIDER = '=' * 60

_temp_stack = """🚀 WELCOME TO THE STACK AND QUEUE SIMULATOR! 🚀"""

BANNER = "\n".join(l.center(60) for l in _temp_stack.splitlines())

INTRO_TEXT = """This interactive program was developed to demonstrate
in practice how two of the most important data structures
in computing work:

📌 STACKS (Stack - LIFO: Last In, First Out)
📌 QUEUES (Queue - FIFO: First In, First Out)
"""

# THEORY in lessons.py file

_temp_stack = """ -----------> WHAT IS A STACK? <-----------
Imagine a stack of plates. The last plate that
you place is the first one you remove
(LIFO - Last In, First Out).
Practical example: Browser history
or the 'Undo' command itself (Ctrl+Z). """.center(60)

STACK_THEORY = "\n".join(l.center(60) for l in _temp_stack.splitlines())

_temp_stack = """ -----------> WHAT IS A QUEUE? <-----------
Imagine a bank queue. The first person
who arrives is the first to be served
(FIFO - First In, First Out).
Practical example: Print queue
or process scheduling. """

QUEUE_THEORY = "\n".join(l.center(60) for l in _temp_stack.splitlines())