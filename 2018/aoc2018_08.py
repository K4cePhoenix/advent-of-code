import sys

with open('./2018/input/aoc2018_08.txt', 'r') as f:
    data = f.read().split('\n')

sys.setrecursionlimit(5000)

def parse_data(dat):
    return list(map(int, dat[0].split(' ')))

def get_meta(dat):
    tmp = 0
    for i in dat:
        tmp += i
    return tmp

def break_children(meta, dat):
    n = dat[0]
    e = dat[1]
    dat = dat[2:]
    for i in range(n):
        meta, dat = break_children(meta, dat)
    tmp = get_meta(dat[:e])
    meta += tmp
    dat = dat[e:]
    return meta, dat

def break_children2(root, dat):
    n = dat[0]
    e = dat[1]
    dat = dat[2:]
    if n == 0:
        tmp = get_meta(dat[:e])
        root += tmp
        dat = dat[e:]
        return root, dat
    else:
        childs = list()
        for j in range(n):
            tmp, dat = break_children2(0, dat)
            childs.append(tmp)
        for i in dat[:e]:
            if i <= len(childs):
                root += childs[i-1]
        dat = dat[e:]
        return root, dat

def part_1(data):
    data = parse_data(data)
    meta, _ = break_children(0, data)
    return meta

def part_2(data):
    data = parse_data(data)
    root, _ = break_children2(0, data)
    return root

print(part_1(data))
print(part_2(data))
