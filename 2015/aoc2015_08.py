
f = open('./input/aoc2015_08.txt', 'r')

data = f.readlines()

def part_1(dat):
    n_memory = 0
    n_literal = 0
    for line in dat:
        line = line.strip()
        n_memory += 2
        i = 1
        while (i < len(line)-1):
            if not line[i].isalnum():
                if line[i] == '\\':
                    if line[i+1] == '"':
                        i += 2
                        n_literal += 1
                        n_memory += 2
                    elif line[i+1] == 'x':
                        i += 4
                        n_literal += 1
                        n_memory += 4
                    elif line[i+1] == '\\':
                        i += 2
                        n_literal += 1
                        n_memory += 2
            else:
                i += 1
                n_literal += 1
                n_memory += 1
    return n_memory - n_literal

def part_2(dat):
    n_memory = 0
    n_literal = 0
    for line in dat:
        line = line.strip()
        line = line.replace('\\', '\\\\').replace('"', '\\"')
        n_memory += 2
        i = 0
        while (i < len(line)):
            if not line[i].isalnum():
                if line[i] == '\\':
                    if line[i+1] == '"':
                        i += 2
                        n_literal += 1
                        n_memory += 2
                    elif line[i+1] == 'x':
                        i += 4
                        n_literal += 1
                        n_memory += 4
                    elif line[i+1] == '\\':
                        i += 2
                        n_literal += 1
                        n_memory += 2
            else:
                i += 1
                n_literal += 1
                n_memory += 1
    return n_memory - n_literal

print(part_1(data))
print(part_2(data))
