def fib(int):
	list = [0,1]
	if int <= 0:
		return []
	elif int <= 2:
		return list[:int]
	elif int > 2:
		for i in range(1,int-1):
			list.append((list[i]+list[i-1]))
		return list

while True:
	x = int(input("Enter an integer: "))
	if x < 0:
		break
	print()
	print(fib(x))
	print()