#!/usr/local/bin/python3

# For example, consider the following records, which have already been organized into chronological order:

# [1518-11-01 00:00] Guard #10 begins shift
# [1518-11-01 00:05] falls asleep
# [1518-11-01 00:25] wakes up
# [1518-11-01 00:30] falls asleep
# [1518-11-01 00:55] wakes up
# [1518-11-01 23:58] Guard #99 begins shift
# [1518-11-02 00:40] falls asleep
# [1518-11-02 00:50] wakes up
# [1518-11-03 00:05] Guard #10 begins shift
# [1518-11-03 00:24] falls asleep
# [1518-11-03 00:29] wakes up
# [1518-11-04 00:02] Guard #99 begins shift
# [1518-11-04 00:36] falls asleep
# [1518-11-04 00:46] wakes up
# [1518-11-05 00:03] Guard #99 begins shift
# [1518-11-05 00:45] falls asleep
# [1518-11-05 00:55] wakes up
# Timestamps are written using year-month-day hour:minute format. The guard falling asleep or waking up is always the one whose shift most recently started. Because all asleep/awake times are during the midnight hour (00:00 - 00:59), only the minute portion (00 - 59) is relevant for those events.

# Visually, these records show that the guards are asleep at these times:

# Date   ID   Minute
#             000000000011111111112222222222333333333344444444445555555555
#             012345678901234567890123456789012345678901234567890123456789
# 11-01  #10  .....####################.....#########################.....
# 11-02  #99  ........................................##########..........
# 11-03  #10  ........................#####...............................
# 11-04  #99  ....................................##########..............
# 11-05  #99  .............................................##########.....
# The columns are Date, which shows the month-day portion of the relevant day; ID, which shows the guard on duty that day; and Minute, which shows the minutes during which the guard was asleep within the midnight hour. (The Minute column's header shows the minute's ten's digit in the first row and the one's digit in the second row.) Awake is shown as ., and asleep is shown as #.

# Note that guards count as asleep on the minute they fall asleep, and they count as awake on the minute they wake up. For example, because Guard #10 wakes up at 00:25 on 1518-11-01, minute 25 is marked as awake.

# If you can figure out the guard most likely to be asleep at a specific time, you might be able to trick that guard into working tonight so you can have the best chance of sneaking in. You have two strategies for choosing the best guard/minute combination.

# Strategy 1: Find the guard that has the most minutes asleep. What minute does that guard spend asleep the most?

# In the example above, Guard #10 spent the most minutes asleep, a total of 50 minutes (20+25+5), while Guard #99 only slept for a total of 30 minutes (10+10+10). Guard #10 was asleep most during minute 24 (on two days, whereas any other minute the guard was asleep was only seen on one day).

# While this example listed the entries in chronological order, your entries are in the order you found them. You'll need to organize them before they can be analyzed.

# What is the ID of the guard you chose multiplied by the minute you chose? (In the above example, the answer would be 10 * 24 = 240.)

from collections import defaultdict
import re
import sys

sanitize = lambda groups: (
	int(groups[0]), 
	groups[1], 
	int(groups[2]) if groups[2] else None)

default_stat = lambda: {'total': 0, 'tally': defaultdict(int)}

pattern = re.compile('\A\[\S+ \d+:(\d+)\] (\D+(\d+)?\D+)\Z')

if __name__ == '__main__':
	entries = sorted(line.strip() for line in sys.stdin)
	stats = defaultdict(default_stat)
	current_guard, start_time = 0, 0
	for entry in entries:
		minute, event, guard_id = sanitize(
			pattern.match(entry).groups())
		if guard_id:
			current_guard = guard_id
		elif event == 'falls asleep':
			start_time = minute
		else:
			stats[current_guard]['total'] += minute - start_time
			for time in range(start_time, minute):
				stats[current_guard]['tally'][time] += 1
	sleepy_guard = max(
		stats, 
		key=lambda x: stats[x]['total'])
	sleepy_minute = max(
		stats[sleepy_guard]['tally'], 
		key=lambda x: stats[sleepy_guard]['tally'][x])
	print(sleepy_guard * sleepy_minute)
