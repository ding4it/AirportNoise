from flask import Flask, render_template
from SurferApp import SurferApp
from ExcelApp import ExcelApp
from Contour import Contour
from AirportNoise import AirportNoise
import pythoncom
import json



latitude_path = r"E:\AirportNoiseProject\AirportNoise\latitude.txt"
longitude_path = r"E:\AirportNoiseProject\AirportNoise\longitude.txt"
X = [ 53, 53, 28, 28, 53, 53, 30, 28, 53, 53, 44, 43, 43, 42, 43, 43, 40, 31, 42, 30]
Y = [ 49, 49, 60, 59, 49, 49, 58, 59, 49, 49, 49, 49, 46, 48, 46, 46, 49, 58, 48, 58]
excel_path = 'E:/datas_2014082600_2014082700.xls'

app = Flask(__name__)
a = AirportNoise(latitude_path,longitude_path)
excel = ExcelApp(excel_path,0,3,1)
title = ['X','Y','Z']
csv_path = 'E:/noisepath.csv'
output_file = "E:/output.grd"
contour = Contour()


@app.route('/')
@app.route('/index.html')

def index(name=None):

    lines = getData()

    return render_template('hello.html', length=a.length,
        longitude=a.longitude, latitude=a.latitude,lines=lines)

def getData():
    pythoncom.CoInitialize()
    excel_data= excel.getData()
    arr = map(lambda x,y,z:[x,y,z],a.latitude,a.longitude,excel_data)
    excel.saveToCSV(csv_path,title,arr)
    surfer = SurferApp()
    surfer.gridData(csv_path,output_file)
    ncols,nrows,x_min,x_max,y_min,y_max,z_min,z_max,data = surfer.readGrd(output_file) 
    lines = contour.getLines( ncols,nrows,x_min,x_max,y_min,y_max,z_min,z_max,data)
    return lines

@app.route('/getData')
@app.route('/getData.html')
def Datapage():
    lines = getData()
    return json.dumps(lines)
'''the main fun '''
if __name__ == '__main__':
    adfae = 1    
    app.run(host="0.0.0.0", port=8080, debug=True)
