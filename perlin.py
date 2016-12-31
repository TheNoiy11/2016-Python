from SimpleGraphics import *
from random import randint
from hsvTOrgb import *
setAutoUpdate(False)

width = 1000
height = 1000
resize(width,height)
update()

TERRAIN = True

def main():
	global xscale
	global yscale
	global TERRAIN
	
	fileOpen = open("perlin.txt","r")
	fileData = fileOpen.read()
	fileOpen.close()

	fileData = fileData.split("\n")
	fileData.pop()
	for i in range(len(fileData)):
		fileData[i] = fileData[i].strip("|").split("|")

	for row in range(len(fileData)):
		for col in range(len(fileData[row])):
			fileData[row][col] = int(float(fileData[row][col]))

	xscale = width/len(fileData)
	yscale = height/len(fileData[0])
	print(len(fileData), len(fileData[0]))
	print(xscale, yscale)
	
	for row in range(len(fileData)):
		for col in range(len(fileData[row])):
			value = fileData[row][col]
			if TERRAIN:
				if value <= 127:
					#Water
					setColor(0, 0, value)
				elif value > 127 and value <= 130:
					#Sand
					setColor(255, 250 ,107)
				elif value > 130 and value <= 140:
					#Grass no trees
					setColor(50, value, 50)
				elif value > 140:
					#Grass, chance of trees
					if randint(0,10) == 0:
						setColor(25, 75, 25)
					else:
						setColor(50, value, 50)
				rect(col*yscale, row*xscale, yscale, xscale)
			else:
				setColor(value, value, value)
				rect(col*yscale, row*xscale, yscale, xscale)
	update()

main()
print('DONE')