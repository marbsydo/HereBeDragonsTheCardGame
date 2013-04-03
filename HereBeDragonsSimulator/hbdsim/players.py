import cards

class Player:
	def __init__(self, name, pos):
		self.name = name
		self.pos = pos
		self.loot = cards.CardPile()
		self.trouble = cards.CardPile()
		self.victoryPoints = 0

def GenerateDefaultPlayers(gameMapWidth, gameMapHeight):
	return [
	Player('Jolly Rodger', [0, 0]),
	Player('Octopus Brine', [0, gameMapHeight - 1]),
	Player('Zanzibar', [gameMapWidth - 1, 0]),
	Player('Going Merry', [gameMapWidth - 1, gameMapHeight - 1])
	]