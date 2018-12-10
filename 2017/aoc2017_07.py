import numpy as np

with open('./2017/input/aoc2017_07.txt', 'r') as f:
    data = f.read().split('\n')

class Tower():
    def __init__(self, n, w, c=[]):
        self.name = n
        self.weight = w
        self.children = c

    def has_children(self):
        return any(self.children)

def parse_data(dat):
    towers = list()
    for line in dat:
        if len(line.split(' -> ')) == 2:
            nw, c = line.split(' -> ')
            name, weight = nw.split()
            t = Tower(name, int(weight[1:-1]), c.split(', '))
            towers.append(t)
        elif len(line.split('->')) == 1:
            name, weight = line.split()
            t = Tower(name, int(weight[1:-1]))
            towers.append(t)
    return towers

def part_1(data):
    data = parse_data(data)
    ind = 0
    while data:
        if len(data) == 1:
            return data[0].name
        if data[ind].children:
            for child in data[ind].children:
                found = False
                for i in range(len(data)):
                    if child == data[i].name and not data[i].has_children():
                        data[ind].children.remove(child)
                        data.pop(i)
                        ind -= 1
                        found = True
                        break
                if found:
                    break
        ind += 1
        if ind >= len(data):
            ind = 0

def part_2(data):
    data = parse_data(data)
    tmp = data
    ind = 0
    while tmp:
        if len(tmp) == 1:
            return tmp[0].name
        if tmp[ind].children:
            for child in tmp[ind].children:
                found = False
                for i in range(len(tmp)):
                    if child == tmp[i].name and not tmp[i].has_children():
                        tmp[ind].children.remove(child)
                        tmp[ind].weight += tmp[i].weight
                        found = True
                        break
                if found:
                    break
        ind += 1
        if ind >= len(tmp):
            ind = 0
            for tower in tmp:
                print(tower.name, tower.weight)

data = [
    "pbga (66)",
    "xhth (57)",
    "ebii (61)",
    "havc (66)",
    "ktlj (57)",
    "fwft (72) -> ktlj, cntj, xhth",
    "qoyq (66)",
    "padx (45) -> pbga, havc, qoyq",
    "tknk (41) -> ugml, padx, fwft",
    "jptl (61)",
    "ugml (68) -> gyxo, ebii, jptl",
    "gyxo (61)",
    "cntj (57)",
]

print(part_1(data))
print(part_2(data))
