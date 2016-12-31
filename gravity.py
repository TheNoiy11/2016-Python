from SimpleGraphics import *
from math import cos, sin, pi
from angles import *

resize(500,500)
background(0,0,0)

class vector:
	
	def __init__(self, xPos, yPos, angle, magnitude):
		self.__angle = angle
		self.__magnitude = magnitude
		self.__startx = xPos
		self.__starty = yPos
		self.__endx = cos(self.__angle)*self.__magnitude + self.__startx
		self.__endy = sin(self.__angle)*self.__magnitude + self.__starty
		
	def info(self):
		print("Starting coordinates: (", self.__startx, ", ", self.__starty, ")", sep="")
		print("Ending coordinates: (", self.__endx, ", ", self.__endy, ")",  sep="")
		print("Angle:", self.__angle)
		print("Magnitude:", self.__magnitude)

class celBody:
	
	def __init__(self):
		self.__xPos = 250
		self.__yPos = 250
		self.__radius = 5
		self.__mass = 100
		self.__color = (255,255,255)
		
	def show(self):
		setColor(self.__color[0], self.__color[1], self.__color[2])
		ellipse(self.__xPos-self.__radius, self.__yPos-self.__radius, self.__radius*2, self.__radius*2)
		
	def getMass(self):
		return self.__mass
def main():
	sun = celBody()
	while not closed():
		sun.show()
		
main()