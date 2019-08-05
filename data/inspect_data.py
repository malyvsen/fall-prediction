import os
from voltage import Voltage


in_dir = 'original'

if __name__ == '__main__':
    for filename in os.listdir(in_dir):
        with open(os.path.join(in_dir, filename), 'r') as in_file:
            voltage = Voltage.from_file(in_file)
            voltage.plot(window_title=filename)
            voltage.to_heart_rate().plot(window_title=filename)
