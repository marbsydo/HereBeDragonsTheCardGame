# -*- coding: utf-8 -*-

import tiles

class GameMap:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.tiles = {(x,y):tiles.Unexplored for x in range(width) for y in range (height)}
		self.TileSet(0, 0, tiles.Town)
		self.TileSet(0, height - 1, tiles.Town)
		self.TileSet(width - 1, 0, tiles.Town)
		self.TileSet(width - 1, height - 1, tiles.Town)

	def TileGet(self, x, y):
		if x >= 0 and x < self.width and y >= 0 and y < self.height:
			return self.tiles[(x, y)]
		else:
			return tiles.Invalid

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

	def RenderMap(self, gameIO, pos = [-1, -1]):
		key = [
		gameIO.MakeString(tiles.TileToSymbol(tiles.Whirlpool), tiles.TileToColour(tiles.Whirlpool)) + ' = Whirlpool   ' + gameIO.MakeString(tiles.TileToSymbol(tiles.TreasureIsland), tiles.TileToColour(tiles.TreasureIsland)) + ' = Treasure Island',
		gameIO.MakeString(tiles.TileToSymbol(tiles.Whirlwind), tiles.TileToColour(tiles.Whirlwind)) + ' = Whirlwind   ' + gameIO.MakeString(tiles.TileToSymbol(tiles.Town), tiles.TileToColour(tiles.Town)) + ' = Town',
		gameIO.MakeString(tiles.TileToSymbol(tiles.Tempest), tiles.TileToColour(tiles.Tempest)) + ' = Tempest     ' + gameIO.MakeString(tiles.TileToSymbol(tiles.MerchantShip), tiles.TileToColour(tiles.MerchantShip)) + ' = Merchant Ship',
		gameIO.MakeString(tiles.TileToSymbol(tiles.Shipwreck), tiles.TileToColour(tiles.Shipwreck)) + ' = Shipwreck   ' + gameIO.MakeString(tiles.TileToSymbol(tiles.OpenOcean), tiles.TileToColour(tiles.OpenOcean)) + ' = Open ocean',
		]
		gameIO.PrintLine('╔' + '═' * (self.width * 2 + 1) + '╗')
		for y in range(0, self.width):
			gameIO.Print('║ ')
			for x in range(0, self.height):
				tile = self.TileGet(x, y)

				if x == pos[0] and y == pos[1]:
					tileString = gameIO.MakeString(tiles.TileToSymbol(tile), 'red', 'background')
				else:
					tileString = gameIO.MakeString(tiles.TileToSymbol(tile), tiles.TileToColour(tile))
				gameIO.Print(tileString + ' ')
			gameIO.Print('║')
			if y < len(key):
				gameIO.PrintLine(' ' + key[y])
			else:
				gameIO.PrintLine()
		gameIO.PrintLine('╚' + '═' * (self.width * 2 + 1) + '╝')