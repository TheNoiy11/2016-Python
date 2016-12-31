#
#Name: Brian LeBlanc
#Student Number: 101042929
#
#Gaddis, T. (2015). “Starting Out With Python”
#
from SimpleGraphics import *

setAutoUpdate(False)
img = loadImage("test.png")

width = getWidth(img)
height = getHeight(img)

new = createImage(width,height)
newInverse = createImage(width, height)

left = getWidth()/2 - width/2
top = getHeight()/2 - height/2
for column in range(width):
	for row in range(height):
		r, g, b = getPixel(img, column, row)
		putPixel(new, column, row, r, g, b)
		putPixel(newInverse, column, row, 255-r, 255-g, 255-b)
	clear()
	drawImage(new, left-width/2,top)
	drawImage(newInverse, left+width/2,top)
	update()