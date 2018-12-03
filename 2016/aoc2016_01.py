
f = open('./input/aoc2016_01.txt', 'r')

data = f.readlines()

def move(start, direction, distance):
    if direction % 4 == 0:
        destination = (start[0]+distance, start[1])
    elif direction % 4 == 1:
        destination = (start[0], start[1]+distance)
    elif direction % 4 == 2:
        destination = (start[0]-distance, start[1])
    elif direction % 4 == 3:
        destination = (start[0], start[1]-distance)
    return destination

def step(start, direction):
    if direction % 4 == 0:
        destination = (start[0]+1, start[1])
    elif direction % 4 == 1:
        destination = (start[0], start[1]+1)
    elif direction % 4 == 2:
        destination = (start[0]-1, start[1])
    elif direction % 4 == 3:
        destination = (start[0], start[1]-1)
    return destination

def part_1(dat):
    dat = dat[0]
    START_POS = (0, 0)
    _pos = START_POS
    _dir = 0 # x%4==0:N x%4==1:E x%4==2:S x%4==3:W
    for dn in dat.split(','):
        dn = dn.strip()
        if dn[0] == 'R':
            _dir += 1
        elif dn[0] == 'L':
            _dir -= 1
        _pos = move(_pos, _dir, int(dn[1:]))
    return abs(_pos[0])+abs(_pos[1])

def part_2(dat):
    dat = dat[0]
    START_POS = (0, 0)
    _pos = START_POS
    last_pos = [_pos]
    _dir = 0 # x%4==0:N x%4==1:E x%4==2:S x%4==3:W
    for dn in dat.split(','):
        dn = dn.strip()
        if dn[0] == 'R':
            _dir += 1
        elif dn[0] == 'L':
            _dir -= 1
        for i in range(0, int(dn[1:])):
            _pos = step(_pos, _dir)
            if _pos in last_pos:
                return abs(_pos[0])+abs(_pos[1])
            last_pos.append(_pos)

print(part_1(data))
print(part_2(data))
