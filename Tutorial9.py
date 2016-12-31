#
#Name: Brian LeBlanc
#Student Number: 101042929
#
#Gaddis, T. (2015). “Starting Out With Python”
#

from time import clock, time, sleep
from random import randint

#QUESTION 1
def mul(a,b):
	return a*b

print(mul(4,200))

#QUESTION 2
def mulRec(a,b):
	if b == 0:
		return 0
	return mulRec(a,b-1) + a
	
print(mulRec(100,200))

#QUESTION 3


#QUESTION 4
def sumList(list):
	if len(list) == 1:
		return list[0]
	return list[0] + sumList(list[1:])

print(sumList([5,5,5,6,7,1,5]))

#QUESTION 5
def sumOddEvenZero(list):
	if len(list) == 0:
		return(0,0,0)
	
	if list[0] == 0:
		sumEven, sumOdd, amountZero = sumOddEvenZero(list[1:])
		return (list[0]+sumEven, sumOdd, amountZero+1)
	elif list[0] % 2 == 0:
		sumEven, sumOdd, amountZero = sumOddEvenZero(list[1:])
		return (list[0]+sumEven, sumOdd, amountZero)
	else:
		sumEven, sumOdd, amountZero = sumOddEvenZero(list[1:])
		return (sumEven, list[0]+sumOdd, amountZero)

print(sumOddEvenZero([0,1,2]))

#QUESTION 6
def MaxMin(list):
	if len(list) == 0:
		print("GOT THERE")
		return (0, 0)
	(max, min) = MaxMin(list[1:])
	if list[0] > max:
		return (list[0], min)
	elif list[0] < min:
		return (max, list[0])
	return (max,min)
	
print(MaxMin([-1,2,1000000000000,-100,3,-2]))

#QUESTION 7
start = time()
for i in range(1000000):
	mul(randint(0,10),randint(0,10))
print(time()-start)

start = time()
for i in range(100000):
	mulRec(randint(0,10),randint(0,10))
print(time()-start)