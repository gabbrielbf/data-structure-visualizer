from abc import ABC, abstractmethod

class DataStructure(ABC):
    """ separate class to define the type of list to be worked with """

    def __init__(self, capacity=None): # <- defaulting to None if the user doesn't want to limit items
        self._items = [] # <- starting an empty list in the parent class so that child classes only implement the way to handle their respective
        self._capacity = capacity # <- add new attribute to store maximum limit,
        return

    def is_full(self):
        """ checks if the structure has reached its maximum capacity """

        if self._capacity is None:
            return False
        return len(self._items) >= self._capacity

    def display_items(self):
        """ global method for displaying items because
        both lists use the same logic to display their elements """

        if self._items:
            print(f'\nDisplaying the list of {self.__class__.__name__}:')  # <- this line displays in real time the name of the list to be manipulated
            print('-' * 30)
            for index, item in enumerate(self._items, start=1):
                print(f'{index} - {item} ({type(item).__name__})')  # <- displaying the position, item, and the data type of the added item
            print('-' * 30)
        else:
            print(f'\nThe list of {self.__class__.__name__} is empty!\n')

    @abstractmethod
    def add_item(self, item):
        """ global method for adding elements
        regardless of the list type """
        pass

    @abstractmethod
    def remove_item(self):
        """ method responsible for general item removal, regardless of whether it is a STACK or QUEUE because
        what will define the removal will be the instantiated class itself in the procedural program """
        pass


class Stacks(DataStructure):

    def add_item(self, item):
        if self.is_full(): # <- this block check item count before returning to add_item
            print(f'\n[ERROR] Stack Overflow! The {self.__class__.__name__} is full (Max: {self._capacity}).\n')
            return False
        self._items.append(item)

        data_type = type(item).__name__ # <- this variable gets the name of the data type written in the input above and displays it to the user below
        structure_name = self.__class__.__name__ # <- this variable only serves to make a dynamic list name display

        print(f'\nThe element {item} ({data_type}) was added to the {structure_name} list ✔\n') # saw to the user about which list we are manipulating

        return True

    def remove_item(self):
        if self._items:
            print('-'*30)
            print('Stack (LIFO - Last In, First Out)')
            print(f'Removed the last item: {self._items[-1]}')
            print('-'*30)
            self._items.pop()
        else:
            print(f'\nThe list of {self.__class__.__name__} is empty!\n')
        return 


class Queues(DataStructure):

    def add_item(self, item):
        if self.is_full():
            print(f'[ERROR] Queue Overflow! The {self.__class__.__name__} is full (Max: {self._capacity}).\n')
            return False
        self._items.append(item)

        data_type = type(item).__name__
        structure_name = self.__class__.__name__ 

        print(f'\nThe element {item} ({data_type}) was added to the {structure_name} list ✔\n') 
        return True # <- return boolean to indicate success status of add_item

    def remove_item(self):
        if self._items:
            print('-'*30)
            print('Queue (FIFO - First In, First Out / First in is the first out)')
            print(f'We removed the first item: {self._items[0]}')
            print('-'*30)
            self._items.pop(0)
        else:
            print(f'\nThe {self.__class__.__name__} list is empty!\n')
        return
