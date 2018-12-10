from string import ascii_lowercase
import numpy as np

with open('./2017/input/aoc2017_04.txt', 'r') as f:
    data = f.read().split('\n')

def part_1(data):
    valid_phrases = 0
    for l in data:
        d = l.split()
        valid = True
        for i in range(len(d)):
            if d[i] in d[:i]:
                valid = False
                break
            if d[i] in d[i+1:]:
                valid = False
                break
        if valid:
            valid_phrases += 1
    return valid_phrases

def part_2(data):
    valid_phrases = 0
    for l in data:
        d = l.split()
        valid = True
        for i in range(len(d)):
            for j in range(i+1, len(d)):
                if len(d[i]) == len(d[j]):
                    w0 = np.zeros(len(ascii_lowercase))
                    w1 = np.zeros(len(ascii_lowercase))
                    for k in d[i]:
                        w0[ord(k)-ord('a')] += 1
                    for k in d[j]:
                        w1[ord(k)-ord('a')] += 1
                    if all(w0 == w1):
                        valid = False
        if valid:
            valid_phrases += 1
    return valid_phrases


print(part_1(data))
print(part_2(data))
