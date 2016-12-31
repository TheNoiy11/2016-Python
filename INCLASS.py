from SimpleGraphics import *
while not closed():
	print(getHeldKeys())
	if leftButtonPressed() == True:
		print(mouseX(),mouseY())
		rect(mouseX(),mouseY(),3,3)