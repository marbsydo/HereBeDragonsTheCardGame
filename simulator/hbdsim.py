#!/usr/bin/env python

import sys
import random

print "Here be Dragons: The Card Game: The Simulator\n"

def enum(*sequential, **named):
	enums = dict(zip(sequential, range(len(sequential))), **named)
	return type('Enum', (), enums)

TileType = enum('None', 'Any', 'Unexplored', 'Town' ,'OpenOcean', 'TreasureIsland', 'Whirlpool', 'Whirlwind', 'Storm', 'Shipwreck')

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

class GameMap:
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

# Base card
class Card:
	def __init__(self):
		self.name = 'Undefined Card'
		self.tile = TileType.None

# Base card types
class LocationCard(Card):
	def __init__(self):
		self.category = 'Location'

class DragonCard(Card):
	def __init__(self):
		self.category = 'Dragon'

class TreasureCard(Card):
	def __init__(self):
		self.category = 'Treasure'

class AmuletCard(Card):
	def __init__(self):
		self.category = 'Amulet'

# Individual cards - locations
class OpenOcean(LocationCard):
	def __init__(self):
		self.name = 'Open Ocean'
		self.tile = TileType.OpenOcean

class TreasureIsland(LocationCard):
	def __init__(self):
		self.name = 'Treasure Island'
		self.tile = TileType.TreasureIsland

class Whirlwind(LocationCard):
	def __init__(self):
		self.name = 'Whirlwind'
		self.tile = TileType.Whirlwind

class Whirlpool(LocationCard):
	def __init__(self):
		self.name = 'Whirlpool'
		self.tile = TileType.Whirlpool

class Storm(LocationCard):
	def __init__(self):
		self.name = 'Storm'
		self.tile = TileType.Storm

class Shipwreck(LocationCard):
	def __init__(self):
		self.name = 'Shipwreck'
		self.tile = TileType.Shipwreck

# Individual cards - dragons
class WindLeviathan(DragonCard):
	def __init__(self):
		self.name = 'Wind Leviathan'
		self.tile = TileType.Whirlwind

class WindWyrm(DragonCard):
	def __init__(self):
		self.name = 'Wind Wyrm'
		self.tile = TileType.Whirlwind

class OceanLeviathan(DragonCard):
	def __init__(self):
		self.name = 'Ocean Leviathan'
		self.tile = TileType.Whirlpool

class OceanWyrm(DragonCard):
	def __init__(self):
		self.name = 'Ocean Wyrm'
		self.tile = TileType.Whirlpool

class StormLeviathan(DragonCard):
	def __init__(self):
		self.name = 'Storm Leviathan'
		self.tile = TileType.Storm

class StormWyrm(DragonCard):
	def __init__(self):
		self.name = 'Storm Wyrm'
		self.tile = TileType.Storm

class GhostLeviathan(DragonCard):
	def __init__(self):
		self.name = 'Ghost Leviathan'
		self.tile = TileType.Shipwreck

class GhostWyrm(DragonCard):
	def __init__(self):
		self.name = 'Ghost Wyrm'
		self.tile = TileType.Shipwreck

# Individual cards - treasures
class Gold(TreasureCard):
	def __init__(self):
		self.name = 'Gold'
		self.victoryPoints = 2;

class Jewels(TreasureCard):
	def __init__(self):
		self.name = 'Jewels'
		self.victoryPoints = 2;

class Map(TreasureCard):
	def __init__(self):
		self.name = 'Map'
		self.victoryPoints = 1;

class Rum(TreasureCard):
	def __init__(self):
		self.name = 'Rum'
		self.victoryPoints = 1;

# Individual cards - amulets
class WindAmulet(AmuletCard):
	def __init__(self):
		self.name = 'Wind Amulet'
		self.victoryPoints = 1;
		self.tile = TileType.Whirlwind

class OceanAmulet(AmuletCard):
	def __init__(self):
		self.name = 'Ocean Amulet'
		self.victoryPoints = 1;
		self.tile = TileType.Whirlpool

class StormAmulet(AmuletCard):
	def __init__(self):
		self.name = 'Storm Amulet'
		self.victoryPoints = 1;
		self.tile = TileType.Storm

class GhostAmulet(AmuletCard):
	def __init__(self):
		self.name = 'Ghost Amulet'
		self.victoryPoints = 1;
		self.tile = TileType.Shipwreck

class DragonAmulet(AmuletCard):
	def __init__(self):
		self.name = 'Dragon Amulet'
		self.victoryPoints = 2;
		self.tile = TileType.Any

discoveryPile = [
OpenOcean(), OpenOcean(), OpenOcean(), OpenOcean(),
TreasureIsland(), TreasureIsland(), TreasureIsland(), TreasureIsland(),
TreasureIsland(), TreasureIsland(), TreasureIsland(), TreasureIsland(),
Whirlwind(), Whirlwind(),
Whirlpool(), Whirlpool(),
Storm(), Storm(),
Shipwreck(), Shipwreck(),
WindLeviathan(), WindWyrm(),
OceanLeviathan(), OceanWyrm(),
StormLeviathan(), StormWyrm(),
GhostLeviathan(), GhostWyrm()
]

treasurePile = [
Gold(), Gold(), Gold(),
Jewels(), Jewels(), Jewels(),
Map(), Map(), Map(),
Rum(), Rum(), Rum(),
WindAmulet(), WindAmulet(),
OceanAmulet(), OceanAmulet(),
StormAmulet(), StormAmulet(),
GhostAmulet(), GhostAmulet(),
DragonAmulet(), DragonAmulet()
]

random.seed(23)
random.shuffle(discoveryPile)
random.shuffle(treasurePile)

def printTitle(s):
	sys.stdout.write('  ' + s + '  \n' + '=' * (len(s) + 4) + '\n')

printTitle('Discovery pile')
for x in discoveryPile:
	print x.name

printTitle('Treasure pile')
for x in treasurePile:
	print x.name

width = height = 8;
map = GameMap(width, height)
map.Print()