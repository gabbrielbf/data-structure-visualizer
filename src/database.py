import json
import os

class DatabaseManager:
    """ class responsible for handling data persistence 
    saving and loading items using a json file """

    def __init__(self, filename="database.json"):
        self._filename = filename
        return

    def save_data(self, stack_items, queue_items):
        """ saves the current state of stacks and queues
        into local json file """

        data = {
            'stacks': stack_items, # <- organizing data into a python dictionary before saving
            'queues': queue_items
        }

        with open(self._filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4) # <- this block opens the file in write mode and dumps the dictionary into json format

        print(f'\n[INFO] Data succssufully saved to {self._filename} ✔\n')