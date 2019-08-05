import os
from utils import dir_voltages



out_dir = 'student_format'
os.makedirs(out_dir, exist_ok=True)

if __name__ == '__main__':
    for filename, voltage in dir_voltages():
        student_format = voltage.to_heart_rate().to_student_format()
        student_format.to_csv(os.path.join(out_dir, filename), index=False)
