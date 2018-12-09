#!/usr/local/bin/python3

# To make sure you didn't miss any, you scan the likely candidate boxes again, counting the number that have an ID containing exactly two of any letter and then separately counting those with exactly three of any letter. You can multiply those two counts together to get a rudimentary checksum and compare it to what your device predicts.

# For example, if you see the following box IDs:

# abcdef contains no letters that appear exactly two or three times.
# bababc contains two a and three b, so it counts for both.
# abbcde contains two b, but no letter appears exactly three times.
# abcccd contains three c, but no letter appears exactly two times.
# aabcdd contains two a and two d, but it only counts once.
# abcdee contains two e.
# ababab contains three a and three b, but it only counts once.
# Of these box IDs, four of them contain a letter which appears exactly twice, and three of them contain a letter which appears exactly three times. Multiplying these together produces a checksum of 4 * 3 = 12.

# What is the checksum for your list of box IDs?

import collections
import sys

def occurrences(line):
	result = collections.defaultdict(int)
	for char in line:
		result[char] += 1
	return result

def checksum(lines):
	results = [occurrences(line) for line in lines]
	twos, threes = 0, 0
	for result in results:
		has_two, has_three = False, False
		for char in result:
			has_two |= result[char] == 2
			has_three |= result[char] == 3
			if has_two and has_three: 
				break
		twos += 1 if has_two else 0
		threes += 1 if has_three else 0
	return twos * threes

if __name__ == '__main__':
	lines = [line.strip() for line in sys.stdin]
	print(checksum(lines))
