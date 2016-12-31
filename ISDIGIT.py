def sumEven(list):
	sum = 0
	for i in range(len(list)):
		if list[i].isdigit == True:
			if list[i] % 2 == 0:
				sum = sum + list[i]
	return sum
	
def sumOdd(list):
	sum = 0
	for i in range(len(list)):
		if list[i].isdigit == True:
			if list[i] % 2 != 0:
				sum = sum + list[i]
	return sum
	
def concatStr(list):
	string = ""
	for i in range(len(list)):
		if list[i].replace('.','',1).isdigit == False:
			string = string + list[i]
	
	return string
list = []
flag = True
while flag:
	while flag:
		more = input("Would you like to (a)dd a value, (r)emove the last value, or e(x)it the program?")
		if more == "x":
			flag = False
			print("Goodbye")
		elif more == "a" or more == "r":
			break
		else:
			print("Please enter either a, r, or x")
	if more == "a":
		next = (input("What value would you like to add? "))
		if next.isdigit() == True:
			next = int(next)
		elif next.replace('.','',1).isdigit() == True:
			next = float(next)
		list.append(next)
		print("The list is now:", list)
	if more == "r":
		list.pop()
		print("The list is now:", list)

print(sumEven(list))
print(sumOdd(list))
prit(concatStr(list))