import numpy as np
from nif.data.point_wise_data import PointWiseData
import os

class TravelingWave(PointWiseData):
    def __init__(self):
        path = os.path.abspath(__file__)
        dir_path = os.path.dirname(path)
        data = np.load(dir_path+'/dataset/traveling_wave.npz')['data']
        parameter_data = data[:,[0]]
        x_data = data[:,[1]]
        u_data = data[:,[2]]
        super(TravelingWave, self).__init__(parameter_data, x_data, u_data)
        self.data, self.mean, self.std = self.standard_normalize(self.data_raw)

if __name__=='__main__':
    tw = TravelingWave()
    print(tw.data.mean(axis=0))
    print(tw.data.std(axis=0))
    print(tw.parameter.shape)
    print(tw.x.shape)
    print(tw.u.shape)
