import random
import tiles

# Base card
class Card:
	def __init__(self):
		self.name = 'Undefined Card'
		self.tile = tiles.Invalid

# Base card types
class VoidCard(Card):
	def __init__(self):
		self.category = 'Void'
		self.name = 'Void'
		self.tile = tiles.Invalid

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
		self.tile = tiles.OpenOcean

class TreasureIsland(LocationCard):
	def __init__(self):
		LocationCard.__init__(self)
		self.name = 'Treasure Island'
		self.tile = tiles.TreasureIsland

class MerchantShip(LocationCard):
	def __init__(self):
		LocationCard.__init__(self)
		self.name = 'Merchant Ship'
		self.tile = tiles.MerchantShip

class Whirlwind(LocationCard):
	def __init__(self):
		LocationCard.__init__(self)
		self.name = 'Whirlwind'
		self.tile = tiles.Whirlwind

class Whirlpool(LocationCard):
	def __init__(self):
		LocationCard.__init__(self)
		self.name = 'Whirlpool'
		self.tile = tiles.Whirlpool

class Tempest(LocationCard):
	def __init__(self):
		LocationCard.__init__(self)
		self.name = 'Tempest'
		self.tile = tiles.Tempest

class Shipwreck(LocationCard):
	def __init__(self):
		LocationCard.__init__(self)
		self.name = 'Shipwreck'
		self.tile = tiles.Shipwreck

# Individual cards - dragons
class WindHydra(DragonCard):
	def __init__(self):
		DragonCard.__init__(self)
		self.name = 'Hydra'
		self.tile = tiles.Whirlwind

class OceanKraken(DragonCard):
	def __init__(self):
		DragonCard.__init__(self)
		self.name = 'Kraken'
		self.tile = tiles.Whirlpool

class StormCthulhu(DragonCard):
	def __init__(self):
		DragonCard.__init__(self)
		self.name = 'Cthulhu'
		self.tile = tiles.Tempest

class GhostFlyingDutchman(DragonCard):
	def __init__(self):
		DragonCard.__init__(self)
		self.name = 'Cthulhu'
		self.tile = tiles.Shipwreck

class WindLeviathan(DragonCard):
	def __init__(self):
		DragonCard.__init__(self)
		self.name = 'Wind Leviathan'
		self.tile = tiles.Whirlwind

class OceanLeviathan(DragonCard):
	def __init__(self):
		DragonCard.__init__(self)
		self.name = 'Ocean Leviathan'
		self.tile = tiles.Whirlpool

class StormLeviathan(DragonCard):
	def __init__(self):
		DragonCard.__init__(self)
		self.name = 'Storm Leviathan'
		self.tile = tiles.Tempest

class GhostLeviathan(DragonCard):
	def __init__(self):
		DragonCard.__init__(self)
		self.name = 'Ghost Leviathan'
		self.tile = tiles.Shipwreck

class WindWyrm(DragonCard):
	def __init__(self):
		DragonCard.__init__(self)
		self.name = 'Wind Wyrm'
		self.tile = tiles.Whirlwind

class OceanWyrm(DragonCard):
	def __init__(self):
		DragonCard.__init__(self)
		self.name = 'Ocean Wyrm'
		self.tile = tiles.Whirlpool

class StormWyrm(DragonCard):
	def __init__(self):
		DragonCard.__init__(self)
		self.name = 'Storm Wyrm'
		self.tile = tiles.Tempest

class GhostWyrm(DragonCard):
	def __init__(self):
		DragonCard.__init__(self)
		self.name = 'Ghost Wyrm'
		self.tile = tiles.Shipwreck

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
		self.tile = tiles.Whirlwind

class OceanAmulet(AmuletCard):
	def __init__(self):
		AmuletCard.__init__(self)
		self.name = 'Ocean Amulet'
		self.victoryPoints = 1
		self.tile = tiles.Whirlpool

class StormAmulet(AmuletCard):
	def __init__(self):
		AmuletCard.__init__(self)
		self.name = 'Storm Amulet'
		self.victoryPoints = 1
		self.tile = tiles.Tempest

class GhostAmulet(AmuletCard):
	def __init__(self):
		AmuletCard.__init__(self)
		self.name = 'Ghost Amulet'
		self.victoryPoints = 1
		self.tile = tiles.Shipwreck

class DragonAmulet(AmuletCard):
	def __init__(self):
		AmuletCard.__init__(self)
		self.name = 'Dragon Amulet'
		self.victoryPoints = 2
		self.tile = tiles.Any

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

	def PopulateWithDiscoveryCards(self):
		self.EmptyCardPile()
		self.AddCard(OpenOcean(), 4)
		self.AddCard(TreasureIsland(), 6)
		self.AddCard(MerchantShip(), 2)
		self.AddCard(Whirlwind(), 2)
		self.AddCard(Whirlpool(), 2)
		self.AddCard(Tempest(), 2)
		self.AddCard(Shipwreck(), 2)
		self.AddCard(WindHydra())
		self.AddCard(WindLeviathan())
		self.AddCard(WindWyrm())
		self.AddCard(OceanKraken())
		self.AddCard(OceanLeviathan())
		self.AddCard(OceanWyrm())
		self.AddCard(StormCthulhu())
		self.AddCard(StormLeviathan())
		self.AddCard(StormWyrm())
		self.AddCard(GhostFlyingDutchman())
		self.AddCard(GhostLeviathan())
		self.AddCard(GhostWyrm())
		self.Shuffle()

	def PopulateWithTreasureCards(self):
		self.EmptyCardPile()
		self.AddCard(Gold(), 3),
		self.AddCard(Jewels(), 3),
		self.AddCard(Map(), 3),
		self.AddCard(Rum(), 3),
		self.AddCard(WindAmulet(), 2),
		self.AddCard(OceanAmulet(), 2),
		self.AddCard(StormAmulet(), 2),
		self.AddCard(GhostAmulet(), 2),
		self.AddCard(DragonAmulet(), 2),
		self.Shuffle()