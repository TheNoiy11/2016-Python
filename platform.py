from SimpleGraphics import *
from time import sleep

resize(500,500)
setAutoUpdate(False)

class player:
	
	def __init__(self, pos = [250,250], size = 10, gravity = 9.81, timeInterval = 0.05, yVelocity = 0, xVelocity = 0, xAcceleration = 0):
		self.__x = pos[0]
		self.__y = pos[1]
		self.__size = size
		self.__gravity = gravity
		self.__timeInterval = timeInterval
		self.__yVelocity = yVelocity
		self.__xVelocity = xVelocity
		self.__xAcceleration = xAcceleration
		
	def getX(self):
		return self.__x
	def getY(self):
		return self.__y
	def getSize(self):
		return self.__size
		
	def setX(self, x):
		self.__x = x
	def setY(self, y):
		self.__y = y

	def jetpack(self):
		self.__yVelocity -= 1
	def goLeft(self):
		self.__xVelocity -= 1
	def goRight(self):
		self.__xVelocity += 1

	def move(self):
		self.__y += (self.__yVelocity*self.__timeInterval) + ((self.__gravity*self.__timeInterval)/2)
		self.__yVelocity = self.__yVelocity + (self.__gravity*self.__timeInterval)
		
		self.__x += (self.__xVelocity*self.__timeInterval) + ((self.__xAcceleration*self.__timeInterval)/2)
		self.__xVelocity = self.__xVelocity + (self.__xAcceleration*self.__timeInterval)

def drawPlayer(player = player()):
	size = player.getSize()
	rect(player.getX() - size/2, player.getY() - size/2, size, size)

def main():	
	PLAYER = player()
	while not closed():
		clear()
		if 'space' in getHeldKeys():
			PLAYER.jetpack()
		if 'a' in getHeldKeys():
			PLAYER.goLeft()
		if 'd' in getHeldKeys():
			PLAYER.goRight()
		
		if PLAYER.getX() > 500:
			PLAYER.setX(0)
		elif PLAYER.getX() < 0:
			PLAYER.setX(500)
		if PLAYER.getY() > 500:
			PLAYER.setY(0)
		elif PLAYER.getY() < 0:
			PLAYER.setY(500)
		PLAYER.move()
		drawPlayer(PLAYER)
		update()
		sleep(0.01)
main()