from ConnectFiveMethod import detectDifferencePosition, getPositionFromAI
# will be deleted soon
from time import sleep

ROW = 19
COLUMN = 19
MAXSTONE = 5
BLANK = "-"
WHITE = "O"
BLACK = "X"
direction = {
	'w': (-1, 0),
	'e': (1, 0),
	'n': (0, -1),
	's': (0, 1),
	'nw': (-1, -1),
	'ne': (1, -1),
	'sw': (-1, 1),
	'se': (1, 1)
}

class Player():
	def __init__(self):
		self.mark = WHITE
		self.axis = ()
	def __str__(self):
		return "Human Player"
	def getMove(self):
	# will be deleted soon
		self.axis = detectDifferencePosition()
		return self.axis

class Computer(Player):
	def __init__(self):
		Player().__init__()
		self.mark = BLACK
	def __str__(self):
		return "AI Player"
	def getMove(self):
	# will be deleted soon
		self.axis = getPositionFromAI()
		return self.axis

class connectFive():
	def __init__(self):
		self.board = [BLANK * ROW] * COLUMN
		self.players = [Player(), Computer()]
		self.turn = 0
		self.round = 0
	def show(self):
		print("Move #{}: {}".format(self.round, self.players[self.turn]))
		print('\n'.join([i for i in self.board]))
		self.round += 1
		# will be deleted soon
		sleep(0.1)
	def setTurn(self):
		self.turn = 0 if self.turn else 1
	def currentPlayer(self):
		return self.players[self.turn]
	def reset(self):
		self.turn = 0
		self.round = 0
		self.board = [BLANK * ROW] * COLUMN

def updateStatus(envir,player):
	player.axis = player.getMove()
	while envir.board[player.axis[1]][player.axis[0]] != BLANK:
		player.axis = player.getMove()
	stone = BLACK if envir.turn else WHITE
	envir.board[player.axis[1]] = envir.board[player.axis[1]][:player.axis[0]] \
					+ stone \
					+ envir.board[player.axis[1]][player.axis[0] + 1:]

def getStatus(envir, player):
	for arrow in direction.values():
		match = 0
		for i in range(0, MAXSTONE + 1):
			if player.axis[1] + arrow[1] * i >= ROW \
				or player.axis[0] + arrow[0] * i >= COLUMN \
				or player.axis[1] + arrow[1] * i < 0 \
				or player.axis[0] + arrow[0] * i < 0:
				if match == 5:
					return True
				else:
					return False
			if envir.board[player.axis[1] + arrow[1] * i] \
					[player.axis[0] + arrow[0] * i] == player.mark:
				match += 1
			else:
				if match == 5:
					return True
				elif match > 5:
					break
				else:
					continue
	return False

def playGame(game):
	game.reset()
	isEnd = False
	while isEnd != True:
		game.show()
		updateStatus(game, game.currentPlayer())
		isEnd = getStatus(game, game.currentPlayer())
		game.setTurn()
		
def main():
	game = connectFive()
	playGame(game)

if __name__ == '__main__':
	main()
