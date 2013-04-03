import cards

class GameData():
	def __init__(self, gameIO, gameMap):
		self.gameIO = gameIO
		self.gameMap = gameMap

		# Create card piles
		self.discoveryDiscardPile = cards.CardPile()
		self.treasureDiscardPile = cards.CardPile()
		self.discoveryCardPile = cards.CardPile(self.discoveryDiscardPile)
		self.treasureCardPile = cards.CardPile(self.treasureDiscardPile)

		# Populate discovery and treasure card piles
		self.discoveryCardPile.PopulateWithDiscoveryCards()
		self.treasureCardPile.PopulateWithTreasureCards()