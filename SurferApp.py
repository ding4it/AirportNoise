import win32com.client 


class SurferApp:
	
	def __init__(self):
		self._surfer = win32com.client.Dispatch('Surfer.Application')	
	
	def gridData(self,import_file,output_file):
		self._surfer.GridData(DataFile =import_file,
			Algorithm = win32com.client.constants.srfKriging,
			OutFmt= win32com.client.constants.srfGridFmtAscii,
			OutGrid = output_file)

	def readASC(self,filePath):
		with open(filePath,"r") as f:
			ncols = int(f.readline().split(" ")[1])
			nrows = int(f.readline().split(" ")[1])
			xllcorner = float(f.readline().split(" ")[1]) 
			yllcorner = float(f.readline().split(" ")[1])
			cellsize =  float(f.readline().split(" ")[1])
			nodata_value = float(f.readline().split(" ")[1])
			data = []
			line = f.readline()
			while line:
				tmp = [float(x) for x in line.split(" ")]
				data.extend(tmp)
				line = f.readline()
			tmp = []
			for i in range(nrows):
				tmp.append(line[i:i+ncols])
			data = tmp
			return [ncols,nrows,xllcorner,yllcorner,cellsize,nodata_value,data]

	def readDat(self,filePath):
		x = []
		y = []
		z = []

		with open(filePath,"r") as f:
			line=f.readline()
			while line:
				a,b,c = line.split(" ")

				x.append(float(a))
				y.append(float(b))
				z.append(float(c))
				line=f.readline()#如果没有这行会造成死循环  
		return [x,y,z]

	def readGrd(self,filePath):
		with open(filePath,"r") as f:
			title = f.readline()
			ncols, nrows = [int(i) for i in f.readline().split(" ")]
			x_min, x_max = [float(i) for i in f.readline().split(" ")] 
			y_min, y_max = [float(i) for i in f.readline().split(" ")]
			z_min, z_max = [float(i) for i in f.readline().split(" ")]
			data = []
			for i in range(nrows):
				tmp = [float(x) for x in f.readline().split(" ")[:-1]]
				data.append(tmp)
			return [ncols,nrows,x_min,x_max,y_min,y_max,z_min,z_max,data]
	
	def close(self):
		self._surfer.Quit()


'''the main fun '''
if __name__ == '__main__':
	surfer = SurferApp()
	surfer.gridData("E:/asdf.csv","E:/outgrid.grd")
	x = surfer.readGrd("E:/outgrid.grd")
	#print(x)
	print("Done")
