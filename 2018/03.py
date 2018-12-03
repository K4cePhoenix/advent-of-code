import numpy as np

f = open('data.txt', 'r')
data = f.readlines()

SIZE = 1000

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
    return _id, int(px), int(px), int(px), int(px)

fab = np.zeros((SIZE, SIZE))
l = list()

def part_1(dat):
    for line in dat:
        t, e, m, p, o = parse_data(line)
        c = Claim(t, e, m, p, o)
        l.append(c)
        fab[c.x:c.x+c.w, c.y:c.y+c.h] += 1
    return np.size(np.where(fab > 1)[0])

def part_2(dat):
    for c in l:
        if np.all(fab[c.x:c.x+c.w, c.y:c.y+c.h] == 1):
            return c.id


print(part_1(data))
print(part_2(data))
