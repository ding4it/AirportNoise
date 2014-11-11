from SurferApp import SurferApp
from ExcelApp import ExcelApp
from Contour import Contour

class AirportNoise:
    ''' this is initialize .
        longitude_path and latitude_path has multiple lines
        every line has 3 values like 23 27 50 which means 23° 27.500′
    '''

    def __init__(self, longitude_path, latitude_path):
        self.longitude_path = longitude_path
        self.latitude_path = latitude_path
        self.longitude = []
        self.latitude = []

        with open(self.longitude_path) as f:
            for line in f:
                a, b, c = line.split(" ")
                a, b, c, = int(a), int(b), int(c)
                self.longitude.append(a + b / 60 + c / 3600)
        self.length = len(self.longitude)
        # print("longitude:{}".format(self.longitude))

        with open(self.latitude_path) as f:
            for line in f:
                a, b, c = line.split(" ")
                a, b, c, = int(a), int(b), int(c)
                self.latitude.append(a + b / 60 + c / 3600)