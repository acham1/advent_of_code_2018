#!/usr/local/bin/python3

# Using only the Manhattan distance, determine the area around each coordinate by counting the number of integer X,Y locations that are closest to that coordinate (and aren't tied in distance to any other coordinate).

# Your goal is to find the size of the largest area that isn't infinite. For example, consider the following list of coordinates:

# 1, 1
# 1, 6
# 8, 3
# 3, 4
# 5, 5
# 8, 9
# If we name these coordinates A through F, we can draw them on a grid, putting 0,0 at the top left:

# ..........
# .A........
# ..........
# ........C.
# ...D......
# .....E....
# .B........
# ..........
# ..........
# ........F.
# This view is partial - the actual grid extends infinitely in all directions. Using the Manhattan distance, each location's closest coordinate can be determined, shown here in lowercase:

# aaaaa.cccc
# aAaaa.cccc
# aaaddecccc
# aadddeccCc
# ..dDdeeccc
# bb.deEeecc
# bBb.eeee..
# bbb.eeefff
# bbb.eeffff
# bbb.ffffFf
# Locations shown as . are equally far from two or more coordinates, and so they don't count as being closest to any.

# In this example, the areas of coordinates A, B, C, and F are infinite - while not shown here, their areas extend forever outside the visible grid. However, the areas of coordinates D and E are finite: D is closest to 9 locations, and E is closest to 17 (both including the coordinate's location itself). Therefore, in this example, the size of the largest area is 17.

# What is the size of the largest area that isn't infinite?

import queue
import sys

class _Pair:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def dist(self, pair):
		return abs(self.x - pair.x) + abs(self.y - pair.y)

	@staticmethod
	def parsepair(line):
		xstr, ystr = line.strip().split(',')
		return _Pair(int(xstr), int(ystr))

class _IterBoard:
	def __init__(self, pairs):
		self.pairs = pairs
		self.minx = min(pairs, key=_access('x')).x
		self.maxx = max(pairs, key=_access('x')).x
		self.miny = min(pairs, key=_access('y')).y
		self.maxy = max(pairs, key=_access('y')).y

		self.candidates = set(pairs)
		self.ownership = dict() # pair => rootpair
		self.queue = {pair: [pair] for pair in pairs}
		self.range = -1
		self.regions = dict() # rootpair => set<Pair>

	def max(self):
		maxregion = max(
			self.regions,
			key=lambda x: len(self.regions[x]))
		return (maxregion, len(self.regions[x]))

	def step(self):
		self.range += 1
		for pair in self.pairs:
			# TODO
			return

	def completed(self):
		# TODO
		return True

def _access(name):
	return lambda x: getattr(x, name)

if __name__ == '__main__':
	pairs = [_Pair.parsepair(line) for line in sys.stdin]
	board = _IterBoard(pairs)
	while not board.completed():
		board.step()
	_, maxsize = board.max()
	print(maxregion)
