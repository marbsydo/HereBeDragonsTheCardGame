#!/usr/bin/env python

import sys
import random
import os

def enum(*sequential, **named):
	enums = dict(zip(sequential, range(len(sequential))), **named)
	return type('Enum', (), enums)

Tile = enum('None', 'Any', 'Unexplored', 'Town' ,'OpenOcean', 'TreasureIsland', 'Whirlpool', 'Whirlwind', 'Tempest', 'Shipwreck')

class GameIO:
	def Clear(self):
		os.system(['clear', 'cls'][os.name == 'nt'])

	def PrintBasic(self, text):
		sys.stdout.write(text)

	def MakeString(self, text, colour = -1, textOrBackground = 'text'):
		if colour < 0:
			return text
		else:
			if textOrBackground == 'background':
				pre = self.ColourBackground(colour)
			elif textOrBackground == 'text':
				pre = self.ColourText(colour)
			else:
				pre = self.ColourReset()
			return pre + text + self.ColourReset()

	def Print(self, text, colour = -1, textOrBackground = 'text'):
		self.PrintBasic(self.MakeString(text, colour, textOrBackground))

	def PrintLine(self, text = '', colour = -1, textOrBackground = 'text'):
		self.PrintBasic(self.MakeString(text + '\n', colour, textOrBackground))

	def ColourText(self, colour):
		return '\033[1;3' + str(self.ColourToNumber(colour)) + 'm'

	def ColourBackground(self, colour):
		return '\033[1;4' + str(self.ColourToNumber(colour)) + 'm'

	def ColourReset(self):
		return '\033[1;m'

	def ColourToNumber(self, colour):
		return {
		'default': -1,
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

	def Input(self, text):
		return raw_input(text)

	def Wait(self):
		return self.Input('Press <enter> to continue\n')

class GameMap:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.tiles = {(x,y):Tile.Unexplored for x in range(width) for y in range (height)}
		self.TileSet(0, 0, Tile.Town)
		self.TileSet(0, height - 1, Tile.Town)
		self.TileSet(width - 1, 0, Tile.Town)
		self.TileSet(width - 1, height - 1, Tile.Town)

	def TileGet(self, x, y):
		return self.tiles[(x, y)]

	def TileSet(self, x, y, tile):
		self.tiles[(x, y)] = tile

	def TileExists(self, tile):
		for x in range(0, self.width):
			for y in range(0, self.height):
				if self.tiles[(x, y)] == tile:
					return True
		return False

	def Print(self):
		for x in range(0, self.width):
			for y in range(0, self.height):
				sys.stdout.write(self.TileGet(x, y).CharGet())
			sys.stdout.write('\n')

# Base card
class Card:
	def __init__(self):
		self.name = 'Undefined Card'
		self.tile = Tile.None

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
		self.tile = Tile.OpenOcean

class TreasureIsland(LocationCard):
	def __init__(self):
		self.name = 'Treasure Island'
		self.tile = Tile.TreasureIsland

class Whirlwind(LocationCard):
	def __init__(self):
		self.name = 'Whirlwind'
		self.tile = Tile.Whirlwind

class Whirlpool(LocationCard):
	def __init__(self):
		self.name = 'Whirlpool'
		self.tile = Tile.Whirlpool

class Tempest(LocationCard):
	def __init__(self):
		self.name = 'Tempest'
		self.tile = Tile.Tempest

class Shipwreck(LocationCard):
	def __init__(self):
		self.name = 'Shipwreck'
		self.tile = Tile.Shipwreck

# Individual cards - dragons
class WindLeviathan(DragonCard):
	def __init__(self):
		self.name = 'Wind Leviathan'
		self.tile = Tile.Whirlwind

class WindWyrm(DragonCard):
	def __init__(self):
		self.name = 'Wind Wyrm'
		self.tile = Tile.Whirlwind

class OceanLeviathan(DragonCard):
	def __init__(self):
		self.name = 'Ocean Leviathan'
		self.tile = Tile.Whirlpool

class OceanWyrm(DragonCard):
	def __init__(self):
		self.name = 'Ocean Wyrm'
		self.tile = Tile.Whirlpool

class StormLeviathan(DragonCard):
	def __init__(self):
		self.name = 'Storm Leviathan'
		self.tile = Tile.Tempest

class StormWyrm(DragonCard):
	def __init__(self):
		self.name = 'Storm Wyrm'
		self.tile = Tile.Tempest

class GhostLeviathan(DragonCard):
	def __init__(self):
		self.name = 'Ghost Leviathan'
		self.tile = Tile.Shipwreck

class GhostWyrm(DragonCard):
	def __init__(self):
		self.name = 'Ghost Wyrm'
		self.tile = Tile.Shipwreck

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
		self.tile = Tile.Whirlwind

class OceanAmulet(AmuletCard):
	def __init__(self):
		self.name = 'Ocean Amulet'
		self.victoryPoints = 1;
		self.tile = Tile.Whirlpool

class StormAmulet(AmuletCard):
	def __init__(self):
		self.name = 'Storm Amulet'
		self.victoryPoints = 1;
		self.tile = Tile.Tempest

class GhostAmulet(AmuletCard):
	def __init__(self):
		self.name = 'Ghost Amulet'
		self.victoryPoints = 1;
		self.tile = Tile.Shipwreck

class DragonAmulet(AmuletCard):
	def __init__(self):
		self.name = 'Dragon Amulet'
		self.victoryPoints = 2;
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

discoveryDiscardPile = CardPile()
treasureDiscardPile = CardPile()
discoveryCardPile = CardPile(discoveryDiscardPile)
treasureCardPile = CardPile(treasureDiscardPile)

discoveryCardPile.AddCard(OpenOcean(), 4)
discoveryCardPile.AddCard(TreasureIsland(), 4)
discoveryCardPile.AddCard(Whirlwind(), 2)
discoveryCardPile.AddCard(Whirlpool(), 2)
discoveryCardPile.AddCard(Tempest(), 2)
discoveryCardPile.AddCard(Shipwreck(), 2)
discoveryCardPile.AddCard(WindLeviathan())
discoveryCardPile.AddCard(WindWyrm())
discoveryCardPile.AddCard(OceanLeviathan())
discoveryCardPile.AddCard(OceanWyrm())
discoveryCardPile.AddCard(StormLeviathan())
discoveryCardPile.AddCard(StormWyrm())
discoveryCardPile.AddCard(GhostLeviathan())
discoveryCardPile.AddCard(GhostWyrm())
discoveryCardPile.Shuffle()

treasureCardPile.AddCard(Gold(), 3),
treasureCardPile.AddCard(Jewels(), 3),
treasureCardPile.AddCard(Map(), 3),
treasureCardPile.AddCard(Rum(), 3),
treasureCardPile.AddCard(WindAmulet(), 2),
treasureCardPile.AddCard(OceanAmulet(), 2),
treasureCardPile.AddCard(StormAmulet(), 2),
treasureCardPile.AddCard(GhostAmulet(), 2),
treasureCardPile.AddCard(DragonAmulet(), 2),
treasureCardPile.Shuffle()

card = discoveryCardPile.TakeTopCard()
print card.name

class Player:
	def __init__(self, name, pos):
		self.name = name
		self.pos = pos
		self.loot = CardPile()
		self.trouble = CardPile()

gameIO = GameIO()

# Create map for the game with dimensions 8x8
map = GameMap(9, 9)

# Create players
players = [
Player('Jolly Rodger', [0, 0]),
Player('Octopus Brine', [0, map.height - 1]),
Player('Zanzibar', [map.width - 1, 0]),
Player('Going Merry', [map.width - 1, map.height - 1])
]


def TileToSymbol(tile):
	return {
		Tile.Unexplored: ' ',
		Tile.Town: 'T',
		Tile.OpenOcean: '~',
		Tile.TreasureIsland: 'X',
		Tile.Whirlpool: 'o',
		Tile.Whirlwind: '*',
		Tile.Tempest: '^',
		Tile.Shipwreck: '&',
	}.get(tile, '?')

def TileToColour(tile):
	return {
		Tile.Unexplored: 'default',
		Tile.Town: 'default',
		Tile.OpenOcean: 'blue',
		Tile.TreasureIsland: 'yellow',
		Tile.Whirlpool: 'magenta',
		Tile.Whirlwind: 'cyan',
		Tile.Tempest: 'red',
		Tile.Shipwreck: 'crimson'
	}.get(tile, 'grey')

def TileToColourSymbol(tile):
	return gameIO.MakeString(TileToSymbol(tile), TileToColour(tile))

def RenderMap(pos = [-1, -1]):
	key = [
	TileToColourSymbol(Tile.Whirlpool) + ' = Whirlpool   ' + TileToColourSymbol(Tile.TreasureIsland) + ' = Treasure Island',
	TileToColourSymbol(Tile.Whirlwind) + ' = Whirlwind   ' + TileToColourSymbol(Tile.Town) + ' = Town',
	TileToColourSymbol(Tile.Tempest) + ' = Tempest     ' + TileToColourSymbol(Tile.OpenOcean) + ' = Open ocean',
	TileToColourSymbol(Tile.Shipwreck) + ' = Shipwreck',
	]

	for y in range(0, map.width):
		for x in range(0, map.height):
			tile = map.TileGet(x, y)

			if x == pos[0] and y == pos[1]:
				tileString = gameIO.MakeString(TileToSymbol(tile), 'red', 'background')
			else:
				tileString = gameIO.MakeString(TileToSymbol(tile), TileToColour(tile), 'text')
			gameIO.Print(tileString + ' ')
		if y < len(key):
			gameIO.PrintLine(' ' + key[y])
		else:
			gameIO.PrintLine()

gameIO.Clear()
gameIO.PrintLine('Here be Dragons: The Card Game: The Simulator')
RenderMap()
gameIO.PrintLine('There are ' + str(len(players)) + ' players:')
for player in players:
	gameIO.PrintLine('* ' + player.name)
gameIO.PrintLine('The game is about to start.')
gameIO.Wait()

turn = 0
while map.TileExists(Tile.Unexplored):
	for player in players:
		# Start of turn - clear, show player info
		gameIO.Clear()
		turn += 1
		print 'Turn ' + str(turn) + ': ' + player.name

		# Player movement
		px = player.pos[0]
		py = player.pos[1]
		px += random.randint(-1, 1)
		py += random.randint(-1, 1)
		if px < 0:
			px = 0
		if py < 0:
			py = 0
		if px > map.width - 1:
			px = map.width - 1
		if py > map.height - 1:
			py = map.height - 1

		player.pos = (px, py)

		if map.TileGet(player.pos[0], player.pos[1]) == Tile.Unexplored:
			# Discover a new location
			newLocation = discoveryCardPile.TakeTopCard()
			map.TileSet(px, py, newLocation.tile)

			# Put card in discard pile
			discoveryDiscardPile.AddCard(newLocation)
		else:
			newLocation = Tile.None

		# Render map
		RenderMap(player.pos)

		if newLocation != Tile.None:
			gameIO.PrintLine('Discovered a new location: ' + newLocation.name)

		# End of turn - allow chance to quit game
		rin = gameIO.Wait()
		if rin != '':
			sys.exit()