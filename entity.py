from SimpleGraphics import *
from math import sin, cos, atan, radians, degrees
from time import sleep
from random import randint
		
class grapple:
		
	def __init__(self, x = 375, y = 375, radius = 3, speed = 5, angle = 0, color = (255,0,0)):
		self.__x = x
		self.__y = y
		self.__radius = radius
		self.__speed = speed
		self.__angle = radians(angle)
		self.__dx = cos(self.__angle) * self.__speed
		self.__dy = sin(self.__angle) * self.__speed
		self.__color = color
	def x(self):
		return self.__x
	def y(self):
		return self.__y

	def setColor(self, r, g, b):
		self.__color = (r,g,b)
		
	def draw(self):
		setFill(self.__color[0], self.__color[1], self.__color[2])
		ellipse(self.__x - self.__radius, self.__y - self.__radius, self.__radius*2, self.__radius*2)
		
	def move(self):
		global borders
		if self.__x + self.__dx > borders[1]:
			self.__x = borders[1]
		elif self.__x + self.__dx < borders[0]:
			self.__x = borders[0]
		else:
			self.__x += self.__dx
		
		if self.__y + self.__dy > borders[1]:
			self.__y = borders[1]
		elif self.__y + self.__dy < borders[0]:
			self.__y = borders[0]
		else:
			self.__y += self.__dy
			
class player:
		
	def __init__(self, x = 375, y = 375, radius = 5, speed = 1, angle = 0, color = (0,255,255)):
		self.__x = x
		self.__y = y
		self.__radius = radius
		self.__speed = speed
		self.__angle = radians(angle)
		self.__dx = cos(self.__angle) * self.__speed
		self.__dy = sin(self.__angle) * self.__speed
		self.__color = color
		self.__grapple = 0
		self.__attached = False
		
	def x(self):
		return self.__x
	def y(self):
		return self.__y
	def radius(self):
		return self.__radius
	def angle(self):	
		return self.__angle
	
	def draw(self):
		setFill(self.__color[0], self.__color[1], self.__color[2])
		ellipse(self.__x - self.__radius, self.__y - self.__radius, self.__radius*2, self.__radius*2)
	
	def move(self):
		if self.__x + self.__dx > borders[1]-self.__radius:
			self.__x = borders[1]-self.__radius
		elif self.__x + self.__dx < borders[0]+self.__radius:
			self.__x = borders[0]+self.__radius
		else:
			self.__x += self.__dx
		
		if self.__y + self.__dy > borders[1]-self.__radius:
			self.__y = borders[1]-self.__radius
		elif self.__y + self.__dy < borders[0]+self.__radius:
			self.__y = borders[0]+self.__radius
		else:
			self.__y += self.__dy
			
	def changeDirection(self):
		if not self.__attached:
			heldKeys = getHeldKeys()
			if 'w' in heldKeys and 'd' in heldKeys:
				self.__angle = radians(-45)
				self.__dx = cos(self.__angle) * self.__speed
				self.__dy = sin(self.__angle) * self.__speed
			elif 'w' in heldKeys and 'a' in heldKeys:
				self.__angle = radians(-135)
				self.__dx = cos(self.__angle) * self.__speed
				self.__dy = sin(self.__angle) * self.__speed
			elif 's' in heldKeys and 'd' in heldKeys:
				self.__angle = radians(45)
				self.__dx = cos(self.__angle) * self.__speed
				self.__dy = sin(self.__angle) * self.__speed
			elif 's' in heldKeys and 'a' in heldKeys:
				self.__angle = radians(135)
				self.__dx = cos(self.__angle) * self.__speed
				self.__dy = sin(self.__angle) * self.__speed
			elif 'w' in heldKeys and not 's' in heldKeys:
				self.__angle = radians(-90)
				self.__dx = cos(self.__angle) * self.__speed
				self.__dy = sin(self.__angle) * self.__speed
			elif 's' in heldKeys and not 'w' in heldKeys:
				self.__angle = radians(90)
				self.__dx = cos(self.__angle) * self.__speed
				self.__dy = sin(self.__angle) * self.__speed
			elif 'd' in heldKeys and not 'a' in heldKeys:
				self.__angle = radians(0)
				self.__dx = cos(self.__angle) * self.__speed
				self.__dy = sin(self.__angle) * self.__speed
			elif 'a' in heldKeys and not 'd' in heldKeys:
				self.__angle = radians(180)
				self.__dx = cos(self.__angle) * self.__speed
				self.__dy = sin(self.__angle) * self.__speed
			else:
				self.__dx = 0
				self.__dy = 0
	
	def isGrappling(self):
		if self.__grapple == 0:
			return False
		else:
			return True
			
	def stopGrappling(self):
		self.__grapple = 0
		self.__attached = False
		self.__speed = 1
	
	def newGrapple(self):
		tempAngle = getAngle(self.__x, self.__y, mouseX(), mouseY())
		self.__grapple = grapple(self.__x + cos(tempAngle)*self.__radius, self.__y + sin(tempAngle)*self.__radius, 3, 3, degrees(tempAngle), (255,0,0))
	
	def grapple(self):
		tempAngle = getAngle(self.__x, self.__y, self.__grapple.x(), self.__grapple.y())
		if self.__grapple.x() in borders or self.__grapple.y() in borders:
			self.__grapple.setColor(0,255,0)
			self.__attached = True
			self.__speed = 2
			self.__angle = getAngle(self.__x, self.__y, self.__grapple.x(), self.__grapple.y())

			self.__dx = cos(self.__angle) * self.__speed
			self.__dy = sin(self.__angle) * self.__speed
			self.__grapple.draw()
			line(self.__x + cos(tempAngle)*self.__radius, self.__y + sin(tempAngle)*self.__radius, self.__grapple.x(), self.__grapple.y())
		else:
			self.__grapple.setColor(255,0,0)
			self.__attached = False
			self.__speed = 1
			self.__grapple.move()
			self.__grapple.draw()
			line(self.__x + cos(tempAngle)*self.__radius, self.__y + sin(tempAngle)*self.__radius, self.__grapple.x(), self.__grapple.y())

def drawBorders():
	global borders
	line(borders[0],borders[0],borders[0],borders[1])
	line(borders[0],borders[0],borders[1],borders[0])
	line(borders[1],borders[1],borders[0],borders[1])
	line(borders[1],borders[1],borders[1],borders[0])
		
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

def main():
	global borders
	pOne = player()
	while not closed():
		clear()
		drawBorders()
		
		pOne.draw()
		pOne.move()
		pOne.changeDirection()
		
		if leftButtonPressed():
			if not pOne.isGrappling():
				pOne.newGrapple()
			else:
				pOne.grapple()
		elif pOne.isGrappling():
			pOne.stopGrappling()
		
		update()
		
setAutoUpdate(False)
resize(750,750)
borders = [150,600]
main()