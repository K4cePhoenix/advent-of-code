
# Part One
f = open('./2018/input/aoc2018_01.txt', 'r')
data = f.readlines()

freq = 0
for line in data:
    freq += int(line)

print(freq)


# Part Two
fcl = list()
for line in data:
    fcl.append(int(line))

c = True
freq = 0
s = set([freq])
while c:
    for j in fcl:
        freq += j
        if freq in s:
            c = False
            break
        s.add(freq)

print(freq)
