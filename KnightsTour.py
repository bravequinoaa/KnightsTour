# Board matrix size
N = 8
TARGETMOVES = N**2

def printBoard(board):
	'''
		Prints Board
	'''
	for i in range(len(board)):
		print(board[i])

def checkValid(board, movx, movy):
	'''
		params:
		movx => next x move
		movy => next y move
		
		checks if move is valid
	'''
	if (movx >= 0 and movy >= 0 and movx < N and movy < N and board[movx][movy] == -1):
		return True
	return False

def generateMove(board, currx, curry, totalmoves, xmoves, ymoves):
	if totalmoves == TARGETMOVES:
		return True

	print("X: {} <> Y: {}".format(currx, curry))


	for i in range(8):

		nextx = currx + xmoves[i]
		nexty = curry + ymoves[i]

		if checkValid(board, nextx, nexty):
			board[nextx][nexty] = totalmoves

			if generateMove(board, nextx, nexty, totalmoves+1, xmoves, ymoves):
				return True
			board[nextx][nexty] = -1

	return False

if __name__ == "__main__":
	currx = 0
	curry = 0

	# Init board
	board = [[-1 for i in range(N)] for i in range(N)]

	xmoves = [-2, -2, -1, -1, 1, 1, 2, 2]
	ymoves = [1, -1, 2, -2, 2, -2, 1, -1]

	totalmoves = 1

	board[0][0] = 0

	if generateMove(board, currx, curry, totalmoves, xmoves, ymoves):
		printBoard(board)
	else: print("Invalid")