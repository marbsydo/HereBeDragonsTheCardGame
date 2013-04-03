def TileToSymbol(tile):
	return {
		Unexplored: ' ',
		Town: 'T',
		OpenOcean: '~',
		TreasureIsland: 'X',
		MerchantShip: '$',
		Whirlpool: 'o',
		Whirlwind: '*',
		Tempest: '^',
		Shipwreck: '&',
	}.get(tile, '?')

def TileToColour(tile):
	return {
		Unexplored: 'default',
		Town: 'default',
		OpenOcean: 'blue',
		TreasureIsland: 'yellow',
		MerchantShip: 'green',
		Whirlpool: 'magenta',
		Whirlwind: 'cyan',
		Tempest: 'red',
		Shipwreck: 'crimson'
	}.get(tile, 'grey')

class Invalid:
	pass

class Any:
	pass

class Unexplored:
	pass

class Town:
	pass

class OpenOcean:
	pass

class TreasureIsland:
	pass

class MerchantShip:
	pass

class Whirlpool:
	pass

class Whirlwind:
	pass

class Tempest:
	pass

class Shipwreck:
	pass