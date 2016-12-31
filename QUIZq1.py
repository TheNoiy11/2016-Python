from random import randint

def q1(x):
	if x == int(x):
		return x
	else:
		return int(x//1 + 1)

def q3(list):
	returnList = []
	for char in list:
		if char.upper() == char:
			returnList.insert(0,ord(char))
	return returnList

print(q3(["H","e","l","L","o","W","o","r","l","D"]))

MORSE_KEY = {'.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f','--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l','--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r','...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x','-.--':'y','--..':'z'}
def q4(string):
	global MORSE_KEY
	returnString = ""
	string = string.strip("{}").split()
	for char in string:
		returnString = returnString + MORSE_KEY[char]
	return returnString

test = "{-... .-. .. .- -.}"
print(test)
print(q4(test))

def q5(x,y,z):
	x = x.strip().replace(","," ").split()
	evenList = []
	for i in range(len(x)):
		x[i] = int(x[i])
		if x[i] % 2 == 0:
			evenList.append(x[i])
	finalList = []
	for i in range(y):
		nextRow = []
		for j in range(z):
			nextNum = randint(0,len(evenList)-1)
			nextRow.append(evenList[nextNum])
		finalList.append(nextRow)
	return finalList

print(q5("1,2,3,4,5,6,7,8,9,10,11,12",2,6))