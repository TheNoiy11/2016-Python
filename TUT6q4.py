from random import randint

def playRPS():
	comp = randint(0,2)
	while True:
		user = int(input("Rock(0), Paper(1), or Scissors(2)?  "))
		if user == 0 or user == 1 or user == 2:
			break
		else:
			print("Hey! Please enter a valid input")
	
	if comp == user:
		if user == 0:
			print("You both chose ROCK")
		elif user == 1:
			print("You both chose PAPER")
		else:
			print("You both chose SCISSORS")
		print("It's a tie!")
	elif comp == 0:
		print("The computer chose ROCK")
		if user == 1:
			print("You chose PAPER")
			print("You win!")
		elif user == 2:
			print("You chose SCISSORS")
			print("You lose!")
	elif comp == 1:
		print("The computer chose PAPER")
		if user == 0:
			print("You chose ROCK")
			print("You lose!")
		elif user == 2:
			print("You chose SCISSORS")
			print("You win!")
	elif comp == 2:
		print("The computer chose SCISSORS")
		if user == 0:
			print("You chose ROCK")
			print("You win!")
		elif user == 1:
			print("You chose PAPER")
			print("You lose!")

def playTTT():
	for i in range(50):
		print("")
	for i in range(3):
		for j in range(3):
			print("-", end="")
		print("")
	if randint(0,1) == 1:
		playerTurn = True
		print("You go first!")
	else:
		playerTurn = False
		print("The computer goes first")
	print("Each square is represented by a 2 digit number")
	print("The first is the coulmn, the second is the row")
	print("For example, 00 is the bottom left corner, 10 is the middle of the first column, and 11 is the centre")
	
	square00 = 0
	square01 = 0
	square02 = 0
	
	square10 = 0
	square11 = 0
	square12 = 0
	
	square20 = 0
	square21 = 0
	square22 = 0

	active = True
	while active:
		if playerTurn == True:
			user = input("Your turn, where do you want to go?")
			if user == "00":
				square00 = 1
			elif user == "01":
				square01 = 1
			elif user == "02":
				square02 = 1
			elif user == "10":
				square10 = 1
			elif user == "11":
				square11 = 1
			elif user == "12":
				square12 = 1
			elif user == "20":
				square20 = 1
			elif user == "21":
				square21 = 1
			elif user == "22":
				square22 = 1
			playerTurn = False
		elif playerTurn == False:
			print("COMPUTER TURN")
			playerTurn = True
		for i in range(50):
			print("")
		for i in range(3):
			for j in range(3):
				if square == 1:
					print("X", end="")
				elif ("square"+str(i)+str(j)) == 2:
					print("O", end="")
				else:
					print("-", end="")
			print("")
mainFlag = True
while mainFlag:
	flag = True
	print("You can play 'Rock, Paper, Scissors'(RPS), or you can play 'Tic-Tac-Toe'(TTT)")
	game = input("Which game would you like to play, or would you like to quit? (RPS, TTT, quit): ")
	while flag:
		if game == "RPS":
			while flag:
				playRPS()
				while flag:
					more = input("Would you like to play again?(y/n): ")
					if more == "y":
						break
					if more == "n":
						flag = False
					else:
						print("please enter y or n")
		elif game == "TTT":
			while flag:
				playTTT()
				while flag:
					more = input("Would you like to play again?(y/n): ")
					if more == "y":
						break
					if more == "n":
						flag = False
					else:
						print("please enter y or n")
		elif game == "quit":
			mainFlag = False
			flag = False
		else:
			print("Your input was invalid, please enter RPS, TTT, or quit")