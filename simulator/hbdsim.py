#!/usr/bin/env python

import sys

print "Here be Dragons: The Card Game: The Simulator\n"

def enum(*sequential, **named):
	enums = dict(zip(sequential, range(len(sequential))), **named)
	return type('Enum', (), enums)

TileType = enum('Unexplored', 'Town' ,'OpenOcean', 'TreasureIsland', 'Whirlpool', 'Whirlwind', 'Storm', 'Shipwreck')

class Tile:
	def __init__(self, tileType):
		self.tileType = tileType

	def GetChar(self):
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


class Map:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.tiles = {(x,y):Tile(TileType.OpenOcean) for x in range(width) for y in range (height)}

	def GetTile(self, x, y):
		return self.tiles[(x, y)]

	def SetTile(self, x, y, tile):
		self.tiles[(x, y)] = tile

	def Print(self):
		for x in range(0, self.width):
			for y in range(0, self.height):
				tile = self.GetTile(x, y)
				tileChar = tile.GetChar()
				sys.stdout.write(tileChar)
			sys.stdout.write('\n')



class Card:
	def __init__(self, cardType):
		self.type = cardType

map = Map(8, 8)
map.SetTile(0, 0, Tile(TileType.Town))
map.SetTile(0, 7, Tile(TileType.Town))
map.SetTile(7, 0, Tile(TileType.Town))
map.SetTile(7, 7, Tile(TileType.Town))
map.Print()