import cards

class Player:
	def __init__(self, name, pos):
		self.name = name
		self.pos = pos
		self.loot = cards.CardPile()
		self.trouble = cards.CardPile()
		self.victoryPoints = 0

	def FindAdjacentTiles(self, gameMap):
		# Returns tuple of (position, tile type)
		adjacentTiles = []
		for x in range(max(self.GetX() - 1, 0), min(self.GetX() + 2, gameMap.width)):
			for y in range(max(self.GetY() - 1, 0), min(self.GetY() + 2, gameMap.height)):
				adjacentTiles.append(((x, y), gameMap.TileGet(x, y)))
		return adjacentTiles

	def FindAdjacentTilesSimple(self, gameMap):
		# Returns positions
		adjacentTiles = []
		for x in range(max(self.GetX() - 1, 0), min(self.GetX() + 2, gameMap.width)):
			for y in range(max(self.GetY() - 1, 0), min(self.GetY() + 2, gameMap.height)):
				adjacentTiles.append((x, y))
		return adjacentTiles

	def MoveToPos(self, pos, gameMap):
		# Verify move was legal
		adjacentTiles = self.FindAdjacentTilesSimple(gameMap)
		if pos in adjacentTiles:
			self.pos = pos
		else:
			raise Exception('Invalid AI movement!\nPossible movments: ' + str(adjacentTiles) + '\nChosen (invalid) movement: ' + str(pos))

	def GetX(self):
		return self.pos[0]

	def GetY(self):
		return self.pos[1]

def GenerateDefaultPlayers(gameMapWidth, gameMapHeight):
	return [
	Player('Jolly Rodger', [0, 0]),
	Player('Octopus Brine', [0, gameMapHeight - 1]),
	Player('Zanzibar', [gameMapWidth - 1, 0]),
	Player('Going Merry', [gameMapWidth - 1, gameMapHeight - 1])
	]