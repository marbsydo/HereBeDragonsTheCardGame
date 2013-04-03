import random

def enum(*sequential, **named):
	enums = dict(zip(sequential, range(len(sequential))), **named)
	return type('Enum', (), enums)

Tile = enum('None', 'Any', 'Unexplored', 'Town' ,'OpenOcean', 'TreasureIsland', 'MerchantShip', 'Whirlpool', 'Whirlwind', 'Tempest', 'Shipwreck')

# Base card
class Card:
	def __init__(self):
		self.name = 'Undefined Card'
		self.tile = Tile.None

# Base card types
class VoidCard(Card):
	def __init__(self):
		self.category = 'Void'
		self.name = 'Void'
		self.tile = Tile.None

class LocationCard(Card):
	def __init__(self):
		self.category = 'Location'

class DragonCard(Card):
	def __init__(self):
		self.category = 'Dragon'

class TreasureCard(Card):
	def __init__(self):
		self.category = 'Treasure'

class AmuletCard(Card):
	def __init__(self):
		self.category = 'Amulet'

# Individual cards - locations
class OpenOcean(LocationCard):
	def __init__(self):
		LocationCard.__init__(self)
		self.name = 'Open Ocean'
		self.tile = Tile.OpenOcean

class TreasureIsland(LocationCard):
	def __init__(self):
		LocationCard.__init__(self)
		self.name = 'Treasure Island'
		self.tile = Tile.TreasureIsland

class MerchantShip(LocationCard):
	def __init__(self):
		LocationCard.__init__(self)
		self.name = 'Merchant Ship'
		self.tile = Tile.MerchantShip

class Whirlwind(LocationCard):
	def __init__(self):
		LocationCard.__init__(self)
		self.name = 'Whirlwind'
		self.tile = Tile.Whirlwind

class Whirlpool(LocationCard):
	def __init__(self):
		LocationCard.__init__(self)
		self.name = 'Whirlpool'
		self.tile = Tile.Whirlpool

class Tempest(LocationCard):
	def __init__(self):
		LocationCard.__init__(self)
		self.name = 'Tempest'
		self.tile = Tile.Tempest

class Shipwreck(LocationCard):
	def __init__(self):
		LocationCard.__init__(self)
		self.name = 'Shipwreck'
		self.tile = Tile.Shipwreck

# Individual cards - dragons
class WindHydra(DragonCard):
	def __init__(self):
		DragonCard.__init__(self)
		self.name = 'Hydra'
		self.tile = Tile.Whirlwind

class OceanKraken(DragonCard):
	def __init__(self):
		DragonCard.__init__(self)
		self.name = 'Kraken'
		self.tile = Tile.Whirlpool

class StormCthulhu(DragonCard):
	def __init__(self):
		DragonCard.__init__(self)
		self.name = 'Cthulhu'
		self.tile = Tile.Tempest

class GhostFlyingDutchman(DragonCard):
	def __init__(self):
		DragonCard.__init__(self)
		self.name = 'Cthulhu'
		self.tile = Tile.Shipwreck

class WindLeviathan(DragonCard):
	def __init__(self):
		DragonCard.__init__(self)
		self.name = 'Wind Leviathan'
		self.tile = Tile.Whirlwind

class OceanLeviathan(DragonCard):
	def __init__(self):
		DragonCard.__init__(self)
		self.name = 'Ocean Leviathan'
		self.tile = Tile.Whirlpool

class StormLeviathan(DragonCard):
	def __init__(self):
		DragonCard.__init__(self)
		self.name = 'Storm Leviathan'
		self.tile = Tile.Tempest

class GhostLeviathan(DragonCard):
	def __init__(self):
		DragonCard.__init__(self)
		self.name = 'Ghost Leviathan'
		self.tile = Tile.Shipwreck

class WindWyrm(DragonCard):
	def __init__(self):
		DragonCard.__init__(self)
		self.name = 'Wind Wyrm'
		self.tile = Tile.Whirlwind

class OceanWyrm(DragonCard):
	def __init__(self):
		DragonCard.__init__(self)
		self.name = 'Ocean Wyrm'
		self.tile = Tile.Whirlpool

class StormWyrm(DragonCard):
	def __init__(self):
		DragonCard.__init__(self)
		self.name = 'Storm Wyrm'
		self.tile = Tile.Tempest

class GhostWyrm(DragonCard):
	def __init__(self):
		DragonCard.__init__(self)
		self.name = 'Ghost Wyrm'
		self.tile = Tile.Shipwreck

# Individual cards - treasures
class Gold(TreasureCard):
	def __init__(self):
		TreasureCard.__init__(self)
		self.name = 'Gold'
		self.victoryPoints = 2

class Jewels(TreasureCard):
	def __init__(self):
		TreasureCard.__init__(self)
		self.name = 'Jewels'
		self.victoryPoints = 2

class Map(TreasureCard):
	def __init__(self):
		TreasureCard.__init__(self)
		self.name = 'Map'
		self.victoryPoints = 1

class Rum(TreasureCard):
	def __init__(self):
		TreasureCard.__init__(self)
		self.name = 'Rum'
		self.victoryPoints = 1

# Individual cards - amulets
class WindAmulet(AmuletCard):
	def __init__(self):
		AmuletCard.__init__(self)
		self.name = 'Wind Amulet'
		self.victoryPoints = 1
		self.tile = Tile.Whirlwind

class OceanAmulet(AmuletCard):
	def __init__(self):
		AmuletCard.__init__(self)
		self.name = 'Ocean Amulet'
		self.victoryPoints = 1
		self.tile = Tile.Whirlpool

class StormAmulet(AmuletCard):
	def __init__(self):
		AmuletCard.__init__(self)
		self.name = 'Storm Amulet'
		self.victoryPoints = 1
		self.tile = Tile.Tempest

class GhostAmulet(AmuletCard):
	def __init__(self):
		AmuletCard.__init__(self)
		self.name = 'Ghost Amulet'
		self.victoryPoints = 1
		self.tile = Tile.Shipwreck

class DragonAmulet(AmuletCard):
	def __init__(self):
		AmuletCard.__init__(self)
		self.name = 'Dragon Amulet'
		self.victoryPoints = 2
		self.tile = Tile.Any

class CardPile:
	def __init__(self, refillPile = None):
		self.EmptyCardPile()

		# When this pile is empty, take all cards from the refill pile and shuffle
		self.refillPile = refillPile

	def EmptyCardPile(self):
		self.cards = []

	def AddCard(self, card, quantity = 1):
		for x in range (0, quantity):
			self.cards.append(card)

	def Shuffle(self):
		random.shuffle(self.cards)

	def Show(self):
		for card in self.cards:
			print card.name

	def TakeTopCard(self):
		card = self.cards.pop()
		self.RefillIfNecessary()
		return card

	def RefillIfNecessary(self):
		# If there is a refill pile, take all its cards and shuffle
		if self.refillPile != None:
			if len(self.cards) == 0:
				for card in self.refillPile.cards:
					self.AddCard(card, 1)
				self.refillPile.EmptyCardPile()
				self.Shuffle()
