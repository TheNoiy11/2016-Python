from SimpleGraphics import *
from random import randint
from time import sleep
setAutoUpdate(False)

def newMap(mapY=25,mapX=25,value=1):
	map = []
	for y in range(mapY):
		row = []
		for x in range(mapX):
			row.append(value)
		map.append(row)
	return map

def drawMap(map,pixelSize=10):	
	resize(len(map[0])*pixelSize,len(map)*pixelSize)
	update()
	clear()
	for y in range(len(map)):
		for x in range(len(map[y])):
			if map[y][x] == 1:
				setColor(255,255,255)
			elif map[y][x] == 2:
				setColor(255,255,0)
			elif map[y][x] == 3:
				setColor(255,0,255)
			elif map[y][x] == 4:
				setColor(0,0,255)
			elif map[y][x] == 5:
				setColor(255,0,0)
			rect(1 + x*pixelSize, 1 + y*pixelSize,pixelSize,pixelSize)
	update()
	
def buttons(map):
	for y in range(2,5):
		for x in range(2,10):
			map[y][x] = 2
	for y in range(6,9):
		for x in range(2,10):
			map[y][x] = 3
	return map

map = buttons(newMap())

pixelSize = 10
flag = True
while flag and not closed():
	drawMap(map)
	mY = (mouseY()+1)/pixelSize
	mX = (mouseX()+1)/pixelSize
	if not mY > len(map) and not mY < 0 and not mX > len(map[0]) and not mX < 0:
		mY = int(mY//1)
		mX = int(mX//1)
		if map[mY][mX] == 2:
			print("BUTTON 1")
			if leftButtonPressed() == True:
				map = newMap(25,25,4)
		elif map[mY][mX] == 3:
			print("BUTTON 2")
			if leftButtonPressed() == True:
				map = newMap(25,25,5)
		else:
			print("NOTHING")