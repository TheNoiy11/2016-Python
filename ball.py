from SimpleGraphics import *
from math import sin, cos, fabs
from random import randint, choice
from hsvTOrgb import *
from time import sleep

setAutoUpdate(False)
resize(500,500)
background(0,0,0)

class ball:
	def __init__(self, x = 250, y = 250, angle = randint(0,359), color = (255,255,255)):
		self.__x = x
		self.__y = y
		self.__speed = 3
		self.__angle = angle
		self.__dx = cos(self.__angle)*self.__speed
		self.__dy = sin(self.__angle)*self.__speed
		self.__size = 10
		self.__color = color
	
	def draw(self):
		setColor(self.__color[0],self.__color[1],self.__color[2])
		ellipse(self.__x - self.__size/2, self.__y - self.__size/2, self.__size, self.__size)
		text(self.__x, self.__y - 5, self.__speed, "s")
	
	def setSize(self, size):
		self.__size = size
	
	def setColor(self, r, g ,b):
		self.__color = (r,g,b)
		
	def setSpeed(self, new):
		self.__speed = new
	
	def getSpeed(self):
		return self.__speed
		
	def scaleSpeed(self, scale):
		self.__dx *= scale
		self.__dy *= scale
		self.__speed = fabs(((self.__dx)**2 + (self.__dy)**2)**0.5)

	def move(self):
		if self.__x + self.__dx < 0:
			self.__dx = -self.__dx
		elif self.__x + self.__dx > 500:
			self.__dx = -self.__dx
			
		if self.__y + self.__dy < 0:
			self.__dy = -self.__dy
		elif self.__y + self.__dy > 500:
			self.__dy = -self.__dy
		
		self.__x += self.__dx
		self.__y += self.__dy

h = 0
balls = []
speeds = [0.5,2.5]	
for i in range(200):
	balls.append(ball(randint(0,500), randint(0,500), randint(0,359), color = (randint(150,255), randint(150,255), randint(150,255))))
while not closed():
	clear()
	
	if h == 359:
		h = 0
	else:
		h += 1
	r, g, b = getRGB(h,0.5,0.5)
	background(r,g,b)
	
	if randint(0,10) == 0:
			choice(balls).scaleSpeed(choice(speeds))
	
	highest = ball()
	highest.setSpeed(0)
	for i in balls:
		if i.getSpeed() > highest.getSpeed():
			highest = i
		else:
			i.setColor(255,255,255)
	highest.setColor(255,0,0)
	highest.setSize(20)
	for i in balls:
		i.move()
		i.draw()
	update()
	sleep(0.01)