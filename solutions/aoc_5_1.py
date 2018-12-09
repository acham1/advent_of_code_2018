#!/usr/local/bin/python3

import sys

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

if __name__ == "__main__":	
	line = sys.stdin.readline().strip()
	print(len(react(line)))
