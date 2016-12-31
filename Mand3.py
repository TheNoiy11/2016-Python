from SimpleGraphics import *
x = 400
y = 300
Stretch = 145

tempReal = 0
tempImag = 0
i = float(-2)
j = float(-2)
while i <= 2 and i >= -2:
	j = -2
	while j <= 2 and j >= -2:
		real = j
		imag = i
		k = 0
		while k < 100:
			tempReal = real
			tempImag = imag
			real = (tempReal**5) - (12*(tempReal**3)*(tempImag**2)) + (5*tempReal*(tempImag**4)) + j
			imag = (tempImag**5) - (12*(tempReal**2)*(tempImag**3)) + (5*(tempReal**4)*(tempImag)) + i
			if ((real)**2 + (imag)**2)**0.5 > 2:
				setColor(100,255-(2*k),255-(2*k))
				rect(j*Stretch + x - 1, i*Stretch + y - 1, 3,3)
				k = 100
			if k == 99:
				setColor(0,0,0)
				rect(j*Stretch + x - 1, i*Stretch + y - 1, 3,3)
			k = k + 1
		j = j + 0.01
	i = i + 0.01
setColor(255,0,0)
line(x, 0, x, 599)
line(0, y, 799, y)

setColor(0,255,0)
line(0,y+(-1*Stretch), 799, y+(-1*Stretch))
line(0,y+(1*Stretch), 799, y+(1*Stretch))
line(0,y+(-2*Stretch), 799, y+(-2*Stretch))
line(0,y+(2*Stretch), 799, y+(2*Stretch))

line(x+(1*Stretch), 0, x+(1*Stretch), 599)
line(x+(-1*Stretch), 0, x+(-1*Stretch), 599)
line(x+(2*Stretch), 0, x+(2*Stretch), 599)
line(x+(-2*Stretch), 0, x+(-2*Stretch), 599)
print("Drawing complete")