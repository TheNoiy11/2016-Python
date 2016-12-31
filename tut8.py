'''
Name: Brian LeBlanc
Student Number: 101042929

Gaddis, T. (2015). “Starting Out With Python”
'''

#Question 1
def isRectangular(list):
	for i in range(len(list)):
		if len(list[0]) != len(list[i]):
			return False
	return True
print("********Question 1********")
print(isRectangular([[1,2],[1,2],[1,2]]))
print(isRectangular([[1,2],[1,2],[1]]))
print()

#Question 2
def isNumeric(list):
	for i in range(len(list)):
		for j in range(len(list[i])):
			if isinstance(list[i][j] , (int,float)) == False:
				return False
	return True
print("********Question 2********")
print(isNumeric([[1,2],[1.1,1]]))
print(isNumeric([[1,2],[1.1,"1"]]))
print()

#Question 3
def isMatrix(list):
	if isRectangular(list) == False or isNumeric(list) == False:
		return False
	return True
print("********Question 3********")
print(isMatrix([[1,1,1],[2,2,2],[3,3,3]]))
print(isMatrix([[1,1,1],[2,2],[3,3,3]]))
print()

#Question 4
def printMatrix(list):
	if isRectangular(list) == False or isNumeric(list) == False:
		print("Inputed list is not a matrix")
	else:
		for y in range(len(list)):
			print("| ", end = "")
			for x in range(len(list[y])):
				print(list[y][x], end = " ")
			print("|")
print("********Question 4********")
printMatrix([[1,1,1],[2,2,2],[3,3,3]])
printMatrix([[1,1,1],[2,2],[3,3,3]])
printMatrix([[1,1,1],[2,2,2],[3,3,"3"]])
print()

#Question 5
def zeroMatrix(int):
	list = []
	for y in range(int):
		nextRow = []
		for x in range(int):
			nextRow.append(0)
		list.append(nextRow)
	return list
print("********Question 5********")
print(zeroMatrix(3))
printMatrix(zeroMatrix(4))
print()

#Question 6
def identityMatrix(int):
	list = []
	for y in range(int):
		nextRow = []
		for x in range(int):
			if x == y:
				nextRow.append(1)
			else:
				nextRow.append(0)
		list.append(nextRow)
	return list
print("********Question 6********")
print(identityMatrix(3))
printMatrix(identityMatrix(5))
print()

#Question 7
def sameSize(list1,list2):
	if isRectangular(list1) == False or isNumeric(list1) == False or isRectangular(list2) == False or isNumeric(list2) == False:
		print("One of the inputed lists is not a matrix")
	else:
		sizeList1 = (len(list1), len(list1[0]))
		sizeList2 = (len(list2), len(list2[0]))
		if sizeList1 == sizeList2:
			return True
		else:
			return False
print("********Question 7********")
print(sameSize([[1],[1],[1]],[[1],[1],[1]]))
print(sameSize([[1],[1],[1]],[[1],[1]]))
print()