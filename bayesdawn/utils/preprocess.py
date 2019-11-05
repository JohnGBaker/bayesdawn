from scipy import signal
import numpy as np


def preprocess(config, td, i1, i2):

    del_t = td[1, 0] - td[0, 0]

    if config['InputData'].getboolean('decimation'):
        fc = config['InputData'].getfloat('filterFrequency')
        b, a = signal.butter(5, fc, 'low', analog=False, fs=1/del_t)
        Xd = signal.filtfilt(b, a, td[:, 1])
        Yd = signal.filtfilt(b, a, td[:, 2])
        Zd = signal.filtfilt(b, a, td[:, 3])
        # Downsampling
        q = config['InputData'].getint('decimationFactor')
        tm = td[i1:i2:q, 0]
        Xd = Xd[i1:i2:q]
        Yd = Yd[i1:i2:q]
        Zd = Zd[i1:i2:q]

    else:
        q = 1
        tm = td[i1:i2, 0]
        Xd = td[i1:i2, 1]
        Yd = td[i1:i2, 2]
        Zd = td[i1:i2, 3]

    return tm, Xd, Yd, Zd, q