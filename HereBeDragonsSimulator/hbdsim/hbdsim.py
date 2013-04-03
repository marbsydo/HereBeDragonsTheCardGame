#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import random
import os


from cards import *

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
		if x >= 0 and x < self.width and y >= 0 and y < self.height:
			return self.tiles[(x, y)]
		else:
			return Tile.None

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

class Player:
	def __init__(self, name, pos):
		self.name = name
		self.pos = pos
		self.loot = CardPile()
		self.trouble = CardPile()
		self.victoryPoints = 0

discoveryDiscardPile = CardPile()
treasureDiscardPile = CardPile()
discoveryCardPile = CardPile(discoveryDiscardPile)
treasureCardPile = CardPile(treasureDiscardPile)

discoveryCardPile.AddCard(OpenOcean(), 4)
discoveryCardPile.AddCard(TreasureIsland(), 6)
discoveryCardPile.AddCard(MerchantShip(), 2)
discoveryCardPile.AddCard(Whirlwind(), 2)
discoveryCardPile.AddCard(Whirlpool(), 2)
discoveryCardPile.AddCard(Tempest(), 2)
discoveryCardPile.AddCard(Shipwreck(), 2)
discoveryCardPile.AddCard(WindHydra())
discoveryCardPile.AddCard(WindLeviathan())
discoveryCardPile.AddCard(WindWyrm())
discoveryCardPile.AddCard(OceanKraken())
discoveryCardPile.AddCard(OceanLeviathan())
discoveryCardPile.AddCard(OceanWyrm())
discoveryCardPile.AddCard(StormCthulhu())
discoveryCardPile.AddCard(StormLeviathan())
discoveryCardPile.AddCard(StormWyrm())
discoveryCardPile.AddCard(GhostFlyingDutchman())
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

gameIO = GameIO()
gameMap = GameMap(10, 10)

# Create players
players = [
Player('Jolly Rodger', [0, 0]),
Player('Octopus Brine', [0, gameMap.height - 1]),
Player('Zanzibar', [gameMap.width - 1, 0]),
Player('Going Merry', [gameMap.width - 1, gameMap.height - 1])
]

def NumberToTally(number):
	fives = int(number) / 5
	remainder = number - fives * 5
	return '||||/ ' * fives + '|' * remainder

def TileToSymbol(tile):
	return {
		Tile.Unexplored: ' ',
		Tile.Town: 'T',
		Tile.OpenOcean: '~',
		Tile.TreasureIsland: 'X',
		Tile.MerchantShip: '$',
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
		Tile.MerchantShip: 'green',
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
	TileToColourSymbol(Tile.Tempest) + ' = Tempest     ' + TileToColourSymbol(Tile.MerchantShip) + ' = Merchant Ship',
	TileToColourSymbol(Tile.Shipwreck) + ' = Shipwreck   ' + TileToColourSymbol(Tile.OpenOcean) + ' = Open ocean',
	]
	gameIO.PrintLine('╔' + '═' * (gameMap.width * 2 + 1) + '╗')
	for y in range(0, gameMap.width):
		gameIO.Print('║ ')
		for x in range(0, gameMap.height):
			tile = gameMap.TileGet(x, y)

			if x == pos[0] and y == pos[1]:
				tileString = gameIO.MakeString(TileToSymbol(tile), 'red', 'background')
			else:
				tileString = TileToColourSymbol(tile)
			gameIO.Print(tileString + ' ')
		gameIO.Print('║')
		if y < len(key):
			gameIO.PrintLine(' ' + key[y])
		else:
			gameIO.PrintLine()
	gameIO.PrintLine('╚' + '═' * (gameMap.width * 2 + 1) + '╝')

gameIO.Clear()
gameIO.PrintLine('Here be Dragons: The Card Game: The Simulator')
RenderMap()
gameIO.PrintLine('There are ' + str(len(players)) + ' players:')
for player in players:
	gameIO.PrintLine('* ' + player.name)
gameIO.PrintLine('The game is about to start.')
gin = gameIO.Input('a (auto) to automatically run game until end\ns (step) to manually step through game turns\n')

autoplay = gin == 'a' or gin == 'auto'
autoplayMax = 1000

turn = 0
while (not autoplay and gameMap.TileExists(Tile.Unexplored)) or (autoplay and turn < autoplayMax and gameMap.TileExists(Tile.Unexplored)):
	for player in players:
		# Start of turn - clear, show player info
		gameIO.Clear()
		turn += 1
		print 'Turn ' + str(turn) + ': ' + player.name

		# Player movement
		
		# Find all adjacent tiles
		adjacentTiles = []
		for x in range(max(player.pos[0] - 1, 0), min(player.pos[0] + 2, gameMap.width)):
			for y in range(max(player.pos[1] - 1, 0), min(player.pos[1] + 2, gameMap.height)):
				adjacentTiles.append(((x, y), gameMap.TileGet(x, y)))
		random.shuffle(adjacentTiles)

		'''
		# Debug: Show potential tiles
		gameIO.Print('Potential: ')
		for adjacentTile in adjacentTiles:
			gameIO.Print('(' + str(adjacentTile[0][0]) + ',' + str(adjacentTile[0][1]) + ')')
		'''

		# Choose a random location, which is the default
		px = adjacentTiles[0][0][0]
		py = adjacentTiles[0][0][1]

		# Choose the first unexplored location
		# If none is found, the default is used (by default)
		for adjacentTile in adjacentTiles:
			if adjacentTile[1] == Tile.Unexplored:
				px = adjacentTile[0][0]
				py = adjacentTile[0][1]
				break

		'''
		# Debug: Show chosen tile
		gameIO.PrintLine(' Chosen:(' + str(px) + ',' + str(py) + ')')
		'''

		'''
		# Completely random movement
		px = player.pos[0]
		py = player.pos[1]
		px += random.randint(-1, 1)
		py += random.randint(-1, 1)
		if px < 0:
			px = 0
		if py < 0:
			py = 0
		if px > gameMap.width - 1:
			px = gameMap.width - 1
		if py > gameMap.height - 1:
			py = gameMap.height - 1
		'''

		player.pos = (px, py)

		if gameMap.TileGet(player.pos[0], player.pos[1]) == Tile.Unexplored:
			# Discover a new location
			newLocation = discoveryCardPile.TakeTopCard()
			gameMap.TileSet(px, py, newLocation.tile)

			# Put card in discard pile
			discoveryDiscardPile.AddCard(newLocation)
		else:
			newLocation = VoidCard()

		# Render map
		RenderMap(player.pos)

		if newLocation.tile != Tile.None:
			gameIO.PrintLine('Discovered a new location: ' + newLocation.name)
		if newLocation.category == 'Dragon':
			gameIO.PrintLine('It\'s a dragon!')

		# End of turn - allow chance to quit game
		if not autoplay:
			rin = gameIO.Wait()
			if rin != '':
				sys.exit()