import re
import numpy as np

f = open('./2015/input/aoc2015_06.txt', 'r')

data = f.readlines()

def part_1(dat):
    grid = np.zeros((1000, 1000))
    for line in dat:
        pattern = re.compile("(\w+.\w+) (\d+),(\d+) (\w+) (\d+),(\d+)")
        m = pattern.search(line)
        coords = list(map(int, m.group(2, 3, 5, 6)))
        if m.group(1) == 'toggle':
            grid[coords[0]:coords[2]+1, coords[1]:coords[3]+1] = np.invert(grid[coords[0]:coords[2]+1, coords[1]:coords[3]+1].astype(bool))
        elif m.group(1) == 'turn on':
            grid[coords[0]:coords[2]+1, coords[1]:coords[3]+1] = np.ones((coords[2]+1-coords[0], coords[3]+1-coords[1]))
        elif m.group(1) == 'turn off':
            grid[coords[0]:coords[2]+1, coords[1]:coords[3]+1] = np.zeros((coords[2]+1-coords[0], coords[3]+1-coords[1]))
    return int(np.sum(grid))

def part_2(dat):
    grid = np.zeros((1000, 1000))
    for line in dat:
        pattern = re.compile("(\w+.\w+) (\d+),(\d+) (\w+) (\d+),(\d+)")
        m = pattern.search(line)
        coords = list(map(int, m.group(2, 3, 5, 6)))
        if m.group(1) == 'toggle':
            grid[coords[0]:coords[2]+1, coords[1]:coords[3]+1] += np.ones((coords[2]+1-coords[0], coords[3]+1-coords[1]))*2
        elif m.group(1) == 'turn on':
            grid[coords[0]:coords[2]+1, coords[1]:coords[3]+1] += np.ones((coords[2]+1-coords[0], coords[3]+1-coords[1]))
        elif m.group(1) == 'turn off':
            grid[coords[0]:coords[2]+1, coords[1]:coords[3]+1] -= np.ones((coords[2]+1-coords[0], coords[3]+1-coords[1]))
        grid[np.where(grid < 0)] = 0
    return int(np.sum(grid))

print(part_1(data))
print(part_2(data))
