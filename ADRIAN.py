from SimpleGraphics import *
from random import *
from smile import *
resize(1080,300)

setAutoUpdate(False)
while not closed():
	clear()
	for i in range(0,100,10):
		for j in range(0,360,10):
			h = randint(0,359)
			s = (randint(25,100))/100
			v = (randint(25,100))/100
			smile(j*3 + 1,i*3 + 1,30, h,s,v)
	update()
print("DONE")