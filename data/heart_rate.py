import matplotlib.pyplot as plt



class HeartRate:
    def __init__(self, beat_times, heart_rate):
        self.beat_times = beat_times
        self.heart_rate = heart_rate


    def plot(self, window_title='heart rate plot'):
        plt.plot(self.beat_times, self.heart_rate, label='heart rate')
        plt.xlabel('seconds')
        plt.ylabel('beats per minute')
        plt.legend()
        plt.gcf().canvas.set_window_title(window_title)
        plt.show()
