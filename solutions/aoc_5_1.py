#!/usr/local/bin/python3

import sys

line = sys.stdin.readline().strip()

def reacts(a, b):
	return (a.lower() == b or b.lower() == a) and a != b

def react(line):
	last = ''
	for char in line:
		if last and reacts(char, last[-1]):
			last = last[:-1]
		else:
			last += char
	return last

print(len(react(line)))