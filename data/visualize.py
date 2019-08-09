from utils import dir_voltages



def visualize_all(voltages=None, show=True, save=False):
    if voltages is None:
        voltages = dir_voltages()
    for filename, voltage in voltages:
        save_as = None if not save else 'plots/' + filename.replace('.csv', '_voltage.png')
        voltage.plot(window_title=filename, show=show, save_as=save_as)
        save_as = None if not save else 'plots/' + filename.replace('.csv', '_heart_rate.png')
        voltage.to_heart_rate().plot(window_title=filename, show=show, save_as=save_as)



if __name__ == '__main__':
    visualize_all()
