
f = open('./input/aoc2015_02.txt', 'r')

data = f.readlines()

def part_1(dat):
    paper = 0
    for line in dat:
        l, w, h = map(int, line.split('x'))
        paper += 2*l*w+2*l*h+2*w*h+min(l*w, l*h, w*h)
    return paper

def part_2(dat):
    ribbon = 0
    for line in dat:
        l, w, h = map(int, line.split('x'))
        ribbon += l*w*h+2*l+2*w+2*h
        ribbon -= max(l, w, h)*2
    return ribbon

print(part_1(data))
print(part_2(data))
