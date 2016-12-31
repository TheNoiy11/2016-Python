from math import atan, radians

def getDistance(x1, y1, x2, y2):
	return ((x1-x2)**2 + (y1-y2)**2)**0.5
	
def getAngle(x1, y1, x2, y2):
	if x2 - x1 > 0:
		return atan( (y2-y1)/(x2-x1) )
	elif x2 - x1 < 0:
		return atan( (y2-y1)/(x2-x1) ) + radians(180)
	elif x2 - x1 == 0:
		if y2 - y1 > 0:
			return radians(90)
		elif y2 - y1 < 0:
			return radians(-90)
		elif y2 - y1 == 0:
			return 0