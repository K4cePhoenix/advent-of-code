
f = open('./input/aoc2015_01.txt', 'r')

data = f.readlines()

def part_1(dat):
    dat = dat[0]
    floor = 0
    for char in dat:
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
        else:
            print("WHAT")
    return floor


def part_2(dat):
    dat = dat[0]
    floor = 0
    for ind, char in enumerate(dat):
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
        else:
            print("WHAT")
        if floor == -1:
            return ind+1

print(part_1(data))
print(part_2(data))
