from SimpleGraphics import *
from hsvTOrgb import *
resize(800,600)
x = -300
y = 300
Stretch = 3000

i = float(-0.1)
j = float(0.1)
while i <= 0.1 and i >= -0.1:
	j = 0.1
	while j >= 0.1 and j <= 0.5:
		reals = j
		imaginaries = i
		k = 0
		while k < 100:
			tempImag = imaginaries
			imaginaries = 2*reals*imaginaries + i
			reals = reals**2 + j - (tempImag**2)
			if ((reals)**2 + (imaginaries)**2)**0.5 > 2:
				r,g,b = getRGB(3*k,1,1)
				setColor(r,g,b)
				rect(j*Stretch + x - 1, i*Stretch + y - 1, 3,3)
				k = 100
			if k == 99:
				setColor(0,0,0)
				rect(j*Stretch + x - 1, i*Stretch + y - 1, 3,3)
			k = k + 1
		j = j + 0.00025
	i = i + 0.00025	
print("Drawing complete")