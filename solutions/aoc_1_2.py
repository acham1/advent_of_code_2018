#!/usr/local/bin/python3

import sys

lines = [line.strip() for line in sys.stdin]
nums = [int(line) for line in lines]

def first_repeated_total(nums):
	position, total, seen = 0, 0, {0}
	while (True):
		num = nums[position % len(nums)]
		position += 1
		total += num
		if (total in seen):
			return total
		seen.add(total)

print(first_repeated_total(nums))
