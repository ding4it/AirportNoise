import xlrd
class ExcelApp:
	def __init__(self,filePath,sheet_num,start_row,start_col):
		self.workbook = xlrd.open_workbook(filePath) # 'E:/datas_2014082600_2014082700.xls'
		self.current_row = start_row
		self.current_col = start_col
		self.table = self.workbook.sheets()[0]
		self.nrows = self.table.nrows
		self.ncols = self.table.ncols

	def getData(self):
		data = self.table.row_values(self.current_row);
		self.current_row += 1;
		return data[self.current_col:]

	def saveToCSV(self,filePath,title,arr):
		with open(filePath,"w") as f:
			f.write(",".join(title))
			f.write('\n')
			for data in arr:
				f.write(",".join(str(x) for x in data))
				f.write("\n")
				
	def close(self):
		pass					
def main():
	X = [ 53, 53, 28, 28, 53, 53, 30, 28, 53, 53, 44, 43, 43, 42, 43, 43, 40, 31, 42, 30];
	Y = [ 49, 49, 60, 59, 49, 49, 58, 59, 49, 49, 49, 49, 46, 48, 46, 46, 49, 58, 48, 58];
	excel = ExcelApp('E:/datas_2014082600_2014082700.xls',0,3,1)
	a = excel.getData()
	#print(type(a))
	title = ['X','Y','Z']
	arr = map(lambda x,y,z:[x,y,z],X,Y,a)
	excel.saveToCSV("E:/asdf.csv",title,arr);
	excel.close()
	print("Done")	
				
'''the main fun '''
if __name__ == '__main__':
	main()



