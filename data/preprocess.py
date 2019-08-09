import os
from utils import dir_voltages



out_dir = 'preprocessed'
os.makedirs(out_dir, exist_ok=True)

if __name__ == '__main__':
    for filename, voltage in dir_voltages():
        preprocessed = voltage.to_heart_rate().preprocessed()
        preprocessed.to_csv(os.path.join(out_dir, filename), index=False)
