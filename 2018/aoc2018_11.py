import numpy as np
import cv2
import timeit

t0 = timeit.default_timer()

with open('./2018/input/aoc2018_11.txt', 'r') as f:
    data = f.read().split('\n')

GRID_SIZE = 300

def parse_data(dat):
    return int(dat[0])

def get_power(x, y, s):
    rid = x + 10
    p = ((rid * y) + s) * rid
    p = p // 100 % 10
    return p - 5

def fill_fuelgrid(serial):
    return np.fromfunction(get_power, (GRID_SIZE, GRID_SIZE), s=serial)

def find_total_power(cg, k_off=3, _min=0, _max=0):
    size = power = 0
    for k in range(_min, _max+1):
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (k-_min+k_off,k-_min+k_off))
        ps = cv2.filter2D(cg, -1, kernel, borderType=cv2.BORDER_ISOLATED)
        print(cg.dtype, ps.dtype)
        if power < max(p for r in ps for p in r):
            power = max(p for r in ps for p in r)
            size = k
            y, x = np.where(ps >= max(p for r in ps for p in r))
    return x[0]-(size+k_off-1)//2, y[0]-(size+k_off-1)//2, size, power

def part_1(data):
    serial = parse_data(data)
    cells = fill_fuelgrid(serial)
    y, x, s, p = find_total_power(cells)
    return (x, y, s, p)

def part_2(data):
    serial = parse_data(data)
    cells = fill_fuelgrid(serial)
    y, x, s, p = find_total_power(cells, 1, 1, GRID_SIZE)
    return (x, y, s, p)

print(part_1(data))
t1=timeit.default_timer()
print(part_2(data))
print(t1-t0, timeit.default_timer()-t0)
