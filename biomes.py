from SimpleGraphics import *
from random import randint
from hsvTOrgb import *

setAutoUpdate(False)
resize(900,900)
update()

fileOpen = open("biomes.txt","r")
fileData = fileOpen.read()
fileOpen.close()

fileData = fileData.split("\n\n\n")
fileData.pop()

for i in range(len(fileData)):
	fileData[i] = fileData[i].split("\n\n")
	
for h in range(len(fileData)):
	for i in range(len(fileData[h])):
		fileData[h][i] = fileData[h][i].split("\n")

for h in range(len(fileData)):
	for i in range(len(fileData[h])):
		for j in range(len(fileData[h][i])):
			fileData[h][i][j] = fileData[h][i][j].strip("|").split("|")
		
for h in range(len(fileData)):
	for i in range(len(fileData[h])):
		for j in range(len(fileData[h][i])):
			for k in range(len(fileData[h][i][j])):
				fileData[h][i][j][k] = int(float(fileData[h][i][j][k]))

def checkBiome(value):
	type = ""
	if value > 0 and value <=100:
		type = "OCEAN"
	elif value > 100 and value <=200:
		type = "FOREST"
	elif value > 200 and value <=300:
		type = "PLAINS"
	elif value > 300 and value <=400:
		type = "DESERT"
	else:
		type = "unknown"
	
	
	if type == "OCEAN":
		temp = value
		return getRGB(217, 0.83, temp/100)
	elif type == "FOREST":
		temp = value - 100
		return getRGB(120, 1, temp/200)
	elif type == "PLAINS":
		temp = value - 200
		return getRGB(126, 0.5, temp/100)
	elif type == "DESERT":
		temp = value - 300
		return getRGB(57, 0.5, temp/100)
	else:
		print("IDK")
	
scale = 2
x = -1
y = -1
for h in range(len(fileData)):
	y += 1
	x = -1
	for i in range(len(fileData[h])):
		x += 1
		for j in range(len(fileData[h][i])):
			for k in range(len(fileData[h][i][j])):
				r, g, b = checkBiome(fileData[h][i][j][k])
				#print(r, g, b)
				setColor(r, g, b)
				rect(k*scale + (x * len(fileData[h][i]))*scale, j*scale + (y * len(fileData[h][i][j]))*scale, scale,scale)
			
update()