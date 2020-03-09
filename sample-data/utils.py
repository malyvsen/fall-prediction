import os
import matplotlib.pyplot as plt
from voltage import Voltage



def dir_voltages(dir='original'):
    for filename in os.listdir(dir):
        with open(os.path.join(dir, filename), 'r') as file:
            yield filename, Voltage.from_file(file)


def render_plot(show, save_as):
    if show:
        plt.show()
    if save_as is not None:
        os.makedirs(os.path.dirname(save_as), exist_ok=True)
        plt.savefig(save_as, bbox_inches='tight')
    plt.clf()
