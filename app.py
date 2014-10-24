from flask import Flask,render_template
class AirportNoise:
	''' this is initialize .
		longitude_path and latitude_path has multiple lines
		every line has 3 values like 23 27 50 which means 23° 27.500′
	'''
	def __init__(self,longitude_path,latitude_path):
		self.longitude_path = longitude_path
		self.latitude_path = latitude_path
		self.longitude = []
		self.latitude = []

		with open(self.longitude_path) as f:
			for line in f:
				a,b,c = line.split(" ")
				a,b,c, = int(a),int(b),int(c)
				self.longitude.append(a + b/60 + c/3600)
		self.length = len(self.longitude)
		#print("longitude:{}".format(self.longitude))

		with open(self.latitude_path) as f:
			for line in f:
				a,b,c = line.split(" ")
				a,b,c, = int(a),int(b),int(c)
				self.latitude.append(a + b/60 + c/3600)

		#print("latitude:{}".format(self.latitude))

	'''get the longitude value'''
	def get_Longitude(self):
		pass

	''' get the latitude value'''
	def get_latitude(self):
		pass




a = AirportNoise(r"E:\机场噪声\AirportNoise\latitude.txt",
		r"E:\机场噪声\AirportNoise\longitude.txt")

app = Flask(__name__)
@app.route('/hello/')
@app.route('/hello/<name>')
def run(name=None):
   	return render_template('hello.html', name=name,
   		length = a.length, longitude = a.longitude, latitude = a.latitude)

'''the main fun '''
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080, debug=True)
