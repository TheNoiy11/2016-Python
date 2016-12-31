from SimpleGraphics import *
from random import randint
from time import sleep

Alive = True
rows = 50
cols = 50

zoom = 10

score = 0
speed = 1

headX = rows//2
headY = cols//2
nextX = 0
nextY = 0

tailX = headX - 1
tailY = headY

coinX = randint(0,rows-1)
coinY = randint(0,rows-1)

direction = "u"

resize(rows*zoom,cols*zoom)
setAutoUpdate(False)
while not closed():
	while Alive:
		clear()
		setColor(0,127,0)
		for i in range(rows):
			for j in range(cols):
				rect(i*zoom,j*zoom,zoom,zoom)
		setColor(127,0,0)
		rect(coinX*zoom,coinY*zoom,zoom,zoom)
		setColor(127,255,0)
		rect(headX*zoom,headY*zoom,zoom,zoom)
		rect(tailX*zoom,tailY*zoom,zoom,zoom)
		
		update()
		sleep(speed)
		
		keys = getHeldKeys()
					
		nextX = headX
		nextY = headY
		if "Up" in keys:
			direction = "u"
		elif "Down" in keys:
			direction = "d"
		elif "Left" in keys:
			direction = "l"
		elif "Right" in keys:
			direction = "r"
		
		if direction == "u":
			nextY = nextY - 1
		if direction == "d":
			nextY = nextY + 1
		if direction == "l":
			nextX = nextX - 1
		if direction == "r":
			nextX = nextX + 1

		if headX < 0 or headX > cols or headY < 0 or headY > rows or (nextX == tailX and nextY == tailY):
			Alive = False
			for i in range(rows):
				for j in range(cols):
					r = randint(0,255)
					g = randint(0,255)
					b = randint(0,255)
					setColor(r,g,b)
					rect(i*zoom,j*zoom,zoom,zoom)
		else:
			tailX = headX
			tailY = headY
			headX = nextX
			headY = nextY
			if (headX == coinX and headY == coinY):
				coinX = randint(0,rows + 1)
				coinY = randint(0,cols + 1)
				speed = speed - 