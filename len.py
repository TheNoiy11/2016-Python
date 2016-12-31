def lenList(list):
	if list == []:
		return 0
	return lenList(list[1:]) + 1
	
print(lenList([1,2,3,4,5,6,7]))

def sumList(list):
	if lenList(list) == 1:
		return list[0]
	return sumList(list[1:]) + list[0]
	
print(sumList([2,2,2,5]))

def addOne(list):
	if lenList(list) == 0:
		return []
	return (addOne(list[1:])).insert(0,list[0]+1)
	
print(addOne([1,1,1,1,1,1]))