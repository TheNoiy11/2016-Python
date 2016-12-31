flag = True
while flag:
	#asks the user for their input
	amount = int(input("Input an integer between 1 and 9: "))
	if (amount < 1) or (amount > 9):
		print("The integer must be between 1 and 9, inclulsively")
		#if their input is not in between 1 and 9, it will skip the "else:"
		#and will loop back to the start, asking for another number
	else:
		#prints the pattern out
		for i in range(amount):
			for j in range(amount-i):
				print(" ", end="")
			for k in range(i+1):
				print(i+1, "", end="")
			print("")
		#another loop to be able to ask again if they input incorrectly
		while flag:
			more = input("Do you want to draw another triangle? (Y/N): ").upper()
			if more == "N":
				flag = False
				#sets the flag to False so it exits out of both loops
			elif more == "Y":
				break
				#breaks out of this loop only, and continues onto the primary loop
				#which allows them to input another integer
			else:
				print("Your input was invalid")
				#will loop back to the start of this loop
				#so if their input is not Y or N, it will let them try again
print("You have exited the program")