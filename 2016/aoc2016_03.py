
f = open('./2016/input/aoc2016_03.txt', 'r')

data = f.readlines()

def part_1(dat):
    triangles = 0
    for line in dat:
        a, b, c = map(int, line.split())
        if a+b+c-max(a, b, c) > max(a, b, c):
            triangles += 1
    return triangles

def part_2(dat):
    triangles = 0
    dat_lst = list()
    tru_lst = list()

    for line in dat:
        t1, t2, t3 = map(int, line.split())
        dat_lst.append([t1, t2, t3])

    for i in range(len(dat_lst)):
        if i % 3 == 0:
            for j in range(3):
                tmp_lst = [dat_lst[i][j], dat_lst[i+1][j], dat_lst[i+2][j]]
                tmp_lst.sort()
                tru_lst.append(tmp_lst)

    for row in tru_lst:
        if sum(row)-max(row) > max(row):
            triangles += 1
    return triangles

print(part_1(data))
print(part_2(data))
