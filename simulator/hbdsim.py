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
		self.SetTile(0, 0, Tile(TileType.Town))
		self.SetTile(0, height - 1, Tile(TileType.Town))
		self.SetTile(width - 1, 0, Tile(TileType.Town))
		self.SetTile(width - 1, height - 1, Tile(TileType.Town))

	def GetTile(self, x, y):
		return self.tiles[(x, y)]

	def SetTile(self, x, y, tile):
		self.tiles[(x, y)] = tile

	def Print(self):
		for x in range(0, self.width):
			for y in range(0, self.height):
				sys.stdout.write(self.GetTile(x, y).GetChar())
			sys.stdout.write('\n')

class Card:
	def __init__(self, name, category):
		self.name = name
		self.category = category
		

width = height = 8;
map = Map(width, height)
map.Print()