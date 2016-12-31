from SimpleGraphics import *
from time import sleep
from random import randint
from math import sin, cos, atan, asin, acos, fabs, degrees

resize(500,500)
setAutoUpdate(False)

def checkPosition(map):
	for entity in map:
		if entity[0] > 500:
			entity[0] = 0
		if entity[1] > 500:
			entity[1] = 0
		if entity[0] < 0:
			entity[0] = 500
		if entity[1] < 0:
			entity[1] = 500
	return map

def drawMap(map,size = 10):
	for entity in map:
		if entity[2] == 'PLAYER':
			setColor(255,255,0)
		elif entity[2] == 'ZOMBIE':
			setColor(50,200,50)
		ellipse(entity[0] - (size/2), entity[1] - (size/2), size, size)

def moveZombies(map):
	for entity in map:
		if entity[2] == 'ZOMBIE':
			xComponent = (map[0][0] - entity[0])
			yComponent = (map[0][1] - entity[1])
			if xComponent == 0:
				playerAngle = 90
			else:
				playerAngle = fabs(degrees(atan(yComponent/xComponent)))
				
			if xComponent > 0:
				entity[0] = entity[0] + cos(playerAngle)*1.125
			else:
				entity[0] = entity[0] - cos(playerAngle)*1.125
				
			if yComponent > 0:
				entity[1] = entity[1] + sin(playerAngle)*1.125
			else:
				entity[1] = entity[1] - sin(playerAngle)*1.125
			
	return map
	
def entityGotowards(entity,x,y):
	print()
	
def main():
	map = [[250,250,'PLAYER','Alive']]
	for i in range(1):
		map.append([randint(0,500),randint(0,500),'ZOMBIE','Alive'])
	
	while not closed():
		clear()
		drawMap(moveZombies(checkPosition(map)))
		heldKeys = getHeldKeys()
		if 'w' in heldKeys:
			map[0][1] = map[0][1] - 1
		if 's' in heldKeys:
			map[0][1] = map[0][1] + 1
		if 'a' in heldKeys:
			map[0][0] = map[0][0] - 1
		if 'd' in heldKeys:
			map[0][0] = map[0][0] + 1
		
		if leftButtonPressed():
			setColor(0,0,0)
			line(map[0][0],map[0][1],mouseX(),mouseY())
			
		update()
		sleep(0.005)
		
main()