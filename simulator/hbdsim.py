#!/usr/bin/env python
print "Here be Dragons: The Card Game: The Simulator\n"

def enum(*sequential, **named):
	enums = dict(zip(sequential, range(len(sequential))), **named)
	return type('Enum', (), enums)

CardType = enum('OpenOcean', 'TreasureIsland', 'Town', 'Unexplored', 'Whirlpool', 'Whirlwind', 'Storm', 'Shipwreck')

class Map:
	def __init__(self, width, height):
		self.width = width;
		self.height = height;

class Card:
	def __init__(self, cardType):
		self.type = cardType;

map = Map(8,8)