from random import choice
from time import sleep

fileOpen = open("SMASHMOUTH.txt","r")
fileData = fileOpen.read()
fileOpen.close()

fileData = fileData.lower()

for char in ':;!?-*"':
	fileData = fileData.replace(char, "")

fileData = fileData.replace("\n", " * * ")
fileData = "* * " + fileData + " * *"
fileData = fileData.split()

dict = {}

for i in range(len(fileData)-2):
	pair = (fileData[i], fileData[i+1])
	next = fileData[i+2]
	if not pair in dict:
		dict[pair] = []
	dict[pair].append(next)

pair = ("*","*")
Final = []
while True:
	list = dict[(pair)]
	next = choice(list)
	if next != "*":
		Final.append(next)
	pair = (pair[1],next)
	if pair == ("*","*"):
		break

target = open("NEW.txt", 'w')
for i in range(len(Final)):
	print(Final[i], end = " ")
	target.write(Final[i])
	target.write(" ")
target.write("\n")
target.close()
print()