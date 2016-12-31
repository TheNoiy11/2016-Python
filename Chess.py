from SimpleGraphics import *
from time import sleep
from copy import deepcopy

def menu():
	global xWINDOW, yWINDOW
	xWINDOW = 400
	yWINDOW = 200
	resize(xWINDOW,yWINDOW)
	while not closed():
		mX = mouseX()
		mY = mouseY()
		clear()
		setColor(255,255,255)
		setFont("Times","40","Bold")
		rect(100,50,200,100)
		setColor(0,0,0)
		text(200,100,"Chess")
		if not mX < 0 and not mX > xWINDOW and not mY < 0 and not mY > yWINDOW:
			if not mX < 100 and not mX > 300 and not mY < 50 and not mY > 150:
				setColor(255,0,0)
				rect(100,50,200,100)
				setColor(0,0,0)
				text(200,100,"Chess")
				update()
				if leftButtonPressed() == True:
					clear()
					update()
					sleep(1)
					return True

def newBoard():
	board = []
	for y in range(8):
		nextRow = []
		for x in range(8):
			if y == 0:
				if x == 0 or x == 7:
					nextRow.append("wRook")
				elif x == 1 or x == 6:
					nextRow.append("wKnig")
				elif x == 2 or x == 5:
					nextRow.append("wBish")
				elif x == 3:
					nextRow.append("wQuee")
				elif x == 4:
					nextRow.append("wKing")
			elif y == 1:
				nextRow.append("wPawn")
			elif y == 6:
				nextRow.append("bPawn")
			elif y == 7:
				if x == 0 or x == 7:
					nextRow.append("bRook")
				elif x == 1 or x == 6:
					nextRow.append("bKnig")
				elif x == 2 or x == 5:
					nextRow.append("bBish")
				elif x == 3:
					nextRow.append("bQuee")
				elif x == 4:
					nextRow.append("bKing")
			else:
				nextRow.append("empty")
		board.append(nextRow)
	return board
	
def drawBackBoard():
	global xWINDOW, yWINDOW
	xWINDOW = 500
	yWINDOW = 400
	resize(xWINDOW,yWINDOW)
	for y in range(8):
		for x in range(8):
			if (x+y) % 2 == 0:
				setColor(150,150,150)
			else:
				setColor(135,206,225)
			rect(x*50,y*50,50,50)

def drawPiece(x,y,piece):
	if piece == "MoveOption":
		setColor(150,50,50)
		rect((x*50)+20,(y*50)+20,10,10)
		update()
	elif piece == "KillOption":
		setColor(50,150,50)
		rect((x*50)+20,(y*50)+20,10,10)
		update()
	elif piece != "empty":
		pieceColor = piece[0]
		pieceType = piece[1:]
		setFont("Times","20","Bold")
		if pieceColor == "w":
			setColor(255,255,255)
		elif pieceColor == "b":
			setColor(0,0,0)
		letter = ""
		if pieceType == "Pawn":
			letter = "P"
		elif pieceType == "Rook":
			letter = "R"
		elif pieceType == "Knig":
			letter = "K"
		elif pieceType == "Bish":
			letter = "B"
		elif pieceType == "Quee":
			letter = "Q"
		elif pieceType == "King":
			letter = "KI"
		text((x*50)+25,(y*50)+25,letter)

def drawCurrentBoard(board):
	clear()
	global CURRENT_TURN
	setFont("Times","20","Bold")
	setColor("gold4")
	text(400,0,"Turn:","nw")
	if CURRENT_TURN == "White":
		setColor(255,255,255)
		text(400,30,"White","nw")
	elif CURRENT_TURN == "Black":
		setColor(0,0,0)
		text(400,30,"Black","nw")
	drawBackBoard()
	for y in range(8):
		for x in range(8):
			drawPiece(x,y,board[y][x])
	update()

def checkMoves(board,piece,y,x):
	global CURRENT_TURN
	global WINNER
	tempBoard = deepcopy(board)
	pieceColor = piece[0]
	pieceType = piece[1:]
	canMove = False
	if pieceColor == "b" and CURRENT_TURN == "Black":
		if pieceType == "Pawn":
			if not y < 0:
				if board[y-1][x] == "empty":
					if y == 6 and board[y-2][x] == "empty":
						drawPiece(x,y-2,"MoveOption")
						tempBoard[y-2][x] = "MoveOption"
						canMove = True
					drawPiece(x,y-1,"MoveOption")
					tempBoard[y-1][x] = "MoveOption"
					canMove = True
				if not (x+1) > 7:
					if (board[y-1][x+1])[0] == "w":
						drawPiece(x+1,y-1,"KillOption")
						tempBoard[y-1][x+1] = "KillOption"
						canMove = True
				if not (x-1) < 0:
					if (board[y-1][x-1])[0] == "w":
						drawPiece(x-1,y-1,"KillOption")
						tempBoard[y-1][x-1] = "KillOption"
						canMove = True
		elif pieceType == "Rook":
			if not (y-1) < 0:
				for i in range(y-1,-1,-1):
					if board[i][x] == "empty":
						drawPiece(x,i,"MoveOption")
						tempBoard[i][x] = "MoveOption"
						canMove = True
					elif (board[i][x])[0] == "w":
						drawPiece(x,i,"KillOption")
						tempBoard[i][x] = "KillOption"
						canMove = True
						break
					elif (board[i][x])[0] == "b":
						break
			if not (y+1) > 7:
				for i in range(y+1,8,1):
					if board[i][x] == "empty":
						drawPiece(x,i,"MoveOption")
						tempBoard[i][x] = "MoveOption"
						canMove = True
					elif (board[i][x])[0] == "w":
						drawPiece(x,i,"KillOption")
						tempBoard[i][x] = "KillOption"
						canMove = True
						break
					elif (board[i][x])[0] == "b":
						break
			if not (x-1) < 0:
				for i in range(x-1,-1,-1):
					if board[y][i] == "empty":
						drawPiece(i,y,"MoveOption")
						tempBoard[y][i] = "MoveOption"
						canMove = True
					elif (board[y][i])[0] == "w":
						drawPiece(i,y,"KillOption")
						tempBoard[y][i] = "KillOption"
						canMove = True
						break
					elif (board[y][i])[0] == "b":
						break
			if not (x+1) > 7:
				for i in range(x+1,8,1):
					if board[y][i] == "empty":
						drawPiece(i,y,"MoveOption")
						tempBoard[y][i] = "MoveOption"
						canMove = True
					elif (board[y][i])[0] == "w":
						drawPiece(i,y,"KillOption")
						tempBoard[y][i] = "KillOption"
						canMove = True
						break
					elif (board[y][i])[0] == "b":
						break
		elif pieceType == "Knig":
			if not y-2 < 0:
				if not x-1 < 0:
					if board[y-2][x-1] == "empty":
						drawPiece(x-1,y-2,"MoveOption")
						tempBoard[y-2][x-1] = "MoveOption"
						canMove = True
					elif (board[y-2][x-1])[0] == "w":
						drawPiece(x-1,y-2,"KillOption")
						tempBoard[y-2][x-1] = "KillOption"
						canMove = True
				if not x+1 > 7:
					if board[y-2][x+1] == "empty":
						drawPiece(x+1,y-2,"MoveOption")
						tempBoard[y-2][x+1] = "MoveOption"
						canMove = True
					elif (board[y-2][x+1])[0] == "w":
						drawPiece(x+1,y-2,"KillOption")
						tempBoard[y-2][x+1] = "KillOption"
						canMove = True
			if not y+2 > 7:
				if not x-1 < 0:
					if board[y+2][x-1] == "empty":
						drawPiece(x-1,y+2,"MoveOption")
						tempBoard[y+2][x-1] = "MoveOption"
						canMove = True
					elif (board[y+2][x-1])[0] == "w":
						drawPiece(x-1,y+2,"KillOption")
						tempBoard[y+2][x-1] = "KillOption"
						canMove = True
				if not x+1 > 7:
					if board[y+2][x+1] == "empty":
						drawPiece(x+1,y+2,"MoveOption")
						tempBoard[y+2][x+1] = "MoveOption"
						canMove = True
					elif (board[y+2][x+1])[0] == "w":
						drawPiece(x+1,y+2,"KillOption")
						tempBoard[y+2][x+1] = "KillOption"
						canMove = True
			if not x-2 < 0:
				if not y-1 < 0:
					if board[y-1][x-2] == "empty":
						drawPiece(x-2,y-1,"MoveOption")
						tempBoard[y-1][x-2] = "MoveOption"
						canMove = True
					elif (board[y-1][x-2])[0] == "w":
						drawPiece(x-2,y-1,"KillOption")
						tempBoard[y-1][x-2] = "KillOption"
						canMove = True
				if not y+1 > 7:
					if board[y+1][x-2] == "empty":
						drawPiece(x-2,y+1,"MoveOption")
						tempBoard[y+1][x-2] = "MoveOption"
						canMove = True
					elif (board[y+1][x-2])[0] == "w":
						drawPiece(x-2,y+1,"KillOption")
						tempBoard[y+1][x-2] = "KillOption"
						canMove = True
			if not x+2 > 7:
				if not y-1 < 0:
					if board[y-1][x+2] == "empty":
						drawPiece(x+2,y-1,"MoveOption")
						tempBoard[y-1][x+2] = "MoveOption"
						canMove = True
					elif (board[y-1][x+2])[0] == "w":
						drawPiece(x+2,y-1,"KillOption")
						tempBoard[y-1][x+2] = "KillOption"
						canMove = True
				if not y+1 > 7:
					if board[y+1][x+2] == "empty":
						drawPiece(x+2,y+1,"MoveOption")
						tempBoard[y+1][x+2] = "MoveOption"
						canMove = True
					elif (board[y+1][x+2])[0] == "w":
						drawPiece(x+2,y+1,"KillOption")
						tempBoard[y+1][x+2] = "KillOption"
						canMove = True
		elif pieceType == "Bish":
			i = 1
			while not (x-i) < 0 and not (y-i) < 0:
				if board[y-i][x-i] == "empty":
					drawPiece(x-i,y-i,"MoveOption")
					tempBoard[y-i][x-i] = "MoveOption"
					canMove = True
				elif (board[y-i][x-i])[0] == "w":
					drawPiece(x-i,y-i,"KillOption")
					tempBoard[y-i][x-i] = "KillOption"
					canMove = True
					break
				elif (board[y-i][x-i])[0] == "b":
					break
				i = i + 1
			i = 1
			while not (x+i) > 7 and not (y-i) < 0:
				if board[y-i][x+i] == "empty":
					drawPiece(x+i,y-i,"MoveOption")
					tempBoard[y-i][x+i] = "MoveOption"
					canMove = True
				elif (board[y-i][x+i])[0] == "w":
					drawPiece(x+i,y-i,"KillOption")
					tempBoard[y-i][x+i] = "KillOption"
					canMove = True
					break
				elif (board[y-i][x+i])[0] == "b":
					break
				i = i + 1
			i = 1
			while not (x-i) < 0 and not (y+i) > 7:
				if board[y+i][x-i] == "empty":
					drawPiece(x-i,y+i,"MoveOption")
					tempBoard[y+i][x-i] = "MoveOption"
					canMove = True
				elif (board[y+i][x-i])[0] == "w":
					drawPiece(x-i,y+i,"KillOption")
					tempBoard[y+i][x-i] = "KillOption"
					canMove = True
					break
				elif (board[y+i][x-i])[0] == "b":
					break
				i = i + 1
			i = 1
			while not (x+i) > 7 and not (y+i) > 7:
				if board[y+i][x+i] == "empty":
					drawPiece(x+i,y+i,"MoveOption")
					tempBoard[y+i][x+i] = "MoveOption"
					canMove = True
				elif (board[y+i][x+i])[0] == "w":
					drawPiece(x+i,y+i,"KillOption")
					tempBoard[y+i][x+i] = "KillOption"
					canMove = True
					break
				elif (board[y+i][x+i])[0] == "b":
					break
				i = i + 1
		elif pieceType == "Quee":
			if not (y-1) < 0:
				for i in range(y-1,-1,-1):
					if board[i][x] == "empty":
						drawPiece(x,i,"MoveOption")
						tempBoard[i][x] = "MoveOption"
						canMove = True
					elif (board[i][x])[0] == "w":
						drawPiece(x,i,"KillOption")
						tempBoard[i][x] = "KillOption"
						canMove = True
						break
					elif (board[i][x])[0] == "b":
						break
			if not (y+1) > 7:
				for i in range(y+1,8,1):
					if board[i][x] == "empty":
						drawPiece(x,i,"MoveOption")
						tempBoard[i][x] = "MoveOption"
						canMove = True
					elif (board[i][x])[0] == "w":
						drawPiece(x,i,"KillOption")
						tempBoard[i][x] = "KillOption"
						canMove = True
						break
					elif (board[i][x])[0] == "b":
						break
			if not (x-1) < 0:
				for i in range(x-1,-1,-1):
					if board[y][i] == "empty":
						drawPiece(i,y,"MoveOption")
						tempBoard[y][i] = "MoveOption"
						canMove = True
					elif (board[y][i])[0] == "w":
						drawPiece(i,y,"KillOption")
						tempBoard[y][i] = "KillOption"
						canMove = True
						break
					elif (board[y][i])[0] == "b":
						break
			if not (x+1) > 7:
				for i in range(x+1,8,1):
					if board[y][i] == "empty":
						drawPiece(i,y,"MoveOption")
						tempBoard[y][i] = "MoveOption"
						canMove = True
					elif (board[y][i])[0] == "w":
						drawPiece(i,y,"KillOption")
						tempBoard[y][i] = "KillOption"
						canMove = True
						break
					elif (board[y][i])[0] == "b":
						break
			i = 1
			while not (x-i) < 0 and not (y-i) < 0:
				if board[y-i][x-i] == "empty":
					drawPiece(x-i,y-i,"MoveOption")
					tempBoard[y-i][x-i] = "MoveOption"
					canMove = True
				elif (board[y-i][x-i])[0] == "w":
					drawPiece(x-i,y-i,"KillOption")
					tempBoard[y-i][x-i] = "KillOption"
					canMove = True
					break
				elif (board[y-i][x-i])[0] == "b":
					break
				i = i + 1
			i = 1
			while not (x+i) > 7 and not (y-i) < 0:
				if board[y-i][x+i] == "empty":
					drawPiece(x+i,y-i,"MoveOption")
					tempBoard[y-i][x+i] = "MoveOption"
					canMove = True
				elif (board[y-i][x+i])[0] == "w":
					drawPiece(x+i,y-i,"KillOption")
					tempBoard[y-i][x+i] = "KillOption"
					canMove = True
					break
				elif (board[y-i][x+i])[0] == "b":
					break
				i = i + 1
			i = 1
			while not (x-i) < 0 and not (y+i) > 7:
				if board[y+i][x-i] == "empty":
					drawPiece(x-i,y+i,"MoveOption")
					tempBoard[y+i][x-i] = "MoveOption"
					canMove = True
				elif (board[y+i][x-i])[0] == "w":
					drawPiece(x-i,y+i,"KillOption")
					tempBoard[y+i][x-i] = "KillOption"
					canMove = True
					break
				elif (board[y+i][x-i])[0] == "b":
					break
				i = i + 1
			i = 1
			while not (x+i) > 7 and not (y+i) > 7:
				if board[y+i][x+i] == "empty":
					drawPiece(x+i,y+i,"MoveOption")
					tempBoard[y+i][x+i] = "MoveOption"
					canMove = True
				elif (board[y+i][x+i])[0] == "w":
					drawPiece(x+i,y+i,"KillOption")
					tempBoard[y+i][x+i] = "KillOption"
					canMove = True
					break
				elif (board[y+i][x+i])[0] == "b":
					break
				i = i + 1
		elif pieceType == "King":
			if x-1 > 0:
				if board[y][x-1] == "empty":
					drawPiece(x-1,y,"MoveOption")
					tempBoard[y][x-1] = "MoveOption"
					canMove = True
				elif (board[y][x-1])[0] == "w":
					drawPiece(x-1,y,"KillOption")
					tempBoard[y][x-1] = "KillOption"
					canMove = True
			if x+1 < 7:
				if board[y][x+1] == "empty":
					drawPiece(x+1,y,"MoveOption")
					tempBoard[y][x+1] = "MoveOption"
					canMove = True
				elif (board[y][x+1])[0] == "w":
					drawPiece(x+1,y,"KillOption")
					tempBoard[y][x+1] = "KillOption"
					canMove = True
			if y-1 > 0:
				if board[y-1][x] == "empty":
					drawPiece(x,y-1,"MoveOption")
					tempBoard[y-1][x] = "MoveOption"
					canMove = True
				elif (board[y-1][x])[0] == "w":
					drawPiece(x,y-1,"KillOption")
					tempBoard[y-1][x] = "KillOption"
					canMove = True
			if y+1 < 7:
				if board[y+1][x] == "empty":
					drawPiece(x,y+1,"MoveOption")
					tempBoard[y+1][x] = "MoveOption"
					canMove = True
				elif (board[y+1][x])[0] == "w":
					drawPiece(x,y+1,"KillOption")
					tempBoard[y+1][x] = "KillOption"
					canMove = True
			if not (x-1) < 0 and not (y-1) < 0:
				if board[y-1][x-1] == "empty":
					drawPiece(x-1,y-1,"MoveOption")
					tempBoard[y-1][x-1] = "MoveOption"
					canMove = True
				elif (board[y-1][x-1])[0] == "w":
					drawPiece(x-1,y-1,"KillOption")
					tempBoard[y-1][x-1] = "KillOption"
					canMove = True
			if not (x+1) > 7 and not (y-1) < 0:
				if board[y-1][x+1] == "empty":
					drawPiece(x+1,y-1,"MoveOption")
					tempBoard[y-1][x+1] = "MoveOption"
					canMove = True
				elif (board[y-1][x+1])[0] == "w":
					drawPiece(x+1,y-1,"KillOption")
					tempBoard[y-1][x+1] = "KillOption"
					canMove = True
			if not (x-1) < 0 and not (y+1) > 7:
				if board[y+1][x-1] == "empty":
					drawPiece(x-1,y+1,"MoveOption")
					tempBoard[y+1][x-1] = "MoveOption"
					canMove = True
				elif (board[y+1][x-1])[0] == "w":
					drawPiece(x-1,y+1,"KillOption")
					tempBoard[y+1][x-1] = "KillOption"
					canMove = True
			if not (x+1) > 7 and not (y+1) > 7:
				if board[y+1][x+1] == "empty":
					drawPiece(x+1,y+1,"MoveOption")
					tempBoard[y+1][x+1] = "MoveOption"
					canMove = True
				elif (board[y+1][x+1])[0] == "w":
					drawPiece(x+1,y+1,"KillOption")
					tempBoard[y+1][x+1] = "KillOption"
					canMove = True
	if pieceColor == "w" and CURRENT_TURN == "White":
		if pieceType == "Pawn":
			if not y > 7:	
				if board[y+1][x] == "empty":
					if y == 1 and board[y+2][x] == "empty":
						drawPiece(x,y+2,"MoveOption")
						tempBoard[y+2][x] = "MoveOption"
						canMove = True
					drawPiece(x,y+1,"MoveOption")
					tempBoard[y+1][x] = "MoveOption"
					canMove = True
				if not (x+1) > 7:
					if (board[y+1][x+1])[0] == "b":
						drawPiece(x+1,y+1,"KillOption")
						tempBoard[y+1][x+1] = "KillOption"
						canMove = True
				if not (x-1) < 0:
					if (board[y+1][x-1])[0] == "b":
						drawPiece(x-1,y+1,"KillOption")
						tempBoard[y+1][x-1] = "KillOption"
						canMove = True
		elif pieceType == "Rook":
			if not (y-1) < 0:
				for i in range(y-1,-1,-1):
					if board[i][x] == "empty":
						drawPiece(x,i,"MoveOption")
						tempBoard[i][x] = "MoveOption"
						canMove = True
					elif (board[i][x])[0] == "b":
						drawPiece(x,i,"KillOption")
						tempBoard[i][x] = "KillOption"
						canMove = True
						break
					elif (board[i][x])[0] == "w":
						break
			if not (y+1) > 7:
				for i in range(y+1,8,1):
					if board[i][x] == "empty":
						drawPiece(x,i,"MoveOption")
						tempBoard[i][x] = "MoveOption"
						canMove = True
					elif (board[i][x])[0] == "b":
						drawPiece(x,i,"KillOption")
						tempBoard[i][x] = "KillOption"
						canMove = True
						break
					elif (board[i][x])[0] == "w":
						break
			if not (x-1) < 0:
				for i in range(x-1,-1,-1):
					if board[y][i] == "empty":
						drawPiece(i,y,"MoveOption")
						tempBoard[y][i] = "MoveOption"
						canMove = True
					elif (board[y][i])[0] == "b":
						drawPiece(i,y,"KillOption")
						tempBoard[y][i] = "KillOption"
						canMove = True
						break
					elif (board[y][i])[0] == "w":
						break
			if not (x+1) > 7:
				for i in range(x+1,8,1):
					if board[y][i] == "empty":
						drawPiece(i,y,"MoveOption")
						tempBoard[y][i] = "MoveOption"
						canMove = True
					elif (board[y][i])[0] == "b":
						drawPiece(i,y,"KillOption")
						tempBoard[y][i] = "KillOption"
						canMove = True
						break
					elif (board[y][i])[0] == "w":
						break
		elif pieceType == "Knig":
			if not y-2 < 0:
				if not x-1 < 0:
					if board[y-2][x-1] == "empty":
						drawPiece(x-1,y-2,"MoveOption")
						tempBoard[y-2][x-1] = "MoveOption"
						canMove = True
					elif (board[y-2][x-1])[0] == "b":
						drawPiece(x-1,y-2,"KillOption")
						tempBoard[y-2][x-1] = "KillOption"
						canMove = True
				if not x+1 > 7:
					if board[y-2][x+1] == "empty":
						drawPiece(x+1,y-2,"MoveOption")
						tempBoard[y-2][x+1] = "MoveOption"
						canMove = True
					elif (board[y-2][x+1])[0] == "b":
						drawPiece(x+1,y-2,"KillOption")
						tempBoard[y-2][x+1] = "KillOption"
						canMove = True
			if not y+2 > 7:
				if not x-1 < 0:
					if board[y+2][x-1] == "empty":
						drawPiece(x-1,y+2,"MoveOption")
						tempBoard[y+2][x-1] = "MoveOption"
						canMove = True
					elif (board[y+2][x-1])[0] == "b":
						drawPiece(x-1,y+2,"KillOption")
						tempBoard[y+2][x-1] = "KillOption"
						canMove = True
				if not x+1 > 7:
					if board[y+2][x+1] == "empty":
						drawPiece(x+1,y+2,"MoveOption")
						tempBoard[y+2][x+1] = "MoveOption"
						canMove = True
					elif (board[y+2][x+1])[0] == "b":
						drawPiece(x+1,y+2,"KillOption")
						tempBoard[y+2][x+1] = "KillOption"
						canMove = True
			if not x-2 < 0:
				if not y-1 < 0:
					if board[y-1][x-2] == "empty":
						drawPiece(x-2,y-1,"MoveOption")
						tempBoard[y-1][x-2] = "MoveOption"
						canMove = True
					elif (board[y-1][x-2])[0] == "b":
						drawPiece(x-2,y-1,"KillOption")
						tempBoard[y-1][x-2] = "KillOption"
						canMove = True
				if not y+1 > 7:
					if board[y+1][x-2] == "empty":
						drawPiece(x-2,y+1,"MoveOption")
						tempBoard[y+1][x-2] = "MoveOption"
						canMove = True
					elif (board[y+1][x-2])[0] == "b":
						drawPiece(x-2,y+1,"KillOption")
						tempBoard[y+1][x-2] = "KillOption"
						canMove = True
			if not x+2 > 7:
				if not y-1 < 0:
					if board[y-1][x+2] == "empty":
						drawPiece(x+2,y-1,"MoveOption")
						tempBoard[y-1][x+2] = "MoveOption"
						canMove = True
					elif (board[y-1][x+2])[0] == "b":
						drawPiece(x+2,y-1,"KillOption")
						tempBoard[y-1][x+2] = "KillOption"
						canMove = True
				if not y+1 > 7:
					if board[y+1][x+2] == "empty":
						drawPiece(x+2,y+1,"MoveOption")
						tempBoard[y+1][x+2] = "MoveOption"
						canMove = True
					elif (board[y+1][x+2])[0] == "b":
						drawPiece(x+2,y+1,"KillOption")
						tempBoard[y+1][x+2] = "KillOption"
						canMove = True
		elif pieceType == "Bish":
			i = 1
			while not (x-i) < 0 and not (y-i) < 0:
				if board[y-i][x-i] == "empty":
					drawPiece(x-i,y-i,"MoveOption")
					tempBoard[y-i][x-i] = "MoveOption"
					canMove = True
				elif (board[y-i][x-i])[0] == "b":
					drawPiece(x-i,y-i,"KillOption")
					tempBoard[y-i][x-i] = "KillOption"
					canMove = True
					break
				elif (board[y-i][x-i])[0] == "w":
					break
				i = i + 1
			i = 1
			while not (x+i) > 7 and not (y-i) < 0:
				if board[y-i][x+i] == "empty":
					drawPiece(x+i,y-i,"MoveOption")
					tempBoard[y-i][x+i] = "MoveOption"
					canMove = True
				elif (board[y-i][x+i])[0] == "b":
					drawPiece(x+i,y-i,"KillOption")
					tempBoard[y-i][x+i] = "KillOption"
					canMove = True
					break
				elif (board[y-i][x+i])[0] == "w":
					break
				i = i + 1
			i = 1
			while not (x-i) < 0 and not (y+i) > 7:
				if board[y+i][x-i] == "empty":
					drawPiece(x-i,y+i,"MoveOption")
					tempBoard[y+i][x-i] = "MoveOption"
					canMove = True
				elif (board[y+i][x-i])[0] == "b":
					drawPiece(x-i,y+i,"KillOption")
					tempBoard[y+i][x-i] = "KillOption"
					canMove = True
					break
				elif (board[y+i][x-i])[0] == "w":
					break
				i = i + 1
			i = 1
			while not (x+i) > 7 and not (y+i) > 7:
				if board[y+i][x+i] == "empty":
					drawPiece(x+i,y+i,"MoveOption")
					tempBoard[y+i][x+i] = "MoveOption"
					canMove = True
				elif (board[y+i][x+i])[0] == "b":
					drawPiece(x+i,y+i,"KillOption")
					tempBoard[y+i][x+i] = "KillOption"
					canMove = True
					break
				elif (board[y+i][x+i])[0] == "w":
					break
				i = i + 1
		elif pieceType == "Quee":
			if not (y-1) < 0:
				for i in range(y-1,-1,-1):
					if board[i][x] == "empty":
						drawPiece(x,i,"MoveOption")
						tempBoard[i][x] = "MoveOption"
						canMove = True
					elif (board[i][x])[0] == "b":
						drawPiece(x,i,"KillOption")
						tempBoard[i][x] = "KillOption"
						canMove = True
						break
					elif (board[i][x])[0] == "w":
						break
			if not (y+1) > 7:
				for i in range(y+1,8,1):
					if board[i][x] == "empty":
						drawPiece(x,i,"MoveOption")
						tempBoard[i][x] = "MoveOption"
						canMove = True
					elif (board[i][x])[0] == "b":
						drawPiece(x,i,"KillOption")
						tempBoard[i][x] = "KillOption"
						canMove = True
						break
					elif (board[i][x])[0] == "w":
						break
			if not (x-1) < 0:
				for i in range(x-1,-1,-1):
					if board[y][i] == "empty":
						drawPiece(i,y,"MoveOption")
						tempBoard[y][i] = "MoveOption"
						canMove = True
					elif (board[y][i])[0] == "b":
						drawPiece(i,y,"KillOption")
						tempBoard[y][i] = "KillOption"
						canMove = True
						break
					elif (board[y][i])[0] == "w":
						break
			if not (x+1) > 7:
				for i in range(x+1,8,1):
					if board[y][i] == "empty":
						drawPiece(i,y,"MoveOption")
						tempBoard[y][i] = "MoveOption"
						canMove = True
					elif (board[y][i])[0] == "b":
						drawPiece(i,y,"KillOption")
						tempBoard[y][i] = "KillOption"
						canMove = True
						break
					elif (board[y][i])[0] == "w":
						break
			i = 1
			while not (x-i) < 0 and not (y-i) < 0:
				if board[y-i][x-i] == "empty":
					drawPiece(x-i,y-i,"MoveOption")
					tempBoard[y-i][x-i] = "MoveOption"
					canMove = True
				elif (board[y-i][x-i])[0] == "b":
					drawPiece(x-i,y-i,"KillOption")
					tempBoard[y-i][x-i] = "KillOption"
					canMove = True
					break
				elif (board[y-i][x-i])[0] == "w":
					break
				i = i + 1
			i = 1
			while not (x+i) > 7 and not (y-i) < 0:
				if board[y-i][x+i] == "empty":
					drawPiece(x+i,y-i,"MoveOption")
					tempBoard[y-i][x+i] = "MoveOption"
					canMove = True
				elif (board[y-i][x+i])[0] == "b":
					drawPiece(x+i,y-i,"KillOption")
					tempBoard[y-i][x+i] = "KillOption"
					canMove = True
					break
				elif (board[y-i][x+i])[0] == "w":
					break
				i = i + 1
			i = 1
			while not (x-i) < 0 and not (y+i) > 7:
				if board[y+i][x-i] == "empty":
					drawPiece(x-i,y+i,"MoveOption")
					tempBoard[y+i][x-i] = "MoveOption"
					canMove = True
				elif (board[y+i][x-i])[0] == "b":
					drawPiece(x-i,y+i,"KillOption")
					tempBoard[y+i][x-i] = "KillOption"
					canMove = True
					break
				elif (board[y+i][x-i])[0] == "w":
					break
				i = i + 1
			i = 1
			while not (x+i) > 7 and not (y+i) > 7:
				if board[y+i][x+i] == "empty":
					drawPiece(x+i,y+i,"MoveOption")
					tempBoard[y+i][x+i] = "MoveOption"
					canMove = True
				elif (board[y+i][x+i])[0] == "b":
					drawPiece(x+i,y+i,"KillOption")
					tempBoard[y+i][x+i] = "KillOption"
					canMove = True
					break
				elif (board[y+i][x+i])[0] == "w":
					break
				i = i + 1
		elif pieceType == "King":
			if x-1 > 0:
				if board[y][x-1] == "empty":
					drawPiece(x-1,y,"MoveOption")
					tempBoard[y][x-1] = "MoveOption"
					canMove = True
				elif (board[y][x-1])[0] == "b":
					drawPiece(x-1,y,"KillOption")
					tempBoard[y][x-1] = "KillOption"
					canMove = True
			if x+1 < 7:
				if board[y][x+1] == "empty":
					drawPiece(x+1,y,"MoveOption")
					tempBoard[y][x+1] = "MoveOption"
					canMove = True
				elif (board[y][x+1])[0] == "b":
					drawPiece(x+1,y,"KillOption")
					tempBoard[y][x+1] = "KillOption"
					canMove = True
			if y-1 > 0:
				if board[y-1][x] == "empty":
					drawPiece(x,y-1,"MoveOption")
					tempBoard[y-1][x] = "MoveOption"
					canMove = True
				elif (board[y-1][x])[0] == "b":
					drawPiece(x,y-1,"KillOption")
					tempBoard[y-1][x] = "KillOption"
					canMove = True
			if y+1 < 7:
				if board[y+1][x] == "empty":
					drawPiece(x,y+1,"MoveOption")
					tempBoard[y+1][x] = "MoveOption"
					canMove = True
				elif (board[y+1][x])[0] == "b":
					drawPiece(x,y+1,"KillOption")
					tempBoard[y+1][x] = "KillOption"
					canMove = True
			if not (x-1) < 0 and not (y-1) < 0:
				if board[y-1][x-1] == "empty":
					drawPiece(x-1,y-1,"MoveOption")
					tempBoard[y-1][x-1] = "MoveOption"
					canMove = True
				elif (board[y-1][x-1])[0] == "b":
					drawPiece(x-1,y-1,"KillOption")
					tempBoard[y-1][x-1] = "KillOption"
					canMove = True
			if not (x+1) > 7 and not (y-1) < 0:
				if board[y-1][x+1] == "empty":
					drawPiece(x+1,y-1,"MoveOption")
					tempBoard[y-1][x+1] = "MoveOption"
					canMove = True
				elif (board[y-1][x+1])[0] == "b":
					drawPiece(x+1,y-1,"KillOption")
					tempBoard[y-1][x+1] = "KillOption"
					canMove = True
			if not (x-1) < 0 and not (y+1) > 7:
				if board[y+1][x-1] == "empty":
					drawPiece(x-1,y+1,"MoveOption")
					tempBoard[y+1][x-1] = "MoveOption"
					canMove = True
				elif (board[y+1][x-1])[0] == "b":
					drawPiece(x-1,y+1,"KillOption")
					tempBoard[y+1][x-1] = "KillOption"
					canMove = True
			if not (x+1) > 7 and not (y+1) > 7:
				if board[y+1][x+1] == "empty":
					drawPiece(x+1,y+1,"MoveOption")
					tempBoard[y+1][x+1] = "MoveOption"
					canMove = True
				elif (board[y+1][x+1])[0] == "b":
					drawPiece(x+1,y+1,"KillOption")
					tempBoard[y+1][x+1] = "KillOption"
					canMove = True
	while rightButtonPressed() == False and canMove == True and not closed():
		mBoardY = mouseY()//50
		mBoardX = mouseX()//50
		if tempBoard[mBoardY][mBoardX] == "MoveOption":
			if leftButtonPressed() == True:
				board[mBoardY][mBoardX] = piece
				board[y][x] = "empty"
				if CURRENT_TURN == "White":
					CURRENT_TURN = "Black"
				elif CURRENT_TURN == "Black": 
					CURRENT_TURN = "White"
				break
		elif tempBoard[mBoardY][mBoardX] == "KillOption":
			if leftButtonPressed() == True:
				if board[mBoardY][mBoardX] == "wKing":
					WINNER = "Black"
				elif board[mBoardY][mBoardX] == "bKing":
					WINNER = "White"
				board[mBoardY][mBoardX] = piece
				board[y][x] = "empty"
				if CURRENT_TURN == "White":
					CURRENT_TURN = "Black"
				elif CURRENT_TURN == "Black":
					CURRENT_TURN = "White"
				break
	return board

def main():
	global CURRENT_TURN
	if menu() == True:
		board = newBoard()
		drawCurrentBoard(board)
		while not closed():
			mY = mouseY()
			mX = mouseX()
			if not mX < 0 and not mX > xWINDOW and not mY < 0 and not mY > yWINDOW:
				if not mX < 0 and not mX > 400 and not mY < 0 and not mY > 400:
					mBoardY = mY//50
					mBoardX = mX//50
					if leftButtonPressed() == True:
						if board[mBoardY][mBoardX] != "empty":
							board = checkMoves(board,board[mBoardY][mBoardX],mBoardY,mBoardX)
							drawCurrentBoard(board)
					if WINNER != "":
						break
		setFont("Times","60","Bold")
		setColor(255,0,0)
		text(xWINDOW//2,yWINDOW//2,WINNER+" WINS")
CURRENT_TURN = "White"
WINNER = ""
setAutoUpdate(False)
xWINDOW = 0
yWINDOW = 0
main()