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