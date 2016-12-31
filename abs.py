from random import randint


#QUESTION 1
def abs(flo):
	if flo < 0:
		return flo * -1
	return flo

#QUESTION 3
def squareList(list):
	finalList = []
	for i in list:
		if i % 2 == 0:
			finalList.insert(0,i**2)
	return finalList

print(squareList([1,2,3,4,5,6,7,8,9,10]))

#QUESTION 4
def upStrList(string):
	finalList = []
	string = string.strip(".!?").split()
	for word in string:
		for ch in word:
			if ch.upper() == ch:
				finalList.append(word)
				break
	return finalList
	
print(upStrList("This is a Good question?"))

def upStrList2(string):
	finalList = []
	string = string.strip(".!?").split()
	for word in string:
		if word.lower() != word:
			finalList.append(word)
	return finalList
	
print(upStrList2("This is a Good question?"))
#QUESTION 5
w = int(input("Enter an amount of rows: "))
x = int(input("Enter an amount of elements per row: "))
y = int(input("Enter one end of the range: "))
z = int(input("Enter the other end of the range: "))

if y < z:
	firstNum = y
	secondNum = z
else:
	firstNum = z
	secondNum = y
	
finalList = []
for rows in range(w):
	nextRow = []
	for i in range(x):
		nextRow.append(randint(firstNum,secondNum))
	finalList.append(nextRow)
print(finalList)