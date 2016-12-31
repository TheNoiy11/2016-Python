from SimpleGraphics import *
x = 575
y = 300
Stretch = 275

i = float(-1.2)
j = float(-2)
while i <= 1.2 and i >= -1.2:
	j = -2
	while j >= -2 and j <= 0.7:
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
		j = j + 0.01
	i = i + 0.01
setColor(0,255,0)
line(0,y+(-1*Stretch), 799, y+(-1*Stretch))
line(0,y+(1*Stretch), 799, y+(1*Stretch))

line(x+(0.25*Stretch), 0, x+(0.25*Stretch), 599)
line(x+(-2*Stretch), 0, x+(-2*Stretch), 599)

setColor(255,0,0)
line(x, 0, x, 599)
line(0, y, 799, y)

setColor(0,0,255)
setFont("Times", "11", "bold italic")
text(x,y+(-1*Stretch),"1i")
text(x,y+(1*Stretch),"-1i")
text(x+(0.25*Stretch),y+(-1*Stretch),"1/4")
text(x+(-2*Stretch), y+(-1*Stretch), "-2")
print("Drawing complete")