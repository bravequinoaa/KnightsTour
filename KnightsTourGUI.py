import pygame

# Prob have to slow down (sleep?)
# timer
# arrow for path

# Init Gui

pygame.init()


# Window Size
WIN_DIMENSION = 800

win = pygame.display.set_mode((WIN_DIMENSION, WIN_DIMENSION))
pygame.display.set_caption("Knights Tour")


# Board Size
N = 8

TARGETMOVES = N**2

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (180, 0, 0)

def DisplayGui(board, final=False):
	# run = True
	# while run:
	win.fill(black)
	
	for i in range(N):
		ydraw = i * (WIN_DIMENSION/N)
		for n in range(N):
			xdraw = n * (WIN_DIMENSION / N)
			pygame.draw.rect(win, red, (xdraw, ydraw, WIN_DIMENSION/N, WIN_DIMENSION/N), 3)
			displayText(board[i][n], xdraw, ydraw)
			
	while final:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				final = False
				print("CLOSING")

	
	pygame.display.update()


def text_objects(text, font):
	textSurface = font.render(str(text), True, white)
	return textSurface, textSurface.get_rect()


def displayText(text, xdraw, ydraw):
	font = pygame.font.Font('freesansbold.ttf', 7 * N)
	TextSurf, TextRect = text_objects(text, font)
	TextRect.center = ((xdraw + (WIN_DIMENSION / N) / 2), (ydraw + (WIN_DIMENSION / N) / 2))
	win.blit(TextSurf, TextRect)


def checkValid(board, movx, movy):
	'''
		params:
		movx => next x move
		movy => next y move
		
		checks if move is valid
	'''
	if (movx >= 0 and movy >= 0 and movx < N and movy < N and board[movx][movy] == " "):
		return True
	return False


def printBoard(board):
	'''
		Prints Board
	'''
	for i in range(len(board)):
		print(board[i])


def KnightsTour():
	currx = 0
	curry = 0

	# Init board
	board = [[" " for i in range(N)] for i in range(N)]

	xmoves = [-2, -2, -1, -1, 1, 1, 2, 2]
	ymoves = [1, -1, 2, -2, 2, -2, 1, -1]

	totalmoves = 1

	board[0][0] = 0
	DisplayGui(board)

	if generateMove(board, currx, curry, totalmoves, xmoves, ymoves):
		printBoard(board)
		DisplayGui(board, True)
	else: print("Invalid")
	

	


def generateMove(board, currx, curry, totalmoves, xmoves, ymoves):
	if totalmoves == TARGETMOVES:
		return True

	print("X: {} <> Y: {}".format(currx, curry)) # draw  board here


	for i in range(8):

		nextx = currx + xmoves[i]
		nexty = curry + ymoves[i]

		if checkValid(board, nextx, nexty):
			board[nextx][nexty] = totalmoves

			if generateMove(board, nextx, nexty, totalmoves+1, xmoves, ymoves):
				return True
			# backtracking
			board[nextx][nexty] = " "

	return False


if __name__ == "__main__":
	KnightsTour()
	