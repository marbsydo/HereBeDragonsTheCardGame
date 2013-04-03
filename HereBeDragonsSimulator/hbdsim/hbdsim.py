#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import random

import tiles
import cards
import gameio
import gamemap
import players

gameIO = gameio.GameIO()
gameMap = gamemap.GameMap(10, 10)
playerList = players.GenerateDefaultPlayers(gameMap.width, gameMap.height)

discoveryDiscardPile = cards.CardPile()
treasureDiscardPile = cards.CardPile()
discoveryCardPile = cards.CardPile(discoveryDiscardPile)
treasureCardPile = cards.CardPile(treasureDiscardPile)

discoveryCardPile.AddCard(cards.OpenOcean(), 4)
discoveryCardPile.AddCard(cards.TreasureIsland(), 6)
discoveryCardPile.AddCard(cards.MerchantShip(), 2)
discoveryCardPile.AddCard(cards.Whirlwind(), 2)
discoveryCardPile.AddCard(cards.Whirlpool(), 2)
discoveryCardPile.AddCard(cards.Tempest(), 2)
discoveryCardPile.AddCard(cards.Shipwreck(), 2)
discoveryCardPile.AddCard(cards.WindHydra())
discoveryCardPile.AddCard(cards.WindLeviathan())
discoveryCardPile.AddCard(cards.WindWyrm())
discoveryCardPile.AddCard(cards.OceanKraken())
discoveryCardPile.AddCard(cards.OceanLeviathan())
discoveryCardPile.AddCard(cards.OceanWyrm())
discoveryCardPile.AddCard(cards.StormCthulhu())
discoveryCardPile.AddCard(cards.StormLeviathan())
discoveryCardPile.AddCard(cards.StormWyrm())
discoveryCardPile.AddCard(cards.GhostFlyingDutchman())
discoveryCardPile.AddCard(cards.GhostLeviathan())
discoveryCardPile.AddCard(cards.GhostWyrm())
discoveryCardPile.Shuffle()

treasureCardPile.AddCard(cards.Gold(), 3),
treasureCardPile.AddCard(cards.Jewels(), 3),
treasureCardPile.AddCard(cards.Map(), 3),
treasureCardPile.AddCard(cards.Rum(), 3),
treasureCardPile.AddCard(cards.WindAmulet(), 2),
treasureCardPile.AddCard(cards.OceanAmulet(), 2),
treasureCardPile.AddCard(cards.StormAmulet(), 2),
treasureCardPile.AddCard(cards.GhostAmulet(), 2),
treasureCardPile.AddCard(cards.DragonAmulet(), 2),
treasureCardPile.Shuffle()

def NumberToTally(number):
	fives = int(number) / 5
	remainder = number - fives * 5
	return '||||/ ' * fives + '|' * remainder

def TileToSymbol(tile):
	return {
		tiles.Unexplored: ' ',
		tiles.Town: 'T',
		tiles.OpenOcean: '~',
		tiles.TreasureIsland: 'X',
		tiles.MerchantShip: '$',
		tiles.Whirlpool: 'o',
		tiles.Whirlwind: '*',
		tiles.Tempest: '^',
		tiles.Shipwreck: '&',
	}.get(tile, '?')

def TileToColour(tile):
	return {
		tiles.Unexplored: 'default',
		tiles.Town: 'default',
		tiles.OpenOcean: 'blue',
		tiles.TreasureIsland: 'yellow',
		tiles.MerchantShip: 'green',
		tiles.Whirlpool: 'magenta',
		tiles.Whirlwind: 'cyan',
		tiles.Tempest: 'red',
		tiles.Shipwreck: 'crimson'
	}.get(tile, 'grey')

def TileToColourSymbol(tile):
	return gameIO.MakeString(TileToSymbol(tile), TileToColour(tile))

def RenderMap(pos = [-1, -1]):
	key = [
	TileToColourSymbol(tiles.Whirlpool) + ' = Whirlpool   ' + TileToColourSymbol(tiles.TreasureIsland) + ' = Treasure Island',
	TileToColourSymbol(tiles.Whirlwind) + ' = Whirlwind   ' + TileToColourSymbol(tiles.Town) + ' = Town',
	TileToColourSymbol(tiles.Tempest) + ' = Tempest     ' + TileToColourSymbol(tiles.MerchantShip) + ' = Merchant Ship',
	TileToColourSymbol(tiles.Shipwreck) + ' = Shipwreck   ' + TileToColourSymbol(tiles.OpenOcean) + ' = Open ocean',
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
gameIO.PrintLine('There are ' + str(len(playerList)) + ' players:')
for player in playerList:
	gameIO.PrintLine('* ' + player.name)
gameIO.PrintLine('The game is about to start.')
gin = gameIO.Input('a (auto) to automatically run game until end\ns (step) to manually step through game turns\n')

autoplay = gin == 'a' or gin == 'auto'
autoplayMax = 1000

turn = 0
while (not autoplay and gameMap.TileExists(tiles.Unexplored)) or (autoplay and turn < autoplayMax and gameMap.TileExists(tiles.Unexplored)):
	for player in playerList:
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
			if adjacentTile[1] == tiles.Unexplored:
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

		if gameMap.TileGet(player.pos[0], player.pos[1]) == tiles.Unexplored:
			# Discover a new location
			newLocation = discoveryCardPile.TakeTopCard()
			gameMap.TileSet(px, py, newLocation.tile)

			# Put card in discard pile
			discoveryDiscardPile.AddCard(newLocation)
		else:
			newLocation = cards.VoidCard()

		# Render map
		RenderMap(player.pos)

		if newLocation.tile != tiles.Invalid:
			gameIO.PrintLine('Discovered a new location: ' + newLocation.name)
		if newLocation.category == 'Dragon':
			gameIO.PrintLine('It\'s a dragon!')

		# End of turn - allow chance to quit game
		if not autoplay:
			rin = gameIO.Wait()
			if rin != '':
				sys.exit()