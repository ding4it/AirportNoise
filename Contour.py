import numpy as np
from scipy.interpolate import griddata
import matplotlib.pyplot as plt
import matplotlib._cntr as _cntr


'''
np.random.seed(0)
x = np.random.normal(size=200)
y = np.random.normal(size=200)
v = np.sqrt(x ** 2 + y ** 2)
xg, yg = np.mgrid[-2:2:100j, -2:2:100j]
vg = griddata((x, y), v, (xg, yg), method='cubic')
'''


class Contour:
	def __init__(self):
		self

	def getLines(self,ncols,nrows,x_min,x_max,y_min,y_max,z_min,z_max,data):
		xllcorner = x_min
		yllcorner = y_min
		x_cellsize = (x_max - x_min)/ncols
		y_cellsize = (y_max - y_min)/nrows
		yg = [[yllcorner + y_cellsize * i] * ncols for i in range(nrows)]
		xg = [[xllcorner + x_cellsize * i for i in range(ncols)]] * nrows
		#xg = [xllcorner + cellsize * i for i in range(ncols)] * nrows
		#yg = [[yllcorner + cellsize * (nrows - i-1 )] * ncols for i in range(nrows)] 
		vg = data
		max_data = max(max(i) for i in vg)
		min_data = min(min(i) for i in vg)
	
		xg = np.array(xg)
		yg = np.array(yg)
		vg = np.array(vg)

		lines = []
		c = _cntr.Cntr(xg, yg, vg)
		#plt.figure()
		for v in np.arange(min_data, max_data, 2):
		    t = c.trace(v)
		    for p in t[:len(t) // 2]:
		        if np.all(np.isnan(p)):
		            continue
		        lines.append(p.tolist())
		        #plt.plot(p[:, 0], p[:, 1], lw=2)
		        #r = np.sqrt(np.sum(p ** 2, 1))
		#plt.show()
		return lines


from SurferApp import SurferApp

if __name__ == '__main__':
	surfer = SurferApp()
	ncols,nrows,x_min,x_max,y_min,y_max,z_min,z_max,data = surfer.readGrd('E:/outgrid.grd')
	x = [ncols,nrows,x_min,x_max,y_min,y_max,z_min,z_max]
	print(x)
	contour = Contour()
	x = contour.getLines(ncols,nrows,x_min,x_max,y_min,y_max,z_min,z_max,data)
	print(x)
	print("Done")