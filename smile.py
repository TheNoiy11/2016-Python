from SimpleGraphics import *
from hsvTOrgb import *
from time import sleep

setAutoUpdate(False)
def smile(x,y,w,h,s,v):
	r,g,b = getRGB(h,s,v)
	setFill(r,g,b)
	if w > 0:
		ellipse(x,y,w,w)
		ellipse(x+0.2*w, y+0.2*w,0.2*w,0.2*w)
		ellipse(x+0.6*w, y+0.2*w,0.2*w,0.2*w)
		curve(x+0.3*w,y+0.7*w,x+0.5*w,y+0.8*w,x+0.7*w,y+0.7*w)