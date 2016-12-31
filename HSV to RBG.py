###Converts HSV values into RGB

h = 0
s = 1
v = 1
m = v-c

temp = h/60 % 2 - 1

if temp < 0:
	temp = temp * (-1)
x = (c*(1 - temp))

if 0 <= h and h < 60:
	r = c
	g = x
	b = 0
elif 60 <= h and h < 120:
	r = x
	g = c
	b = 0
elif 120 <= h and h < 180:
	r = 0
	g = c
	b = x
elif 180 <= h and h < 240:
	r = 0
	g = x
	b = c
elif 240 <= h and h < 300:
	r = x
	g = 0
	b = c
elif 300 <= h and h < 360:
	r = c
	g = 0
	b = x

r = int((r+m)*255)
g = int((g+m)*255)
b = int((b+m)*255)