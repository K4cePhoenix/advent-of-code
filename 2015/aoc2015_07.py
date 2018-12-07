from collections import defaultdict

f = open('./input/aoc2015_07.txt', 'r')

data = f.readlines()

def part_1(dat):
    # needs more work
    storage = defaultdict()
    for line in dat:
        op, dest = line.split('->')
        if 'AND' in op:
            tmp = op.split('AND')
            tmp0, tmp1 = tmp[0].strip(), tmp[1].strip()
            tmp = int(storage[tmp0]) & int(storage[tmp1])
        elif 'OR' in op:
            tmp = op.split('OR')
            tmp = int(storage[tmp0]) | int(storage[tmp1])
        elif 'RSHIFT' in op:
            tmp = op.split('RSHIFT')
            tmp = int(storage[tmp0]) >> int(tmp1)
        elif 'LSHIFT' in op:
            tmp = op.split('LSHIFT')
            tmp = int(storage[tmp0]) << int(tmp1)
        elif 'NOT' in op:
            tmp = op.split('NOT')
            tmp = ~ int(storage[tmp1])
        else:
            print(op)
            tmp = int(op)
        storage[dest] = tmp
    return storage['a']

def part_2(dat):
    pass

print(part_1(data))
print(part_2(data))
