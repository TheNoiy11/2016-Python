from SimpleGraphics import *
x = 400
y = 300
Stretch = 175

i = float(-2)
j = float(-2)
checks = 0
while i <= 2 and i >= -2:
	j = -2
	while j >= -2 and j <= 2:
		reals = j
		imaginaries = i
		k = 0
		while k < 50:
			tempImag = imaginaries
			tempReals = reals
			
			imaginaries = (-4)*(tempReals**3)*tempImag - (4)*tempReals*(tempImag**3) + (2)*i*j
			reals = (tempReals**4)*(tempImag**4) - (2)*(tempReals**2)*(tempImag**2) - (j**2) - (i**2)
			if ((reals)**2 + (imaginaries)**2)**0.5 > 2:
				setColor(100,255-(5*k),255-(5*k))
				rect(j*Stretch + x - 1, i*Stretch + y - 1, 3,3)
				k = 50
			if k == 49:
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