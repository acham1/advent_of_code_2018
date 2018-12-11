#!/usr/local/bin/python3

# Strategy 2: Of all guards, which guard is most frequently asleep on the same minute?

# In the example above, Guard #99 spent minute 45 asleep more than any other guard or minute - three times in total. (In all other cases, any guard spent any minute asleep at most twice.)

# What is the ID of the guard you chose multiplied by the minute you chose? (In the above example, the answer would be 99 * 45 = 4455.)

from collections import defaultdict
import sys
from aoc_4_1 import build_stats

if __name__ == '__main__':
	entries = sorted(line.strip() for line in sys.stdin)
	stats = build_stats(entries)
	for guard in stats:
		max_minute = max(
			stats[guard]['tally'], 
			key=lambda x: stats[guard]['tally'][x])
		max_tally = stats[guard]['tally'][max_minute]
		stats[guard]['max_minute'] = max_minute
		stats[guard]['max_tally'] = max_tally
	sleepy_guard = max(stats, key=lambda x: stats[x]['max_tally'])
	sleepy_minute = stats[sleepy_guard]['max_minute']
	print(sleepy_guard * sleepy_minute)
