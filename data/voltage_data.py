import csv
import numpy as np
from scipy.signal import savgol_filter, find_peaks
import matplotlib.pyplot as plt



class VoltageData:
    def __init__(self, resolution, voltage):
        self.resolution = resolution
        self.voltage = voltage


    @classmethod
    def from_file(cls, file):
        reader = csv.reader(file)
        first_row = next(reader)
        second_row = next(reader)
        voltage = []
        for row in reader:
            voltage.append(float(row[1]))
        return cls(resolution=float(second_row[3]), voltage=np.array(voltage))


    def smooth(self, window_seconds=0.25):
        window_size = int(window_seconds // self.resolution // 2 * 2) + 1
        smooth_voltage = savgol_filter(self.voltage, window_size, polyorder=3)
        return type(self)(self.resolution, smooth_voltage)


    def change_resolution(self, target_resolution):
        resolution_ratio = int(target_resolution // self.resolution)
        voltage_cut = self.voltage[:len(self.voltage) // resolution_ratio * resolution_ratio]
        result_voltage = np.mean(np.reshape(voltage_cut, (-1, resolution_ratio)), axis=-1)
        return type(self)(target_resolution, result_voltage)


    def power_spectrum(self):
        return np.abs(np.fft.rfft(self.voltage))


    def peaks(self, prominence=None, distance_seconds=0.3):
        if prominence is None:
            prominence = 0.5 * (np.max(self.voltage) - np.min(self.voltage))
        distance = int(distance_seconds // self.resolution)
        return find_peaks(self.voltage, prominence=prominence, distance=distance)[0]


    def plot(self, window_title='VoltageData plot'):
        seconds = np.linspace(0, len(self.voltage) * self.resolution, len(self.voltage))
        plt.plot(seconds, self.voltage, label='voltage')
        plt.plot(seconds, self.smooth().voltage, label='voltage, smoothed')
        peaks = self.peaks()
        plt.plot(seconds[peaks], self.voltage[peaks], 'x', label='peaks')
        plt.xlabel('seconds')
        plt.ylabel('volts')
        plt.legend()
        plt.gcf().canvas.set_window_title(window_title)
        plt.show()
