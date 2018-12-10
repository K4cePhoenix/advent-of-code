import numpy as np
import cv2

with open('./2018/input/aoc2018_06.txt', 'r') as f:
    data = f.read().split('\n')

def parse_data(dat):
    cs = list()
    for line in dat:
        x, y = map(int, line.split(','))
        cs.append((x,y))
    sx = max([x[0] for x in cs])+1
    sy = max([y[1] for y in cs])+1
    return cs, (sx, sy)

def part_1(data):
    cs, s = parse_data(data)
    m = np.ones((s[0], s[1], len(cs)), np.uint8)
    dist_map = np.zeros_like(m, dtype=np.uint16)
    for i in range(len(cs)):
        x, y = cs[i]
        m[x, y, i] = 255
        dist_map[:,:,i] = cv2.distanceTransform(cv2.bitwise_not(m[:,:,i]), cv2.DIST_L1, 3)
    r = dist_map.argmin(axis=-1)
    t = dist_map[:,:,::-1].argmin(axis=-1)
    t = t.max() - t
    r[np.where(t != r)] = -1
    tl = [r[:, 0], r[0, :], r[s[0]-1, :], r[:, s[1]-1]]
    inv =set(i for l in tl for i in l)
    sz = set(len(np.where(r == i)[0]) for i in range(len(cs)) if i not in inv)
    return max(sz)

def part_2(data):
    cs, s = parse_data(data)
    sz = 0
    for i in range(max(s) + 1):
        for j in range(max(s) + 1):
            sz += sum(abs(x - i) + abs(y - j) for x, y in cs) < 10000
    return sz

print(part_1(data))
print(part_2(data))
