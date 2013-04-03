import cards
import tiles

'''
When AI accesses the Player class, it should only call the functions.
AI should never directly modify any class variables.
'''

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
		for x in range(max(self.pos[0] - 1, 0), min(self.pos[0] + 2, gameMap.width)):
			for y in range(max(self.pos[1] - 1, 0), min(self.pos[1] + 2, gameMap.height)):
				adjacentTiles.append(((x, y), gameMap.TileGet(x, y)))
		return adjacentTiles

	def FindAdjacentTilesSimple(self, gameMap):
		# Returns positions
		adjacentTiles = []
		for x in range(max(self.pos[0] - 1, 0), min(self.pos[0] + 2, gameMap.width)):
			for y in range(max(self.pos[1] - 1, 0), min(self.pos[1] + 2, gameMap.height)):
				adjacentTiles.append((x, y))
		return adjacentTiles

	def MoveToPos(self, gameData, pos):
		# Verify move was legal
		adjacentTiles = self.FindAdjacentTilesSimple(gameData.gameMap)
		if pos in adjacentTiles:
			self.pos = pos
			self.PostMovementCheck(gameData)
		else:
			raise Exception('Invalid AI movement!\nPossible movments: ' + str(adjacentTiles) + '\nChosen (invalid) movement: ' + str(pos))

	def PostMovementCheck(self, gameData):
		if gameData.gameMap.TileGet(self.pos[0], self.pos[1]) == tiles.Unexplored:
			# Discover a new location
			newLocation = gameData.discoveryCardPile.TakeTopCard()
			gameData.gameMap.TileSet(self.pos[0], self.pos[1], newLocation.tile)

			# Put card in discard pile
			gameData.discoveryDiscardPile.AddCard(newLocation)
		else:
			newLocation = cards.VoidCard()

		# Event output
		if newLocation.tile != tiles.Invalid:
			gameData.gameIO.messages.Add('Discovered a new location: ' + newLocation.name)
		if newLocation.category == 'Dragon':
			gameData.gameIO.messages.Add('It\'s a dragon!')

def GenerateDefaultPlayers(gameData):
	return [
	Player('Jolly Rodger', [0, 0]),
	Player('Octopus Brine', [0, gameData.gameMap.height - 1]),
	Player('Zanzibar', [gameData.gameMap.width - 1, 0]),
	Player('Going Merry', [gameData.gameMap.width - 1, gameData.gameMap.height - 1])
	]