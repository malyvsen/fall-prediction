import os
from voltage_data import VoltageData


in_dir = 'original'

if __name__ == '__main__':
    for filename in os.listdir(in_dir):
        with open(os.path.join(in_dir, filename), 'r') as in_file:
            data = VoltageData.from_file(in_file)
            data.plot(window_title=filename)
