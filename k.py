for i in range(0,4,1):
	print("*", end="")
	for j in range(i):
		print(".",end="")
	print("*",end="")
	for k in range((8-i)):
		print(".",end="")
	print("*")
for i in range(9,5,-1):
	for j in range(i):
		print(".", end="")
	print("*", end="")
	print("")