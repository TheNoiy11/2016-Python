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