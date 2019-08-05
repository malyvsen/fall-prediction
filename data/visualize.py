from utils import dir_voltages



if __name__ == '__main__':
    for filename, voltage in dir_voltages():
        voltage.plot(window_title=filename)
        voltage.to_heart_rate().plot(window_title=filename)
