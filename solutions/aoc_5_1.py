#!/usr/local/bin/python3

# The polymer is formed by smaller units which, when triggered, react with each other such that two adjacent units of the same type and opposite polarity are destroyed. Units' types are represented by letters; units' polarity is represented by capitalization. For instance, r and R are units with the same type but opposite polarity, whereas r and s are entirely different types and do not react.

# For example:

# In aA, a and A react, leaving nothing behind.
# In abBA, bB destroys itself, leaving aA. As above, this then destroys itself, leaving nothing.
# In abAB, no two adjacent units are of the same type, and so nothing happens.
# In aabAAB, even though aa and AA are of the same type, their polarities match, and so nothing happens.
# Now, consider a larger example, dabAcCaCBAcCcaDA:

# dabAcCaCBAcCcaDA  The first 'cC' is removed.
# dabAaCBAcCcaDA    This creates 'Aa', which is removed.
# dabCBAcCcaDA      Either 'cC' or 'Cc' are removed (the result is the same).
# dabCBAcaDA        No further actions can be taken.
# After all possible reactions, the resulting polymer contains 10 units.

# How many units remain after fully reacting the polymer you scanned?

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
