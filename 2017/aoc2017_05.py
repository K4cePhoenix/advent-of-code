import numpy as np
import collections

with open('./2017/input/aoc2017_05.txt', 'r') as f:
    data = f.read().split('\n')

def parse_data(dat):
    return list(map(int, dat))

def part_1(data):
    data = parse_data(data)
    pos = 0
    steps = 0
    while True:
        if 0 <= pos < len(data):
            tmp = pos
            pos += data[pos]
            data[tmp] += 1
            steps += 1
        else:
            break
    return steps

def part_2(data):
    data = parse_data(data)
    pos = 0
    steps = 0
    while True:
        if 0 <= pos < len(data):
            tmp = pos
            pos += data[pos]
            if data[tmp] < 3:
                data[tmp] += 1
            else:
                data[tmp] -= 1
            steps += 1
        else:
            break
    return steps

print(part_1(data))
print(part_2(data))
