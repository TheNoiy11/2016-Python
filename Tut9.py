#
#Name: Brian LeBlanc
#Student Number: 101042929
#
#Gaddis, T. (2015). “Starting Out With Python”
#

#QUESTION 1
def mul(a,b):
	return a*b

print("~~~~~~~~~~~~~~QUESTION 1~~~~~~~~~~~~~~")
print(mul(9,9))
print()

#QUESTION 2
def mulRec(a,b):
	if b == 0:
		return 0
	return mulRec(a,b-1) + a

print("~~~~~~~~~~~~~~QUESTION 2~~~~~~~~~~~~~~")
print(mulRec(9,9))
print()

#QUESTION 3
morse_code_dict = {
'A': '.-',     
'B': '-...',
'C': '-.-.', 
'D': '-..',    
'E': '.',      
'F': '..-.',
'G': '--.',    
'H': '....',   
'I': '..',
'J': '.---',   
'K': '-.-',    
'L': '.-..',
'M': '--',     
'N': '-.',     
'O': '---',
'P': '.--.',   
'Q': '--.-',  
'R': '.-.',
'S': '...',    
'T': '-',      
'U': '..-',
'V': '...-',   
'W': '.--',    
'X': '-..-',
'Y': '-.--',   
'Z': '--..',
' ': '   '}

def engToMorse(string):
	global morse_code_dict
	string = string.upper()
	if string == "":
		return ""
	return morse_code_dict[string[0]] + " " + engToMorse(string[1:])
	
print("~~~~~~~~~~~~~~QUESTION 3~~~~~~~~~~~~~~")
print(engToMorse("Hello World"))
print()

#QUESTION 4
def sumRec(list):
	if len(list) == 1:
		return list[0]
	return list[0] + sumRec(list[1:])

print("~~~~~~~~~~~~~~QUESTION 4~~~~~~~~~~~~~~")
print(sumRec([1,2,3,4,5,6,7]))
print()

#QUESTION 5
def sumEvenOddZeroes(list):
	if len(list) == 0:
		return (0,0,0)
	
	if list[0] == 0:
		sumEven, sumOdd, Zeroes = sumEvenOddZeroes(list[1:])
		return sumEven, sumOdd, Zeroes + 1
	elif list[0] % 2 == 0:
		sumEven, sumOdd, Zeroes = sumEvenOddZeroes(list[1:])
		return sumEven + list[0], sumOdd, Zeroes
	elif list[0] % 2 != 0:
		sumEven, sumOdd, Zeroes = sumEvenOddZeroes(list[1:])
		return sumEven, sumOdd + list[0], Zeroes
		
print("~~~~~~~~~~~~~~QUESTION 5~~~~~~~~~~~~~~")
print(sumEvenOddZeroes([0,2,5,0,2,5,0,2,5]))
print()

#QUESTION 6
def MaxMin(list):
	if len(list) == 0:
		return 0,0
	max, min = MaxMin(list[1:])
	
	if list[0] > max:
		return list[0], min
	elif list[0] < min:
		return max, list[0]
	else:
		return max, min
		
print("~~~~~~~~~~~~~~QUESTION 6~~~~~~~~~~~~~~")
print(MaxMin([-10,10,5,6,-20]))
print()

#QUESTION 7
from time import time
from random import randint

print("~~~~~~~~~~~~~~QUESTION 7~~~~~~~~~~~~~~")

start = time()
for i in range(500000):
	mul(randint(0,5),randint(0,5))
print("Non-recursive multiplication finished in:", time()-start, "seconds")

start = time()
for i in range(500000):
	mulRec(randint(0,5),randint(0,5))
print("Recursive multiplication finished in:", time()-start, "seconds")