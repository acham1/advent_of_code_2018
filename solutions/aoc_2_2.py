#!/usr/local/bin/python3

# Confident that your list of box IDs is complete, you're ready to find the boxes full of prototype fabric.

# The boxes will have IDs which differ by exactly one character at the same position in both strings. For example, given the following box IDs:

# abcde
# fghij
# klmno
# pqrst
# fguij
# axcye
# wvxyz
# The IDs abcde and axcye are close, but they differ by two characters (the second and fourth). However, the IDs fghij and fguij differ by exactly one character, the third (h and u). Those must be the correct boxes.

# What letters are common between the two correct box IDs? (In the example above, this is found by removing the differing character from either ID, producing fgij.)

import sys

def find_match(lines, width):
	for i in range(width):
		seen = set()
		for line in lines:
			candidate = line[:i] + line[i+1:]
			if candidate in seen:
				return candidate
			seen.add(candidate)
	return None

if __name__ == '__main__':
	lines = [line.strip() for line in sys.stdin]
	print(find_match(lines, len(lines[0])))
