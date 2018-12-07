
f = open('./input/aoc2017_02.txt', 'r')

data = f.readlines()

def bla(dat):
    for i, x in enumerate(dat):
        for y in dat[i+1:]:
            if x % y == 0 or y % x == 0:
                return max(x, y) / min(x, y)

def part_1(dat):
    checksum = 0
    for line in dat:
        tmp = list(map(int, line.split()))
        checksum += (max(tmp) - min(tmp))
    return checksum

def part_2(dat):
    _sum = 0
    for line in dat:
        tmp = list(map(int, line.split()))
        _sum += bla(tmp)
    return int(_sum)

print(part_1(data))
print(part_2(data))
