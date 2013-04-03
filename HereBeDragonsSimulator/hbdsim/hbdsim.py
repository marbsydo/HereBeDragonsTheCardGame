#!/usr/bin/env python

import sys
import random

# Import game modules
import tiles
import cards
import gameio
import gamemap
import players

# Create IO interface, map and players
gameIO = gameio.GameIO()
gameMap = gamemap.GameMap(10, 10)
playerList = players.GenerateDefaultPlayers(gameMap.width, gameMap.height)

# Create card piles
discoveryDiscardPile = cards.CardPile()
treasureDiscardPile = cards.CardPile()
discoveryCardPile = cards.CardPile(discoveryDiscardPile)
treasureCardPile = cards.CardPile(treasureDiscardPile)

# Populate discovery and treasure card piles
discoveryCardPile.PopulateWithDiscoveryCards()
treasureCardPile.PopulateWithTreasureCards()

gameIO.Clear()
gameIO.PrintLine('Here be Dragons: The Card Game: The Simulator')
gameMap.RenderMap(gameIO)
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
		gameMap.RenderMap(gameIO, player.pos)

		if newLocation.tile != tiles.Invalid:
			gameIO.PrintLine('Discovered a new location: ' + newLocation.name)
		if newLocation.category == 'Dragon':
			gameIO.PrintLine('It\'s a dragon!')

		# End of turn - allow chance to quit game
		if not autoplay:
			rin = gameIO.Wait()
			if rin != '':
				sys.exit()