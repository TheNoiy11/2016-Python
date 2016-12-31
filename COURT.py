from random import choice, randint
from time import sleep

def mrAllen():
	fileOpen = open("MrAllen.txt","r")
	fileData = fileOpen.read()
	fileOpen.close()
	
	fileData = fileData.lower()
		
	fileData = fileData.replace("\n", " * * ")
	fileData = "* * " + fileData + " * *"
	fileData = fileData.split()

	dict = {}
	returnString = ""
	for i in range(len(fileData)-2):
		pair = (fileData[i], fileData[i+1])
		next = fileData[i+2]
		if not pair in dict:
			dict[pair] = []
		dict[pair].append(next)
	
	pair = ("*","*")
	returnList = []
	while True:
		currentPair = dict[(pair)]
		nextWord = choice(currentPair)
		if nextWord != "*":
			returnList.append(nextWord)
		pair = (pair[1],nextWord)
		if pair == ("*","*"):
			break
	
	returnList[0] = returnList[0][0].upper() + returnList[0][1:]
	for i in range(len(returnList)):
		if i == 0:
			returnString = returnList[i]
		else:
			returnString = returnString + " " + returnList[i]
	return returnString
	
def theCourt():
	fileOpen = open("TheCourt.txt","r")
	fileData = fileOpen.read()
	fileOpen.close()
	
	fileData = fileData.lower()
		
	fileData = fileData.replace("\n", " * * ")
	fileData = "* * " + fileData + " * *"
	fileData = fileData.split()

	dict = {}
	returnString = ""
	for i in range(len(fileData)-2):
		pair = (fileData[i], fileData[i+1])
		next = fileData[i+2]
		if not pair in dict:
			dict[pair] = []
		dict[pair].append(next)
	
	pair = ("*","*")
	returnList = []
	while True:
		currentPair = dict[(pair)]
		nextWord = choice(currentPair)
		if nextWord != "*":
			returnList.append(nextWord)
		pair = (pair[1],nextWord)
		if pair == ("*","*"):
			break
	
	returnList[0] = returnList[0][0].upper() + returnList[0][1:]
	for i in range(len(returnList)):
		if i == 0:
			returnString = returnList[i]
		else:
			returnString = returnString + " " + returnList[i]
	return returnString

def main(num=5):
	newFile = open("newTxt.txt","w")
	for i in range(num):
		print("	THE COURT:", end= " ")
		newFile.write("THE COURT: ")
		
		while True:
			temp = theCourt()
			print(temp, end=" ")
			newFile.write(temp + " ")
			
			if randint(0,1) == 1:
				break
		
		print()
		newFile.write("\n")
		
		print("	MR ALLEN:", end= " ")
		newFile.write("MR ALLEN: ")
		while True:
			temp = mrAllen()
			print(temp, end= " ")
			newFile.write(temp + " ")
			
			if randint(0,1) == 1:
				break
		print()
		print()
		newFile.write("\n")
		newFile.write("\n")
	newFile.close()

main()