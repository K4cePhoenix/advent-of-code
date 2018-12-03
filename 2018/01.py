
# Part One
f = open('data.txt', 'r')

freq = 0
for line in f.readlines():
    freq += int(line)

print("Part 1 result:", freq)


# Part Two
f = open('data.txt', 'r')
fcl = list()
for line in f.readlines():
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

print("Part 2 result:", freq)
