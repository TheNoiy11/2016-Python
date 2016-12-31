from SimpleGraphics import *

setAutoUpdate(False)
img = loadImage("test.png")

width = getWidth(img)
height = getHeight(img)

resize(width*4,height)

rgbImage = createImage(width,height)
redImage = createImage(width,height)
greenImage = createImage(width,height)
blueImage = createImage(width,height)

for column in range(width):
	for row in range(height):
		r, g, b = getPixel(img, column, row)
		putPixel(rgbImage, column, row, r, g, b)
		putPixel(redImage, column, row, r, 0, 0)
		putPixel(greenImage, column, row, 0, g, 0)
		putPixel(blueImage, column, row, 0, 0, b)
	clear()
	drawImage(rgbImage,0,0)
	drawImage(redImage,width,0)
	drawImage(greenImage,width*2,0)
	drawImage(blueImage,width*3,0)
	update()