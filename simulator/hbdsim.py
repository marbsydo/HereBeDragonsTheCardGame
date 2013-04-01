#!/usr/bin/env python

import sys
import random
import os

print "Here be Dragons: The Card Game: The Simulator\n"

clear = lambda: os.system(['clear', 'cls'][os.name == 'nt'])

def printTitle(s):
	sys.stdout.write('  ' + s + '  \n' + '=' * (len(s) + 4) + '\n')

def enum(*sequential, **named):
	enums = dict(zip(sequential, range(len(sequential))), **named)
	return type('Enum', (), enums)

TileType = enum('None', 'Any', 'Unexplored', 'Town' ,'OpenOcean', 'TreasureIsland', 'Whirlpool', 'Whirlwind', 'Storm', 'Shipwreck')

class GameOut:
	def PrintBasic(self, text):
		sys.stdout.write(text)

	def Print(self, text, colour = -1, background = False):
		if colour < 0:
			self.ColourReset()
		else:
			if background:
				self.ColourBackgroundSet(colour)
			else:
				self.ColourTextSet(colour)
		self.PrintBasic(text)
		self.ColourReset()

	def PrintLine(self, text):
		self.PrintBasic(text + '\n')

	def ColourTextSet(self, colour):
		self.PrintBasic('\033[1;3' + str(self.ColourToNumber(colour)) + 'm')

	def ColourBackgroundSet(self, colour):
		self.PrintBasic('\033[1;4' + str(self.ColourToNumber(colour)) + 'm')

	def ColourReset(self):
		self.PrintBasic('\033[1;m')

	def ColourToNumber(self, colour):
		return {
		'grey': 0,
		'red': 1,
		'green': 2,
		'yellow': 3,
		'blue': 4,
		'magenta': 5,
		'cyan': 6,
		'white': 7,
		'crimson': 8,
		'bold': 9
		}.get(colour, 9)

class Tile:
	def __init__(self, tileType):
		self.tileType = tileType

	def TypeGet(self):
		return self.tileType

	def CharGet(self):
		return {
			TileType.Unexplored: ' ',
			TileType.Town: 'T',
			TileType.OpenOcean: '~',
			TileType.TreasureIsland: 'X',
			TileType.Whirlpool: 'o',
			TileType.Whirlwind: '*',
			TileType.Storm: '^',
			TileType.Shipwreck: '&',
		}.get(self.tileType, '?')

class GameMap:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.tiles = {(x,y):Tile(TileType.Unexplored) for x in range(width) for y in range (height)}
		self.TileSet(0, 0, Tile(TileType.Town))
		self.TileSet(0, height - 1, Tile(TileType.Town))
		self.TileSet(width - 1, 0, Tile(TileType.Town))
		self.TileSet(width - 1, height - 1, Tile(TileType.Town))

	def TileGet(self, x, y):
		return self.tiles[(x, y)]

	def TileSet(self, x, y, tile):
		self.tiles[(x, y)] = tile

	def TileExists(self, tile):
		for x in range(0, self.width):
			for y in range(0, self.height):
				if self.tiles[(x, y)].TypeGet() == tile:
					return True
		return False

	def Print(self):
		for x in range(0, self.width):
			for y in range(0, self.height):
				sys.stdout.write('\033[1;31m')
				sys.stdout.write(self.TileGet(x, y).CharGet())
				sys.stdout.write('\033[1;m')
			sys.stdout.write('\n')

# Base card
class Card:
	def __init__(self):
		self.name = 'Undefined Card'
		self.tile = TileType.None

# Base card types
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
		self.name = 'Open Ocean'
		self.tile = TileType.OpenOcean

class TreasureIsland(LocationCard):
	def __init__(self):
		self.name = 'Treasure Island'
		self.tile = TileType.TreasureIsland

class Whirlwind(LocationCard):
	def __init__(self):
		self.name = 'Whirlwind'
		self.tile = TileType.Whirlwind

class Whirlpool(LocationCard):
	def __init__(self):
		self.name = 'Whirlpool'
		self.tile = TileType.Whirlpool

class Storm(LocationCard):
	def __init__(self):
		self.name = 'Storm'
		self.tile = TileType.Storm

class Shipwreck(LocationCard):
	def __init__(self):
		self.name = 'Shipwreck'
		self.tile = TileType.Shipwreck

# Individual cards - dragons
class WindLeviathan(DragonCard):
	def __init__(self):
		self.name = 'Wind Leviathan'
		self.tile = TileType.Whirlwind

class WindWyrm(DragonCard):
	def __init__(self):
		self.name = 'Wind Wyrm'
		self.tile = TileType.Whirlwind

class OceanLeviathan(DragonCard):
	def __init__(self):
		self.name = 'Ocean Leviathan'
		self.tile = TileType.Whirlpool

class OceanWyrm(DragonCard):
	def __init__(self):
		self.name = 'Ocean Wyrm'
		self.tile = TileType.Whirlpool

class StormLeviathan(DragonCard):
	def __init__(self):
		self.name = 'Storm Leviathan'
		self.tile = TileType.Storm

class StormWyrm(DragonCard):
	def __init__(self):
		self.name = 'Storm Wyrm'
		self.tile = TileType.Storm

class GhostLeviathan(DragonCard):
	def __init__(self):
		self.name = 'Ghost Leviathan'
		self.tile = TileType.Shipwreck

class GhostWyrm(DragonCard):
	def __init__(self):
		self.name = 'Ghost Wyrm'
		self.tile = TileType.Shipwreck

# Individual cards - treasures
class Gold(TreasureCard):
	def __init__(self):
		self.name = 'Gold'
		self.victoryPoints = 2;

class Jewels(TreasureCard):
	def __init__(self):
		self.name = 'Jewels'
		self.victoryPoints = 2;

class Map(TreasureCard):
	def __init__(self):
		self.name = 'Map'
		self.victoryPoints = 1;

class Rum(TreasureCard):
	def __init__(self):
		self.name = 'Rum'
		self.victoryPoints = 1;

# Individual cards - amulets
class WindAmulet(AmuletCard):
	def __init__(self):
		self.name = 'Wind Amulet'
		self.victoryPoints = 1;
		self.tile = TileType.Whirlwind

class OceanAmulet(AmuletCard):
	def __init__(self):
		self.name = 'Ocean Amulet'
		self.victoryPoints = 1;
		self.tile = TileType.Whirlpool

class StormAmulet(AmuletCard):
	def __init__(self):
		self.name = 'Storm Amulet'
		self.victoryPoints = 1;
		self.tile = TileType.Storm

class GhostAmulet(AmuletCard):
	def __init__(self):
		self.name = 'Ghost Amulet'
		self.victoryPoints = 1;
		self.tile = TileType.Shipwreck

class DragonAmulet(AmuletCard):
	def __init__(self):
		self.name = 'Dragon Amulet'
		self.victoryPoints = 2;
		self.tile = TileType.Any

class CardPile:
	def __init__(self):
		self.EmptyCardPile()

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
		return self.cards.pop()

class DiscoveryCardPile(CardPile):
	def __init__(self):
		CardPile.__init__(self)
		self.AddCard(OpenOcean(), 4)
		self.AddCard(TreasureIsland(), 8)
		self.AddCard(Whirlwind(), 2)
		self.AddCard(Whirlpool(), 2)
		self.AddCard(Storm(), 2)
		self.AddCard(Shipwreck(), 2)
		self.AddCard(WindLeviathan())
		self.AddCard(WindWyrm())
		self.AddCard(OceanLeviathan())
		self.AddCard(OceanWyrm())
		self.AddCard(StormLeviathan())
		self.AddCard(StormWyrm())
		self.AddCard(GhostLeviathan())
		self.AddCard(GhostWyrm())

class TreasureCardPile(CardPile):
	def __init__(self):
		CardPile.__init__(self)
		self.AddCard(Gold(), 3),
		self.AddCard(Jewels(), 3),
		self.AddCard(Map(), 3),
		self.AddCard(Rum(), 3),
		self.AddCard(WindAmulet(), 2),
		self.AddCard(OceanAmulet(), 2),
		self.AddCard(StormAmulet(), 2),
		self.AddCard(GhostAmulet(), 2),
		self.AddCard(DragonAmulet(), 2),

discoveryCardPile = DiscoveryCardPile()
discoveryCardPile.Shuffle()

treasureCardPile = TreasureCardPile()
treasureCardPile.Shuffle()

card = discoveryCardPile.TakeTopCard()
print card.name

class Player:
	def __init__(self, name, pos):
		self.name = name
		self.pos = pos
		self.loot = CardPile()
		self.trouble = CardPile()

gameOut = GameOut()

width = height = 8;

players = [
Player('Jolly Rodger', [0, 0]),
Player('Octopus Brine', [0, height - 1]),
Player('Zanzibar', [width - 1, 0]),
Player('Going Merry', [width - 1, height - 1])
]

map = GameMap(width, height)
map.Print()

turn = 0
while map.TileExists(TileType.Unexplored):
	for player in players:
		# Start of turn - clear, show map and current player
		clear()
		turn += 1
		print 'Turn ' + str(turn) + ': ' + player.name + str(player.pos)
		map.Print()

		gameOut.Print('Test post')

		# End of turn - allow chance to quit game
		rin = raw_input('Press <enter> to continue...\n')
		if rin != '':
			sys.exit()