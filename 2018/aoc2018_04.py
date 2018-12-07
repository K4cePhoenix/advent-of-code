from collections import defaultdict
from datetime import datetime
import re

f = open('./input/aoc2018_04.txt', 'r')
data = f.readlines()

def parse_guards(data):
    guards = defaultdict(list)
    times = defaultdict(int)
    for line in sorted(data):
        t, action = line.split(']')
        t = datetime.strptime(t, '[%Y-%m-%d %H:%M')
        if 'Guard #' in action:
            g = int(re.search("\d+", action).group(0))
        if 'falls asleep' in action:
            t0 = t
        if 'wakes up' in action:
            guards[g].append((t0.minute, t.minute))
            times[g] += (t - t0).total_seconds()
    return guards, times

def part_1(data):
    guards, times = parse_guards(data)
    guard, time = max(times.items(), key=lambda i: i[1])
    minute, count = max([(minute, sum(1 for start, end in guards[guard] if start <= minute < end)) for minute in range(60)], key=lambda i: i[1])
    return guard * minute

def part_2(data):
    guards, times = parse_guards(data)
    guard, minute, count = max([(guard, minute, sum(1 for t0, t1 in guards[guard] if t0 <= minute < t1)) for minute in range(60) for guard in guards], key=lambda i: i[2])
    return guard * minute

print(part_1(data))
print(part_2(data))
