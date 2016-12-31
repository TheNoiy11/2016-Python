from SimpleGraphics import *
from hsvTOrgb import *
resize(1080,300)

setAutoUpdate(False)
for i in range(100):
	for j in range(360):
		r, g, b = getRGB(j,v=i/100)
		setColor(r,g,b)
		rect(j*3 + 1,i*3 + 1, 3, 3)
	update()
print("DONE")