from time import time

with open('./2015/input/aoc2015_10.txt', 'r') as f:
    data = f.read().split('\n')

# data=["11"]

def parse_data(dat):
    return dat[0]

def lns(dat, times=40):
    t0 = time()
    for _ in range(times):
        r = ''
        a = 0
        t = dat[0]
        for i, c in enumerate(dat):
            if t == c:
                a += 1
                if i == len(dat)-1:
                    r = f"{r}{a}{t}"
                elif t != dat[i+1]:
                    r = f"{r}{a}{t}"
                    t = dat[i+1]
                    a = 0
            else:
                r = f"{r}{a}{t}"
        dat = r
        print(_, time()-t0)
        t0 = time()
    return r

def part_1(dat):
    dat = parse_data(dat)
    dat = lns(dat)
    return len(dat)

def part_2(dat):
    dat = parse_data(dat)
    dat = lns(dat, 50)
    return len(dat)
print(part_1(data))
print(part_2(data))
