from collections import defaultdict
from datetime import datetime
import re

f = open('./input/aoc2018_05.txt', 'r')
data = f.readlines()
f.close()

def solve_polymers(dat, pairs):
    res = dat+''
    while True:
        tmp = dat
        for pair in pairs:
            tmp = tmp.replace(pair, '')
        res = tmp
        if res == dat:
            break
        dat = res
    return res

def part_1(data):
    dat = data[0].strip()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    pairs = [l + l.upper() for l in alphabet]
    pairs += [l.upper() + l for l in alphabet]
    return len(solve_polymers(dat, pairs))

def part_2(data):
    dat = data[0].strip()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    pairs = [l + l.upper() for l in alphabet]
    pairs += [l.upper() + l for l in alphabet]
    res = 999999999999999
    for l in alphabet:
        tmp = dat+''
        tmp = tmp.replace(l, '')
        tmp = tmp.replace(l.upper(), '')
        tmp = solve_polymers(tmp, pairs)
        if len(tmp) < res:
            res = len(tmp)
    return res

print(part_1(data))
print(part_2(data))
