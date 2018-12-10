import numpy as np
import collections

with open('./2017/input/aoc2017_06.txt', 'r') as f:
    data = f.read().split('\n')

def parse_data(dat):
    return collections.deque(map(int, dat[0].split()))

def part_1(data):
    data = parse_data(data)
    prev_banks = np.array([data])
    # print(data)
    while True:
        pos = np.where(data == np.amax(data))[0][0]
        realloc = data[pos]
        data[pos] = 0
        data.rotate(-(pos+1))
        tmp = realloc
        while realloc > 0:
            data.appendleft(data.popleft()+1)
            data.rotate(-1)
            realloc -= 1
        data.rotate(pos+1+tmp)
        # print(data)
        for bank in prev_banks:
            same = True
            for i in range(len(data)):
                if data[i] != int(bank[i]):
                    same = False
            if same:
                break
        if same:
            break
        prev_banks = np.append(prev_banks, [data], axis=0)
    return prev_banks.shape[0]

def part_2(data):
    data = parse_data(data)
    prev_banks = np.array([data])
    while True:
        pos = np.where(data == np.amax(data))[0][0]
        realloc = data[pos]
        data[pos] = 0
        data.rotate(-(pos+1))
        tmp = realloc
        while realloc > 0:
            data.appendleft(data.popleft()+1)
            data.rotate(-1)
            realloc -= 1
        data.rotate(pos+1+tmp)
        for i in range(prev_banks.shape[0]):
            same = True
            for j in range(len(data)):
                if data[j] != int(prev_banks[i][j]):
                    same = False
            if same:
                cycle_start = i+1
                break
        if same:
            break
        prev_banks = np.append(prev_banks, [data], axis=0)
    return prev_banks.shape[0]-cycle_start

# data = ["0 2 7 0"]

print(part_1(data))
print(part_2(data))
