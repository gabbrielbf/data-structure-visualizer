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

    def load_data(self):
        """ loads data from the json file if it exists
        returing a dictionary with the items """

        if not os.path.exists(self._filename): # <- checks if the file exists before trying to read it
            return {'stacks': [], 'queues': []}

        # opens the file in read mode and loads the json content back to python
        with open(self._filename, 'r', encoding='utf-8') as file:
            try:
                data = json.load(file)
                return data
            except json.JSONDecodeError: # <- handles corrupted or empty json files gracefully
                return {'stacks': [], 'queues': []}