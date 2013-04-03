#!/usr/bin/env python

import sys
import random

# Import game modules
from gameio import GameIO
from gamemap import GameMap
from ai import PlayerAI
import tiles
import cards
import players


# Create IO interface, map and players
gameIO = GameIO()
gameMap = GameMap(10, 10)
ai = PlayerAI()
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
gin = gameIO.Input('The game is about to start.\na (auto) to automatically run game until end\ns (step) to manually step through game turns\n')

autoplay = gin == 'a' or gin == 'auto'
autoplayMax = 1000
turn = 0

ai.Reset()
ai.SetMap(gameMap)

while (not autoplay and gameMap.TileExists(tiles.Unexplored)) or (autoplay and turn < autoplayMax and gameMap.TileExists(tiles.Unexplored)):
	for player in playerList:
		
		#@@ Start of turn
		gameIO.Clear()
		turn += 1
		print 'Turn ' + str(turn) + ': ' + player.name
		
		#@@ Player AI
		ai.SetPlayer(player)
		ai.MoveToUnexplored()

		if gameMap.TileGet(player.pos[0], player.pos[1]) == tiles.Unexplored:
			# Discover a new location
			newLocation = discoveryCardPile.TakeTopCard()
			gameMap.TileSet(player.pos[0], player.pos[1], newLocation.tile)

			# Put card in discard pile
			discoveryDiscardPile.AddCard(newLocation)
		else:
			newLocation = cards.VoidCard()

		#@@ Render map
		gameMap.RenderMap(gameIO, player.pos)

		#@@ Event output
		if newLocation.tile != tiles.Invalid:
			gameIO.PrintLine('Discovered a new location: ' + newLocation.name)
		if newLocation.category == 'Dragon':
			gameIO.PrintLine('It\'s a dragon!')

		#@@ End of turn
		if not autoplay:
			rin = gameIO.Wait()
			if rin != '':
				sys.exit()