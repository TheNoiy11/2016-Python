from SimpleGraphics import *
x = -200
y = 500
Stretch = 1250

i = float(-0.25)
j = float(-0.24)
while i <= -0.25 and i >= 0:
	j = 0.245
	while j >= 0.245 and j <= 0.50:
		reals = j
		imaginaries = i
		k = 0
		while k < 100:
			tempImag = imaginaries
			imaginaries = 2*reals*imaginaries + i
			reals = reals**2 + j - (tempImag**2)
			if ((reals)**2 + (imaginaries)**2)**0.5 > 2:
				setColor(100,255-(2*k),255-(2*k))
				rect(j*Stretch + x - 1, i*Stretch + y - 1, 3,3)
				k = 100
			if k == 99:
				setColor(0,0,0)
				rect(j*Stretch + x - 1, i*Stretch + y - 1, 3,3)
			k = k + 1
		j = j + 0.001
	i = i + 0.001
setColor(0,255,0)
line(0,y+(-0.25*Stretch), 799, y+(-0.25*Stretch))
line(0,y+(0.25*Stretch), 799, y+(0.25*Stretch))

setColor(255,0,0)
line(x, 0, x, 599)
line(0, y, 799, y)

print("Drawing complete")