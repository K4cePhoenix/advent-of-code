
# Part One
f = open('./input/01.txt', 'r')
data = f.readlines()

twos = 0
threes = 0
for line in data:
    _dict = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0,
             'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0,
             'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0, }
    two = False
    three = False
    line = line.strip()

    for ind in range(0, len(line)):
        _dict[line[ind]] = int(_dict[line[ind]]) + 1
    for key in _dict:
        if _dict[key] == 2:
            two = True
        elif _dict[key] == 3:
            three = True

    twos += two
    threes += three

print(twos, threes, twos*threes)


# Part Two

for lind in range(0, len(data)):
    line = data[lind].strip()
    for lind2 in range (lind, len(data)):
        line2 = data[lind2].strip()
        if line == line2:
            pass
        else:
            result = ''
            for ind in range(0, len(line)):
                if line[ind] == line2[ind]:
                    result += line[ind]
            if len(result) == len(line)-1:
                print(result)
