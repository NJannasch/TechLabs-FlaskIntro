""" Minimal example how to read and store data. """

import json

def load_data(filename: str):
    """ Try to read data from file. """

    try:
        with open(filename) as f:
            data = json.load(f)
    except:
        print("Could not open file")
        data = []
        
    return data

def save_data(filename: str, data):
    """ Save data to file """

    with open(filename, 'w+') as f:
        json.dump(data, f)