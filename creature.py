from SimpleGraphics import *
from random import randint, choice
from math import fabs, atan, cos, sin, degrees, radians
from time import sleep
from copy import deepcopy
resize(500,500)
setAutoUpdate(False)

class creature:
	
	def __init__(self, type = "CREATURE", name = "NAME", size = 10, health = 100, speed = 1, xPos = 0.0, yPos = 0.0):
		self.__type = type
		self.__name = name
		self.__health = health
		self.__speed = speed
		self.__xPos = xPos
		self.__yPos = yPos
		self.__size = size
		
	def getType(self):
		return self.__type
	def getName(self):
		return self.__name
	def getSize(self):
		return self.__size
	def getHealth(self):
		return self.__health
	def getSpeed(self):
		return self.__speed
	def getxPos(self):
		return self.__xPos
	def getyPos(self):
		return self.__yPos
	
	def setType(self, user):
		self.__type = user
	def setName(self, user):
		self.__name = user
	def setSize(self, user):
		self.__size = user
	def setHealth(self, user):
		self.__health = user
	def setSpeed(self,user):
		self.__speed = user
	def setxPos(self, user):
		self.__xPos = user
	def setyPos(self, user):
		self.__yPos = user
		
	def moveTowards(self,x,y):
		tempX = (self.__xPos - x)
		tempY = (self.__yPos - y)
		if tempX == 0:
			angle = radians(90)
		else:
			angle = fabs(atan(tempY/tempX))
		
		if self.__xPos > x:
			self.__xPos -= cos(angle)*self.__speed
		elif self.__xPos < x:
			self.__xPos += cos(angle)*self.__speed

		if self.__yPos > y:
			self.__yPos -= sin(angle)*self.__speed
		elif self.__yPos < y:
			self.__yPos += sin(angle)*self.__speed
			
class player:
	
	def __init__(self, size = 10, health = 100, speed = 2, xPos = 250, yPos = 250, gun = "Assault Rifle"):
		self.__health = health
		self.__speed = speed
		self.__xPos = xPos
		self.__yPos = yPos
		self.__size = size
		self.__gun = gun
		
	def getSize(self):
		return self.__size
	def getHealth(self):
		return self.__health
	def getSpeed(self):
		return self.__speed
	def getxPos(self):
		return self.__xPos
	def getyPos(self):
		return self.__yPos
	def getGun(self):
		return self.__gun
		
	def setSize(self, user):
		self.__size = user
	def setHealth(self, user):
		self.__health = user
	def setSpeed(self, user):
		self.__speed = user
	def setxPos(self, user):
		self.__xPos = user
	def setyPos(self, user):
		self.__yPos = user
	def setGun(self, user):
		self.__gun = user
		
	def move(self):
		heldKeys = getHeldKeys()
		if 'w' in heldKeys:
			self.__yPos += -1 * self.__speed
		if 's' in heldKeys:
			self.__yPos += 1 * self.__speed
		if 'a' in heldKeys:
			self.__xPos += -1 * self.__speed
		if 'd' in heldKeys:
			self.__xPos += 1 * self.__speed
		
		if self.__xPos > 500:
			self.__xPos = 500
		elif self.__xPos < 0:
			self.__xPos = 0
		if self.__yPos > 500:
			self.__yPos = 500
		elif self.__yPos < 0:
			self.__yPos = 0

class bullet:
	
	def __init__(self, type = "Assault Rifle", speed = 10, size = 3, xPos = 250, yPos = 250, xTarget = 250, yTarget = 250, angleMod = 0, damage = 10, penetrationMax = 1, infinitePenetrate = False, chase = False, target = 0):
		self.__speed = speed
		self.__type = type
		self.__size = size
		self.__xPos = xPos
		self.__yPos = yPos
		self.__xTarget = xTarget
		self.__yTarget = yTarget
		self.__deltaX = 0
		self.__deltaY = 0
		self.__angleMod = angleMod
		self.__damage = damage
		self.__penetrationCount = 0
		self.__penetrationMax = penetrationMax
		self.__infinitePenetrate = infinitePenetrate
		self.__angle = 0
		self.__chase = chase
		self.__target = target
		
		tempX = (self.__xPos - self.__xTarget)
		tempY = (self.__yPos - self.__yTarget)
		if tempX == 0:
			if tempY > 0:
				self.__angle = radians(-90)
			elif tempY < 0:
				self.__angle = radians(-90)
		else:
			self.__angle = (atan(tempY/tempX))
		
		self.__angle += radians(self.__angleMod)
		
		if tempX > 0:
			self.__deltaX = cos(self.__angle)*self.__speed*-1
			self.__deltaY = sin(self.__angle)*self.__speed*-1
		elif tempX < 0:
			self.__deltaX = cos(self.__angle)*self.__speed
			self.__deltaY = sin(self.__angle)*self.__speed
		else:
			if tempY > 0:
				self.__deltaY = sin(self.__angle)*self.__speed
				self.__deltaX = cos(self.__angle)*self.__speed
			elif tempY < 0:
				self.__deltaY = sin(self.__angle)*self.__speed*-1
				self.__deltaX = cos(self.__angle)*self.__speed*-1

	def getType(self):
		return self.__type
	def getSpeed(self):
		return self.__speed
	def getSize(self):
		return self.__size
	def getxPos(self):
		return self.__xPos
	def getyPos(self):
		return self.__yPos
	def getxTarget(self):
		return self.__xTarget
	def getyTarget(self):
		return self.__yTarget
	def getDamage(self):
		return self.__damage
	def getPenetraionCount(self):
		return self.__penetrationCount
	def getPenetraionMax(self):
		return self.__penetrationMax
	def getChase(self):
		return self.__chase
	def getTarget(self):
		return self.__target
		
	def setSpeed(self,user):
		self.__speed = user
	def setSize(self,user):
		self.__size = user
	def setxPos(self,user):
		self.__xPos = user
	def setyPos(self,user):
		self.__yPos = user
	def setxTarget(self,user):
		self.__xTarget = user
	def setyTarget(self,user):
		self.__yTarget = user
	def setDamage(self, user):
		self.__damage = user
	def setChase(self, user):
		self.__chase = user
		
	def addPenetrationCount(self):
		if self.__infinitePenetrate == False:
			self.__penetrationCount += 1
	
	def moveTowards(self, x, y):
		tempX = (self.__xPos - x)
		tempY = (self.__yPos - y)
		if tempX == 0:
			angle = radians(90)
		else:
			angle = fabs(atan(tempY/tempX))
		
		if self.__xPos > x:
			self.__xPos -= cos(angle)*self.__speed
		elif self.__xPos < x:
			self.__xPos += cos(angle)*self.__speed

		if self.__yPos > y:
			self.__yPos -= sin(angle)*self.__speed
		elif self.__yPos < y:
			self.__yPos += sin(angle)*self.__speed

	def move(self):
		self.__xPos += self.__deltaX
		self.__yPos += self.__deltaY

def createCreatures(amount, size = 10):
	creatures = []
	names = ["Brian", "Virginia", "Razi", "Matt", "Koko", "Bob", "Bill", "Fred"]
	types = ["Zombie", "Ghost", "Vampire"]
	
	for i in range(amount):
		creatures.append(creature(type = choice(types), name = choice(names), size = size, xPos = randint(0,500), yPos = randint(0,500)))
	
	for creat in creatures:
		if creat.getType() == "Zombie":
			creat.setSpeed(1)
			creat.setHealth(150)
		
		elif creat.getType() == "Ghost":
			creat.setSpeed(2)
			creat.setHealth(50)
		
		elif creat.getType() == "Vampire":
			creat.setSpeed(1.25)
			creat.setHealth(100)
			
	return creatures

def getRandomAngle(amount):
	return randint(amount*-1,amount)

def main():
	background(145,105,62)
	mouseControl = True
	PLAYER = player()
	
	creatureAmount = 5
	creatureSize = 25
	
	creatures = createCreatures(creatureAmount, creatureSize)
	bullets = []
	
	shotgunCooldown = 0
	assaultRifleCooldown = 0
	sniperCooldown = 0
	OPcooldown = 0
	weirdCooldown = 0
	FLAG = True
	
	shotgunAmmo = 2500
	assaultRifleAmmo = 100000
	sniperAmmo = 1000
	
	cursorX = 260
	cursorY = 250
	while not closed():
		clear()
		setFont("Times", "8")
		if mouseControl:
			cursorX = mouseX()
			cursorY = mouseY()
		else:
			heldKeys = getHeldKeys()
			if 'Up' in heldKeys:
				cursorY += -2
			if 'Down' in heldKeys:
				cursorY += 2
			if 'Left' in heldKeys:
				cursorX += -2
			if 'Right' in heldKeys:
				cursorX += 2
			
			if cursorX > 500:
				cursorX = 500
			elif cursorX < 0:
				cursorX = 0
			if cursorY > 500:
				cursorY = 500
			elif cursorY < 0:
				cursorY = 0
			setColor(0,255,255)
			ellipse(cursorX - 2, cursorY - 2, 4, 4)
			line(PLAYER.getxPos(), PLAYER.getyPos(), cursorX, cursorY)

		if creatures == []:
			creatureAmount += 15
			creatures  = createCreatures(creatureAmount, creatureSize)
		
		setOutline(0,0,0)
		setFill(255,0,255)
		PLAYER.move()
		ellipse(PLAYER.getxPos()- PLAYER.getSize()/2, PLAYER.getyPos() - PLAYER.getSize()/2, PLAYER.getSize(), PLAYER.getSize())
		text(PLAYER.getxPos(), PLAYER.getyPos() + PLAYER.getSize()/2, PLAYER.getGun(),"n")
		
		if '1' in getHeldKeys():
			PLAYER.setGun("Assault Rifle")
		elif '2' in getHeldKeys():
			PLAYER.setGun("Shotgun")
		elif '3' in getHeldKeys():
			PLAYER.setGun("Sniper")
		elif '4' in getHeldKeys():
			PLAYER.setGun('OP')
		elif '5' in getHeldKeys():
			PLAYER.setGun('Weird')
		
		if leftButtonPressed() or 'space' in getHeldKeys():
			if PLAYER.getGun() == "Assault Rifle" and assaultRifleCooldown < 1 and assaultRifleAmmo > 0:
				bullets.append(bullet(xPos = PLAYER.getxPos(), yPos = PLAYER.getyPos(), xTarget = cursorX, yTarget = cursorY, angleMod = getRandomAngle(3), damage = 10, penetrationMax = 1))
				assaultRifleCooldown += 2
				assaultRifleAmmo -= 1
			elif PLAYER.getGun() == "Shotgun" and shotgunCooldown < 1 and shotgunAmmo > 0:
				for i in range(6):
					bullets.append(bullet(xPos = PLAYER.getxPos(), yPos = PLAYER.getyPos(), xTarget = cursorX, yTarget = cursorY, angleMod = getRandomAngle(5), damage = 20, penetrationMax = 3))
				shotgunCooldown += 15
				shotgunAmmo -= 1
			elif PLAYER.getGun() == "Sniper" and sniperCooldown < 1 and sniperAmmo > 0:
				bullets.append(bullet(speed = 25, xPos = PLAYER.getxPos(), yPos = PLAYER.getyPos(), xTarget = cursorX, yTarget = cursorY, damage = 50, penetrationMax = 10))
				sniperCooldown += 50
				sniperAmmo -= 1
			elif PLAYER.getGun() == "OP" and OPcooldown < 1:
				for i in range(0,360,25):
					bullets.append(bullet(speed = 10, xPos = PLAYER.getxPos(), yPos = PLAYER.getyPos(), xTarget = cursorX, yTarget = cursorY, angleMod = i+getRandomAngle(25), damage = 150, infinitePenetrate = True))
				#OPcooldown += 100
			elif PLAYER.getGun() == "Weird" and weirdCooldown < 1 and FLAG:
				bullets.append(bullet(speed = 10, xPos = PLAYER.getxPos(), yPos = PLAYER.getyPos(), xTarget = creatures[0].getxPos(), yTarget = creatures[0].getxPos(), damage = 150, infinitePenetrate = True, chase = True))
				FLAG = False
		nextBullets = []
		for bull in bullets:
			if bull.getChase():
				bull.moveTowards(creatures[bull.getTarget()].getxPos(), creatures[bull.getTarget()].getyPos())
			else:
				bull.move()
			setColor(255,255,0)
			ellipse(bull.getxPos() - bull.getSize()/2, bull.getyPos() - bull.getSize()/2, bull.getSize(), bull.getSize())
			if not bull.getxPos() > 500 and not bull.getxPos() < 0 and not bull.getyPos() > 500 and not bull.getyPos() < 0:
				nextBullets.append(bull)
		bullets = deepcopy(nextBullets)

		nextCreatures = []
		
		for new in creatures:
			if new.getType() == "Zombie":
				setOutline(0,75,0)
				setFill(0,255,0)
			elif new.getType() == "Ghost":
				setOutline(75,75,75)
				setFill(255,255,255)
			elif new.getType() == "Vampire":
				setOutline(255,0,0)
				setFill(0,0,0)
			
			new.moveTowards(PLAYER.getxPos(),PLAYER.getyPos())
			nextBullets = []
			for bull in bullets:
				if bull.getxPos() > new.getxPos() - new.getSize()/2 and bull.getxPos() < new.getxPos() + new.getSize()/2 and bull.getyPos() > new.getyPos() - new.getSize()/2 and bull.getyPos() < new.getyPos() + new.getSize()/2:
					new.setHealth(new.getHealth() - bull.getDamage())
					if bull.getPenetraionCount() < bull. getPenetraionMax():
						bull.addPenetrationCount()
						nextBullets.append(bull)
				else:
					nextBullets.append(bull)
			bullets = deepcopy(nextBullets)
			
			if new.getHealth() > 0:
				nextCreatures.append(new)
			ellipse(new.getxPos() - new.getSize()/2, new.getyPos()- new.getSize()/2, new.getSize(), new.getSize())
			text(new.getxPos(), new.getyPos() - new.getSize()/2, new.getName(),"s")
			text(new.getxPos(), new.getyPos() + new.getSize()/2, new.getHealth(),"n")
		creatures = deepcopy(nextCreatures)
		
		if shotgunCooldown > 0:
			shotgunCooldown -= 1
		if assaultRifleCooldown > 0:
			assaultRifleCooldown -= 1
		if sniperCooldown > 0:
			sniperCooldown -= 1
		if weirdCooldown > 0:
			weirdCooldown -= 1
		if OPcooldown > 0:
			OPcooldown -= 1
			
		setColor(0,0,0)
		setFont("Times", "12")
		text(10,10, "Assault Rifle" + ": " + str(assaultRifleAmmo), "nw")
		text(10,25, "Shotgun" + ": " + str(shotgunAmmo), "nw")
		text(10,40, "Sniper" + ": " + str(sniperAmmo), "nw")
		update()
		sleep(0.01)
		
main()