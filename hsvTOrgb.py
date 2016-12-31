def getRGB(h,s=1,v=1):
	c = s*v
	m = v-c
	if h < 0 or h > 359:
		print("The given hue is not valid")
		return
	else:
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
		return r,g,b
def getR(h,s,v):
	if h < 0 or h > 359:
		print("The given hue is not valid")
		return
	else:
		c = s*v
		m = v-c
		temp = h/60 % 2 - 1
		if temp < 0:
			temp = temp * (-1)
		x = (c*(1 - temp))

		if 0 <= h and h < 60:
			r = c
		elif 60 <= h and h < 120:
			r = x
		elif 120 <= h and h < 180:
			r = 0
		elif 180 <= h and h < 240:
			r = 0
		elif 240 <= h and h < 300:
			r = x
		elif 300 <= h and h < 360:
			r = c
		r = int(round((r+m)*255))
		return r
def getG(h,s,v):
	if h < 0 or h > 359:
		print("The given hue is not valid")
		return
	else:
		c = s*v
		m = v-c
		temp = h/60 % 2 - 1
		if temp < 0:
			temp = temp * (-1)
		x = (c*(1 - temp))

		if 0 <= h and h < 60:
			g = x
		elif 60 <= h and h < 120:
			g = c
		elif 120 <= h and h < 180:
			g = c
		elif 180 <= h and h < 240:
			g = x
		elif 240 <= h and h < 300:
			g = 0
		elif 300 <= h and h < 360:
			g = 0
		g = int(round((g+m)*255))
		return g
def getB(h,s,v):
	c = s*v
	m = v-c
	if h < 0 or h > 359:
		print("The given hue is not valid")
		return
	else:
		temp = h/60 % 2 - 1
		if temp < 0:
			temp = temp * (-1)
		x = (c*(1 - temp))

		if 0 <= h and h < 60:
			b = 0
		elif 60 <= h and h < 120:
			b = 0
		elif 120 <= h and h < 180:
			b = x
		elif 180 <= h and h < 240:
			b = c
		elif 240 <= h and h < 300:
			b = c
		elif 300 <= h and h < 360:
			b = x
		b = int(round((b+m)*255))
		return b