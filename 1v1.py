from SimpleGraphics import *
from time import sleep

resize(500,500)
setAutoUpdate(False)

pOne = [100,250,'ONE']
pTwo = [400,250,'TWO']
pSize = 10

def getNextPos(player):
	heldKeys = getHeldKeys()
	if player[2] == 'ONE':
		if 'w' in heldKeys:
			player[1] += -1
		if 's' in heldKeys:
			player[1] += 1
		if 'a' in heldKeys:
			player[0] += -1
		if 'd' in heldKeys:
			player[0] += 1
	elif player[2] == 'TWO':
		if 'i' in heldKeys:
			player[1] += -1
		if 'k' in heldKeys:
			player[1] += 1
		if 'j' in heldKeys:
			player[0] += -1
		if 'l' in heldKeys:
			player[0] += 1
	return player

while not closed():
	clear()
	
	setColor(0,0,0)
	ellipse(pOne[0] - pSize/2, pOne[1] - pSize/2,pSize,pSize)
	setColor(255,255,255)
	ellipse(pTwo[0] - pSize/2, pTwo[1] - pSize/2,pSize,pSize)
	
	pOne = getNextPos(pOne)
	pTwo = getNextPos(pTwo)

	update()
	sleep(0.005)