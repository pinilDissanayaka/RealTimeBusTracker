import os


def read_data():
    try:
        with open("test/data/bus1.json") as data_file:
            data = data_file.read()
    except FileNotFoundError as e:
        raise e
    
    return data