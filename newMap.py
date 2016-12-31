from random import randint, seed
from SimpleGraphics import *
from time import sleep
from copy import deepcopy

setAutoUpdate(False)

def newMap(mapY=25,mapX=25,empty=False,SEED=seed()):
	seed(SEED)
	map = []
	if empty == False:
		intEmpty = 0
	else:
		intEmpty = 1
	for y in range(mapY):
		row = []
		for x in range(mapX):
			rand = randint(intEmpty,7)
			if rand == 0:
				nextTile = "Alive"
			else:
				nextTile = "Dead"
			row.append(nextTile)
		map.append(row)
	return map
	
def checkMap(map):
	nextMap = deepcopy(map)
	for y in range(len(map)):
		for x in range(len(map[y])):
			count = 0
			for ySurround in range(-1,2):
				testY = y+ySurround
				for xSurround in range(-1,2):
					testX = x+xSurround
					
					if testY > len(map) -1:
						testY = 0
					elif testY < 0:
						testY = len(map) -1
						
					if testX > len(map[0]) -1:
						testX = 0
					elif testX < 0:
						testX = len(map[0]) -1
					
					if testY == y and testX == x:
						count = count
					else:
						if map[testY][testX] == "Alive":
							count = count + 1
			if map[y][x] == "Alive":
				if count < 2:
					nextMap[y][x] = "Dead"
				elif count > 3:
					nextMap[y][x] = "Dead"
			elif map[y][x] == "Dead":
				if count == 3:
					nextMap[y][x] = "Alive"
	return nextMap

def drawMap(map,tileSize=10):
	resize(len(map[0])*tileSize,len(map)*tileSize)
	update()
	clear()
	for y in range(len(map)):
		for x in range(len(map[0])):
			if map[y][x] == "Alive":
				setColor(255,255,255)
				rect(1 + x*tileSize, 1 + y*tileSize,tileSize,tileSize)
			elif map[y][x] == "Dead":
				setColor(0,0,0)
				rect(1 + x*tileSize, 1 + y*tileSize,tileSize,tileSize)
	update()

def runMap(map=newMap(),tileSize=10):
	global FLAG2
	while not closed():
		drawMap(map,tileSize)
		map = checkMap(map)
		if getKeys() == {'space'}:
			print("EDITTING MAP IN 1 SECOND")
			sleep(1)
			break
		elif getHeldKeys() == {'q'}:
			FLAG2 = False
			map = clearCurrentMap(map,tileSize)
			break
	return map

def editMap(map=newMap(empty=True), tileSize=10):
	global FLAG2
	while not closed():
		drawMap(map,tileSize)
		tempmY = (mouseY()+1)/tileSize
		tempmX = (mouseX()+1)/tileSize
		if not tempmY > len(map) and not tempmY < 0 and not tempmX > len(map[0]) and not tempmX < 0:
			mY = int(tempmY//1)
			mX = int(tempmX//1)
			if leftButtonPressed() == True:
				map[mY][mX] = "Alive"
				drawMap(map,tileSize)
			elif rightButtonPressed() == True:
				map[mY][mX] = "Dead"
				drawMap(map,tileSize)
		if getKeys() == {'space'}:
			print("RUNNING MAP IN 1 SECOND")
			sleep(1)
			break
		elif getHeldKeys() == {'q'}:
			FLAG2 = False
			map = clearCurrentMap(map,tileSize)
			break
	return map

def clearCurrentMap(map,tileSize):
	for y in range(len(map)):
		for x in range(len(map[0])):
			map[y][x] = "Dead"
	drawMap(map,tileSize)
	return map

def gliderGun():
	map = newMap(35,70,True)
	map[1][25] = "Alive"
	for i in [23,25]:
		map[2][i] = "Alive"
	for i in [13,14,21,22,35,36]:
		map[3][i] = "Alive"
	for i in [12,16,21,22,35,36]:
		map[4][i] = "Alive"
	for i in [1,2,11,17,21,22]:
		map[5][i] = "Alive"
	for i in [1,2,11,15,17,18,23,25]:
		map[6][i] = "Alive"
	for i in [11,17,25]:
		map[7][i] = "Alive"
	for i in [12,16,57,58]:
		map[8][i] = "Alive"
	for i in [13,14,57,59]:
		map[9][i] = "Alive"
	map[10][59] = "Alive"
	for i in [59,60]:
		map[11][i] = "Alive"
	return map

def lwSpaceShip():
	map = newMap(empty=True)
	for j in [0,7,14]:
		for i in [1,2,3,4]:
			map[2+j][i] = "Alive"
		for i in [1,5]:
			map[3+j][i] = "Alive"
		map[4+j][1] = "Alive"
		for i in [2,5]:
			map[5+j][i] = "Alive"
	return map

def main():
	global FLAG
	global FLAG2
	FLAG = True
	map = []
	while FLAG:
		FLAG2 = True
		while FLAG:
			user = input("Which one?(random/empty/gliderGun/lwSpaceShip/test/quit): ")
			if user == "random":
				while True:
					y = input("Enter the y: ")
					x = input("Enter the x: ")
					tileSize = input("Enter the tileSize: ")
					if y.isdigit() == True and x.isdigit() == True and tileSize.isdigit() == True:
						if int(tileSize) > 1:
							y = int(y)
							x = int(x)
							tileSize = int(tileSize)
							break
						else:
							print("The tileSize was < 2, and is not valid")
					else:
						print("One of the inputs was not a valid positive integer")
				map = newMap(y,x)
				break
			elif user == "empty":
				while True:
					y = input("Enter the y: ")
					x = input("Enter the x: ")
					tileSize = input("Enter the tileSize: ")
					if y.isdigit() == True and x.isdigit() == True and tileSize.isdigit() == True:
						if int(tileSize) > 1:
							y = int(y)
							x = int(x)
							tileSize = int(tileSize)
							break
						else:
							print("The tileSize was < 2, and is not valid")
					else:
						print("One of the inputs was not a valid positive integer")
				map = newMap(y,x,True)
				break
			elif user == "gliderGun":
				while True:
					tileSize = input("Enter the tilesize: ")
					if tileSize.isdigit() == True:
						if int(tileSize) > 1:
							tileSize = int(tileSize)
							break
						else:
							print("The tileSize was < 2, and is not valid")
					else:
						print("Your input was not a valid positive integer")
				map = gliderGun()
				break
			elif user == "lwSpaceShip":
				while True:
					tileSize = input("Enter the tilesize: ")
					if tileSize.isdigit() == True:
						if int(tileSize) > 1:
							tileSize = int(tileSize)
							break
						else:
							print("The tileSize was < 2, and is not valid")
					else:
						print("Your input was not a valid integer")
				map = lwSpaceShip()
				break
			elif user == "test":
				tileSize = 25
				map = newMap()
				break
			elif user == "quit":
				FLAG = False
				FLAG2 = False
			else:
				print("Your input did not match one of the option")

		while FLAG2:
			if closed() == True:
				print("SimpleGraphics was closed")
				FLAG = False
				FLAG2 = False
			else:
				editMap(map,tileSize)
				if FLAG2 == True:
					map = runMap(map,tileSize)
			
main()
close()