from SimpleGraphics import *
from random import randint

setAutoUpdate(False)

xWindow = 600
yWindow = 600
resize(xWindow,yWindow)

rect(200,200,200,100)

while not closed():
	mX = mouseX()
	mY = mouseY()
	if not mX < 0 and not mX > xWindow and not mY < 0 and not mY > yWindow:
		if not mX < 200 and not mX > 400 and not mY < 200 and not mY > 300:
			if leftButtonPressed() == True:
				r = randint(0,255)
				g = randint(0,255)
				b = randint(0,255)
				setColor(r,g,b)
				clear()
				rect(200,200,200,100)
				update()