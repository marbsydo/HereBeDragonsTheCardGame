#!/usr/bin/env python

'''
TODO:
* Disallow player to be moved multiple times in one turn by AI
* Make players keep dragons and treasures
'''

import sys
import random

# Import game modules
from gameio import GameIO
from gamemap import GameMap
from gamedata import GameData
from ai import PlayerAI
import tiles
import cards
import players

# Create IO interface, map and card piles
gameIO = GameIO()
gameMap = GameMap(10, 10)
gameData = GameData(gameIO, gameMap)
ai = PlayerAI(gameData)

# Create players
playerList = players.GenerateDefaultPlayers(gameData)

# Clear the output console
gameIO.Clear()

# Show intro screen
gameIO.PrintLine('Here be Dragons: The Card Game: The Simulator')
gameMap.RenderMap(gameIO)
gameIO.PrintLine('There are ' + str(len(playerList)) + ' players:')
for player in playerList:
	gameIO.PrintLine('* ' + player.name)
gin = gameIO.Input('The game is about to start.\na (auto) to automatically run game until end\ns (step) to manually step through game turns\n')

# Autoplay and turn limit
autoplay = gin == 'a' or gin == 'auto'
autoplayMax = 1000

# Game loop
while (not autoplay and gameMap.TileExists(tiles.Unexplored)) or (autoplay and gameData.turn < autoplayMax and gameMap.TileExists(tiles.Unexplored)):
	for player in playerList:
		# Start of turn
		gameIO.Clear()
		print 'Turn ' + str(gameData.turn) + ': ' + player.name
		
		# Player AI
		ai.SetPlayer(player)
		ai.MoveToUnexplored()

		# Render map
		gameMap.RenderMap(gameIO, player.pos)

		# Show any events that occurred
		gameIO.ShowAllMessages()

		# End of turn
		if not autoplay and gameIO.Wait() != '':
			sys.exit()
		gameData.IncrementTurn()