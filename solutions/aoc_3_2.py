#!/usr/local/bin/python3

import re
import sys
from aoc_3_1 import parse, Claim

# Amidst the chaos, you notice that exactly one claim doesn't overlap by even a single square inch of fabric with any other claim. If you can somehow draw attention to it, maybe the Elves will be able to make Santa's suit after all!

# For example, in the claims above, only claim 3 is intact after all claims are made.

# What is the ID of the only claim that doesn't overlap?

if __name__ == '__main__':
	claims = map(lambda x: parse(x.strip()), sys.stdin)
	seen, free = dict(), set()
	for claim in claims:
		free.add(claim.claim_id)
		for tile in claim.tiles():
			if tile in seen:
				free.discard(seen[tile])
				free.discard(claim.claim_id)
			seen[tile] = claim.claim_id
	print(free.pop())
