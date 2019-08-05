import os
from voltage import Voltage



def dir_voltages(dir='original'):
    for filename in os.listdir(dir):
        with open(os.path.join(dir, filename), 'r') as file:
            yield filename, Voltage.from_file(file)
