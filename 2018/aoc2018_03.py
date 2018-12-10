import numpy as np

f = open('./2018/input/aoc2018_03.txt', 'r')
data = f.readlines()

SIZE = 1000
fab = np.zeros((SIZE, SIZE))
cs = list()

class Claim():
    def __init__(self, _id: int, x: int, y: int, w: int, h: int):
        self.id = _id
        self.x = x
        self.y = y
        self.w = w
        self.h = h

def parse_data(data):
    _id, _, pos, size = data.split()
    px, py = pos[:-1].split(',')
    sx, sy = size.split('x')
    return _id, int(px), int(py), int(sx), int(sy)

def part_1(dat):
    for line in dat:
        t, e, m, p, o = parse_data(line)
        c = Claim(t, e, m, p, o)
        cs.append(c)
    for c in cs:
        tmp = np.ones(fab[c.x:c.x+c.w, c.y:c.y+c.h].shape)
        fab[c.x:c.x+c.w, c.y:c.y+c.h] += tmp
    return np.size(np.where(fab > 1)[0])

def part_2(dat):
    for c in cs:
        if np.all(fab[c.x:c.x+c.w, c.y:c.y+c.h] == 1):
            return c.id


print(part_1(data))
print(part_2(data))
