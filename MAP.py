from SimpleGraphics import *
from random import randint

setAutoUpdate(False)

def newMap(mapX=10,mapY=10):
	map = []
	for i in range(mapY):
		row = []
		for j in range(mapX):
			rand = randint(0,2)
			if rand == 0:
				nextTile = "Alive"
			else:
				nextTile = "Dead"
			row.append(nextTile)
		map.append(row)
	return map

def drawMap(map,tileSize=10):
	resize(len(map[0])*tileSize,len(map)*tileSize)
	update()
	clear()
	for i in range(len(map[0])):
		for j in range(len(map)):
			if map[j][i] == "Alive":
				setColor(255,255,255)
				rect(1 + i*tileSize, 1 + j*tileSize,tileSize,tileSize)
			elif map[j][i] == "Dead":
				setColor(0,0,0)
				rect(1 + i*tileSize, 1 + j*tileSize,tileSize,tileSize)
	update()

def checkMap(map):
	newMap = map[:]
	for i in range(len(map[0])):
		for j in range(len(map)):
			count = 0
			for y in range(-1,2):
				for x in range(-1,2):
					tempj = j+x
					tempi = i+y
					if tempj > len(map[0])-1:
						tempj = 0
					elif tempj < 0:
						tempj = len(map[0])-1
					
					if tempi > len(map)-1:
						tempi = 0
					elif tempi < 0:
						tempi = len(map)-1
					
					if map[tempj][tempi] == "Alive":
						if map[tempj][tempi] != map[j][i]:
							count = count + 1
					
						
			if map[j][i] == "Alive":
				if count < 2:
					newMap[j][i] = "Dead"
				elif count == 2:
					newMap[j][i] == "Alive"
				elif count > 3:
					newMap[j][i] = "Dead"
			elif map[j][i] == "Dead":
				if count == 3:
					newMap[j][i] = "Alive"
				
	return newMap

GOL = newMap(50,50)
drawMap(GOL)
for i in range(10):
	GOL = checkMap(GOL)
	drawMap(GOL)