#!/usr/bin/env python
print "Here be Dragons: The Card Game: The Simulator\n"

def enum(*sequential, **named):
	enums = dict(zip(sequential, range(len(sequential))), **named)
	return type('Enum', (), enums)

SquareType = enum('OpenOcean', 'TreasureIsland', 'Town', 'Unexplored', 'Whirlpool', 'Whirlwind', 'Storm', 'Shipwreck')
'''
discoveryPile = List();
discoveryDiscardPile = List();
treasuresPile = List();
treasuresDiscardPile = List();
'''
class Map:
	def __init__(self, width, height):
		self.width = width;
		self.height = height;

class Card:
	def __init__(self, cardType):
		self.type = cardType;

#map = Map(8,8)

map = {(x,y):0 for x in range(8) for y in range (8)}
point1 = (1, 2)
map[point1] = 2
print(map[(3, 2)])