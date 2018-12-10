import numpy as np
import collections

with open('./2018/input/aoc2018_09.txt', 'r') as f:
    data = f.read().split('\n')

def parse_data(dat):
    l = dat[0].split()
    return list(map(int, (l[0], l[-2])))

def part_1(data):
    data = parse_data(data)
    scores = np.zeros(data[0])
    circle = np.array([0])
    pos = 0
    for m in range(1, data[1]+1):
        if m % 23:
            pos = (pos + 2) % (circle.shape[0]+1)
            if pos < 1:
                pos = 1
            circle = np.insert(circle, pos, m, axis=-1)
        else:
            scores[m % scores.shape[0]] += m
            pos -= 7
            scores[m % scores.shape[0]] += circle[pos]
            circle = np.delete(circle, pos)
    return int(max(scores))

def part_2(data):
    data = parse_data(data)
    scores = np.zeros(data[0])
    circle = collections.deque([0])
    for m in range(1, data[1]*100+1):
        if m % 23:
            circle.rotate(2)
            circle.append(m)
        else:
            circle.rotate(-7)
            tmp = circle.pop()
            player = m % scores.shape[0]
            scores[player] += m+tmp
    return int(max(scores))

print(part_1(data))
print(part_2(data))
