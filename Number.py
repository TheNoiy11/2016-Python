user = input("Enter a number")
print(user)
for i in user:
	print(i)
for i in user[0:]:
	if i != int(i):
		print("Not a number")
		break
	elif i == int(i):
		print("It is a whole number")