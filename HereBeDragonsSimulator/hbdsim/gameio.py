import os
import sys

class GameIO:
	def Clear(self):
		os.system(['clear', 'cls'][os.name == 'nt'])

	def PrintBasic(self, text):
		sys.stdout.write(text)

	def MakeString(self, text, colour = -1, textOrBackground = 'text'):
		if colour < 0:
			return text
		else:
			if textOrBackground == 'background':
				pre = self.ColourBackground(colour)
			elif textOrBackground == 'text':
				pre = self.ColourText(colour)
			else:
				pre = self.ColourReset()
			return pre + text + self.ColourReset()

	def Print(self, text, colour = -1, textOrBackground = 'text'):
		self.PrintBasic(self.MakeString(text, colour, textOrBackground))

	def PrintLine(self, text = '', colour = -1, textOrBackground = 'text'):
		self.PrintBasic(self.MakeString(text + '\n', colour, textOrBackground))

	def ColourText(self, colour):
		return '\033[1;3' + str(self.ColourToNumber(colour)) + 'm'

	def ColourBackground(self, colour):
		return '\033[1;4' + str(self.ColourToNumber(colour)) + 'm'

	def ColourReset(self):
		return '\033[1;m'

	def ColourToNumber(self, colour):
		return {
		'default': -1,
		'grey': 0,
		'red': 1,
		'green': 2,
		'yellow': 3,
		'blue': 4,
		'magenta': 5,
		'cyan': 6,
		'white': 7,
		'crimson': 8,
		'bold': 9
		}.get(colour, 9)

	def NumberToTally(self, number):
		fives = int(number) / 5
		remainder = number - fives * 5
		return '||||/ ' * fives + '|' * remainder

	def Input(self, text):
		return raw_input(text)

	def Wait(self):
		return self.Input('Press <enter> to continue\n')