#!/usr/bin/env python

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


# Create IO interface, map and players
gameIO = GameIO()
gameMap = GameMap(10, 10)
gameData = GameData(gameIO, gameMap)
ai = PlayerAI(gameData)
playerList = players.GenerateDefaultPlayers(gameData)

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

while (not autoplay and gameMap.TileExists(tiles.Unexplored)) or (autoplay and turn < autoplayMax and gameMap.TileExists(tiles.Unexplored)):
	for player in playerList:
		
		#@@ Start of turn
		gameIO.Clear()
		turn += 1
		print 'Turn ' + str(turn) + ': ' + player.name
		
		#@@ Player AI
		ai.SetPlayer(player)
		ai.MoveToUnexplored()

		#@@ Render map
		gameMap.RenderMap(gameIO, player.pos)

		#@@ Show any events that occurred
		gameIO.ShowAllMessages()

		#@@ End of turn
		if not autoplay:
			rin = gameIO.Wait()
			if rin != '':
				sys.exit()