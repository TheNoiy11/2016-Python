from SimpleGraphics import *
from time import sleep

r = 0
g = 0
b = 0

h1 = 0
s = 1
v = 1

c = s*v
size = 250
resize(size,size)
setAutoUpdate(False)
while not closed():
	setColor(r,g,b)
	h1 = h1 + 1
	if h1 > 359:
		h1 = 0
	h2 = h1/60
	temp = h2 % 2 - 1
	if temp < 0:
		temp = temp * (-1)
	x = (c*(1 - temp))
	if 0 <= h1 and h1 < 60:
		rtemp = c
		gtemp = x
		btemp = 0
	elif 60 <= h1 and h1 < 120:
		rtemp = x
		gtemp = c
		btemp = 0
	elif 120 <= h1 and h1 < 180:
		rtemp = 0
		gtemp = c
		btemp = x
	elif 180 <= h1 and h1 < 240:
		rtemp = 0
		gtemp = x
		btemp = c
	elif 240 <= h1 and h1 < 300:
		rtemp = x
		gtemp = 0
		btemp = c
	elif 300 <= h1 and h1 < 360:
		rtemp = c
		gtemp = 0
		btemp = x
	m = v-c
	
	r = int((rtemp+m)*255)
	g = int((gtemp+m)*255)
	b = int((btemp+m)*255)
	clear()
	rect(0,0,size,size)
	update()
	sleep(0.01)