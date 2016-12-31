from SimpleGraphics import *
from angles import *
from math import degrees, radians, sin, cos
from time import sleep

resize(750,750)
setAutoUpdate(False)
class path:
	
	def __init__(self, points = []):
		self.__points = points
		
	def draw(self):
		setColor(0,0,0)
		for i in range(len(self.__points) - 1):
			line(self.__points[i][0], self.__points[i][1], self.__points[i + 1][0], self.__points[i + 1][1])
			
class bloon:
	
	def __init__(self, level = 0, pos = [0,250]):
		self.__level = level
		self.__pos = pos
		
	def draw(self):
		if self.__level == 0:
			setColor(255,0,0)
			ellipse(self.__pos[0]-4, self.__pos[1]-4, 8, 8)
			
	def move(self, x, y):
		if self.__level == 0:
			self.__pos[0] += cos(getAngle(self.__pos[0], self.__pos[1], x, y))*0.1
			self.__pos[1] += sin(getAngle(self.__pos[0], self.__pos[1], x, y))*0.1
			
class level:
	
	def __init__(self, stage = 1):
		self.__stage = stage
		self.__bloons = []
		if self.__stage == 1:
			self.__path = [(0,250), (100,100), (150,350), (350,150), (750,550)]
			for i in range(10):
				self.__bloons.append(bloon(0, (self.__path[0][0], self.__path[0][1])))
		
def main():
	path1 = path()
	bloon1 = bloon()

main()