from random import randint
from time import time

def swap(list,i,j):
	
	temp = list[i]
	list[i] = list[j]
	list[j] = temp
	
	return list
	
def selectionSort(list):
	length = len(list)
	for i in range(length-1):
		nextSmallest = i
		for j in range(i+1, length):
			if list[j] < list[nextSmallest]:
				nextSmallest = j
		list = swap(list, i, nextSmallest)
	return list
	
def bubbleSort(list):
	length = len(list)
	flag = True
	while flag:
		flag = False
		for i in range(1, length):
			if list[i-1] > list[i]:
				list = swap(list, i-1, i)
				flag = True
		length -= 1
	return list
def main():
	problemSize = 1000
	list = [randint(0,99) for i in range(problemSize)]
	
	start = time()
	list = bubbleSort(list)
	end = time()
	print(end - start)
main()