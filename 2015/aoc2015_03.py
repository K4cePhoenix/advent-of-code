
f = open('./input/aoc2015_03.txt', 'r')

data = f.readlines()

def check_direction(dn, pos):
    if dn == '<':
        pos = (pos[0]-1, pos[1])
    elif dn == '^':
        pos = (pos[0], pos[1]-1)
    elif dn == '>':
        pos = (pos[0]+1, pos[1])
    elif dn == 'v':
        pos = (pos[0], pos[1]+1)
    return pos


def check_position(current_pos, list_of_last_pos):
    if current_pos not in list_of_last_pos:
        return True
    return False

def part_1(dat):
    dat = dat[0]
    houses = 1
    pos = (0, 0)
    last_pos = [pos]
    for dn in dat:
        pos = check_direction(dn, pos)
        if check_position(pos, last_pos):
            last_pos.append(pos)
            houses += 1
    return houses

def part_2(dat):
    dat = dat[0]
    houses = 1
    santa_pos = (0, 0)
    robo_pos = (0, 0)
    last_pos = [santa_pos]
    for ind, dn in enumerate(dat):
        if ind % 2 == 0: # Santa
            santa_pos = check_direction(dn, santa_pos)
            if check_position(santa_pos, last_pos):
                last_pos.append(santa_pos)
                houses += 1
        else: # Robo-Santa
            robo_pos = check_direction(dn, robo_pos)
            if check_position(robo_pos, last_pos):
                last_pos.append(robo_pos)
                houses += 1
    return houses

print(part_1(data))
print(part_2(data))
