import numpy as np

f = open('./input/aoc2017_03.txt', 'r')

data = f.readlines()

def step(start, direction):
    if direction % 4 == 0:
        destination = (start[0]+1, start[1])
    elif direction % 4 == 1:
        destination = (start[0], start[1]+1)
    elif direction % 4 == 2:
        destination = (start[0]-1, start[1])
    elif direction % 4 == 3:
        destination = (start[0], start[1]-1)
    return destination

def part_1(dat):
    pos = np.zeros(2)
    dn = 0
    dist = 1
    steps = 0
    dnc = 0
    while True:
        for i in range(0, dist):
            pos = step(pos, dn)
            steps += 1
            if steps >= int(dat[0])-1:
                return abs(pos[0]) + abs(pos[1])
        dnc += 1
        if dnc % 2 == 0:
            dist += 1
            dnc = 0
        dn += 1

def part_2(dat):
    pass

print(part_1(data))
print(part_2(data))
