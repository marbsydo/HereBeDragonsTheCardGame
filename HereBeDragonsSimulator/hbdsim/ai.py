import random
import tiles

class PlayerAI():
	def __init__(self):
		self.Reset()

	def Reset(self):
		self.player = None
		self.gameMap = None

	def SetPlayer(self, player):
		self.player = player

	def SetMap(self, gameMap):
		self.gameMap = gameMap

	def MoveToUnexplored(self):
		# Get all tiles adjacent to current player
		adjacentTiles = self.player.FindAdjacentTiles(self.gameMap)

		# Shuffle these tiles randomly
		random.shuffle(adjacentTiles)

		# Choose the first unexplored location
		# If none is found, the first is used by default
		newLocation = (adjacentTiles[0][0][0], adjacentTiles[0][0][1])
		for adjacentTile in adjacentTiles:
			if adjacentTile[1] == tiles.Unexplored:
				newLocation = (adjacentTile[0][0], adjacentTile[0][1])
				break

		self.player.MoveToPos(newLocation, self.gameMap)

	def MoveRandomly(self):
		# Completely random movement
		px = self.player.pos[0]
		py = self.player.pos[1]
		px += random.randint(-1, 1)
		py += random.randint(-1, 1)
		if px < 0:
			px = 0
		if py < 0:
			py = 0
		if px > self.gameMap.width - 1:
			px = self.gameMap.width - 1
		if py > self.gameMap.height - 1:
			py = self.gameMap.height - 1
		newLocation = (px, py)

		self.player.MoveToPos(newLocation, self.gameMap)