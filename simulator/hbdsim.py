#!/usr/bin/env python
print "Here be Dragons: The Card Game: The Simulator\n"

class Map:
	def __init__(self, width, height):
		self.width = width;
		self.height = height;

x = Map(8,8)
print x.width