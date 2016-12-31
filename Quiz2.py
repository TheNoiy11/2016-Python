from random import randint

#QUESTION 1
def q1(x):
	if x == int(x):
		return x
	return int(x//1 + 1)

print(q1(5.1))

#QUESTION 3
def q3(list):
	returnList = []
	for char in list:
		if char.upper() == char:
			returnList.insert(0,ord(char))
	return returnList

print(q3(["H","e","l","L","o","W","o","r","l","D"]))

#QUESTION 4
MORSE_KEY = {'.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f','--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l','--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r','...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x','-.--':'y','--..':'z'}
def q4(string):
	global MORSE_KEY
	returnString = ""
	string = string.strip("{}").split()
	for char in string:
		returnString += MORSE_KEY[char]
	return returnString

test = "{.... . -.-- .... --- .-- ... .. - --. --- .. -. --.}"
print(test)
print(q4(test))

#QUESTION 5
x = (input("Enter a list: ")).split(",")
y = int(input("Enter an amount of rows: "))
z = int(input("Enter an amount of elements in each row: "))
evenList = []
for i in range(len(x)):
	x[i] = int(x[i])
	if x[i] % 2 == 0:
		evenList.append(x[i])
finalList = []
for i in range(y):
	nextRow = []
	for j in range(z):
		nextRow.append(evenList[randint(0,len(evenList)-1)])
	finalList.append(nextRow)
print(finalList)