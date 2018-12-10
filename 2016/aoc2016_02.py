import numpy as np

f = open('./2016/input/aoc2016_02.txt', 'r')

data = f.readlines()

def step(dn, pos, lim):
    if dn == 'L' and pos[0] > 0:
        pos = (pos[0]-1, pos[1])
    elif dn == 'U' and pos[1] > 0:
        pos = (pos[0], pos[1]-1)
    elif dn == 'R' and pos[0] < lim:
        pos = (pos[0]+1, pos[1])
    elif dn == 'D' and pos[1] < lim:
        pos = (pos[0], pos[1]+1)
    return pos

def step2(dn, pos, lim, rad):
    old_pos = pos
    if dn == 'L' and pos[0] > 0:
        pos = (pos[0]-1, pos[1])
    elif dn == 'U' and pos[1] > 0:
        pos = (pos[0], pos[1]-1)
    elif dn == 'R' and pos[0] < lim:
        pos = (pos[0]+1, pos[1])
    elif dn == 'D' and pos[1] < lim:
        pos = (pos[0], pos[1]+1)
    rad_dist = (abs(pos[0]-2)**2+abs(pos[1]-2)**2)**0.5
    if rad_dist > rad:
        return old_pos
    return pos

def part_1(dat):
    START_POS = np.array((1, 1))
    KEYPAD = np.arange(1, 10).reshape((3, 3))
    pos = START_POS
    code = ''
    for line in dat:
        for dn in line:
            pos = step(dn, pos, len(KEYPAD[0])-1)
        code += str(KEYPAD[pos[1], pos[0]])
    return code


def part_2(dat):
    START_POS = np.array((2, 0))
    KEYPAD = [ [0, 0, 1, 0, 0],
               [0, 2, 3, 4, 0],
               [5, 6, 7, 8, 9],
               [0, 'A', 'B', 'C', 0],
               [0, 0, 'D', 0, 0],
             ]
    KEYPAD = np.asarray(KEYPAD)
    pos = START_POS
    code = ''
    for line in dat:
        for dn in line:
            pos = step2(dn, pos, len(KEYPAD[0])-1, len(KEYPAD[0])//2)
            if (abs(pos[0]-2)**2+abs(pos[1]-2)**2)**0.5 > 2:
                print(pos)
        code += str(KEYPAD[pos[1], pos[0]])
    return code

print(part_1(data))
print(part_2(data))
