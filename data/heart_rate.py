import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



class HeartRate:
    def __init__(self, beat_times, heart_rate):
        self.beat_times = beat_times
        self.heart_rate = heart_rate


    def to_student_format(self):
        result = pd.DataFrame(data={'HR': self.heart_rate})
        # interpolate data to remove NaN values
        result = result.interpolate(method="linear").fillna(method="bfill").fillna(method="ffill")
        # remove outliers
        for i in range(5):
            df_copy = result.copy()
            df_copy = (result - result.mean()) / result.std()
            for column_name in df_copy:
                column = df_copy[column_name]
                outliers = column.rolling(window=31, center=True).median().fillna(method='bfill').fillna(method='ffill')
                diff = np.abs(column - outliers)
                outlier_ids = diff > 2 / (i+1)
                result[column_name][outlier_ids] = np.NaN
            result = result.interpolate(method="linear").fillna(method="bfill").fillna(method="ffill")

        # normalize
        min_heart_rate = 32 # value provided by student in original code
        max_heart_rate = 156
        result = ((result - min_heart_rate) / (max_heart_rate - min_heart_rate) - 0.5) * 2
        return result


    def plot(self, window_title='heart rate plot'):
        plt.plot(self.beat_times, self.heart_rate, label='heart rate')
        plt.xlabel('seconds')
        plt.ylabel('beats per minute')
        plt.legend()
        plt.gcf().canvas.set_window_title(window_title)
        plt.show()
