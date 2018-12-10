#!/usr/local/bin/python3

# The whole piece of fabric they're working on is a very large square - at least 1000 inches on each side.

# Each Elf has made a claim about which area of fabric would be ideal for Santa's suit. All claims have an ID and consist of a single rectangle with edges parallel to the edges of the fabric. Each claim's rectangle is defined as follows:

# The number of inches between the left edge of the fabric and the left edge of the rectangle.
# The number of inches between the top edge of the fabric and the top edge of the rectangle.
# The width of the rectangle in inches.
# The height of the rectangle in inches.
# A claim like #123 @ 3,2: 5x4 means that claim ID 123 specifies a rectangle 3 inches from the left edge, 2 inches from the top edge, 5 inches wide, and 4 inches tall. Visually, it claims the square inches of fabric represented by # (and ignores the square inches of fabric represented by .) in the diagram below:

# ...........
# ...........
# ...#####...
# ...#####...
# ...#####...
# ...#####...
# ...........
# ...........
# ...........
# The problem is that many of the claims overlap, causing two or more claims to cover part of the same areas. For example, consider the following claims:

# #1 @ 1,3: 4x4
# #2 @ 3,1: 4x4
# #3 @ 5,5: 2x2
# Visually, these claim the following areas:

# ........
# ...2222.
# ...2222.
# .11XX22.
# .11XX22.
# .111133.
# .111133.
# ........
# The four square inches marked with X are claimed by both 1 and 2. (Claim 3, while adjacent to the others, does not overlap either of them.)

# If the Elves all proceed with their own plans, none of them will have enough fabric. How many square inches of fabric are within two or more claims?

import re
import sys

class Claim:
	def __init__(self, claim_id, x, y, width, height):
		self.claim_id = claim_id
		self.x = x
		self.y = y
		self.width = width
		self.height = height

	def tiles(self):
		tile = lambda i: (
			self.x + i % self.width,
			self.y + i // self.width)
		num_tiles = self.width * self.height
		return [tile(i) for i in range(num_tiles)]

def parse(line):
	claim_id, x, y, width, height = map(int, filter(
		lambda x: x, re.split('[#@:x, ]', line)))
	return Claim(claim_id, x, y, width, height)

if __name__ == '__main__':
	claims = [parse(line.strip()) for line in sys.stdin]
	seen, reseen = set(), set()
	for claim in claims:
		for tile in claim.tiles():
			reseen.add(tile) if tile in seen else seen.add(tile)
	print(len(reseen))
