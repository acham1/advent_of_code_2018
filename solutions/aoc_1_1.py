#!/usr/local/bin/python3

import sys

lines = [line.strip() for line in sys.stdin]
total = sum(int(n) for n in lines)
print(total)
