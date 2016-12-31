def readCityFile(filename):
	file = open(filename)
	data = file.read()
	file.close()
	data = data.split(",")
	
	map = []
	
	solid = True
	for char in line:
		if char != "\t":
			solid = False
		else:
			for i in range(width):
				row.append(solid)
			solid = True
	for i in range(width):
		row.append(row)
	return map
	
def makeCityImage(map,room):
	rows =len(map)
	cols = len(map[0])
	wide
	
#not finished yet and will be continued in next lecture