from time import time
import numpy as np
import pytesseract
import cv2

with open('./2018/input/aoc2018_10.txt', 'r') as f:
    data = f.read().split('\n')

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __mul__(self, other: int):
        x = self.x * other
        y = self.y * other
        return Point(x, y)

    def __str__(self):
        return f"{self.x}, {self.y}"

class LightPoint():
    def __init__(self, px, py, vx, vy):
        self.position = Point(px, py)
        self.velocity = Point(vx, vy)

    def __str__(self):
        return f"p:({self.position}) v:({self.velocity})"

    def move(self, seconds=1):
        self.position += self.velocity*seconds
        return self

# class LightPoints():
#     def __init__(self, list_of_lp):


def parse_data(dat):
    points = set()
    for l in dat:
        pos, vel, _ = l.split('>')
        x0, y0 = map(int, pos.split('<')[1].split(', '))
        x1, y1 = map(int, vel.split('<')[1].split(', '))
        points.add(LightPoint(x0, y0, x1, y1))
    return points

def part_1(data):
    data = parse_data(data)
    s = 0
    tmp_x = tmp_y = 999999
    while True:
        diff_x = max(lp.position.x for lp in data) - min(lp.position.x for lp in data)
        diff_y = max(lp.position.y for lp in data) - min(lp.position.y for lp in data)
        if diff_x > tmp_x and diff_y > tmp_y:
            s -= 1
            data = set(lp.move(-1) for lp in data)
            max_x = max(lp.position.x for lp in data)
            max_y = max(lp.position.y for lp in data)
            min_x = min(lp.position.x for lp in data)
            min_y = min(lp.position.y for lp in data)
            break
        tmp_x, tmp_y = diff_x, diff_y
        s += 1
        data = set(lp.move() for lp in data)
    im = np.zeros((max_y-min_y+11, max_x-min_x+11), dtype=np.uint8)
    for lp in data:
        im[lp.position.y-min_y+5, lp.position.x-min_x+5] = 255
    im = cv2.resize(im, (int(im.shape[1]*3.5), int(im.shape[0]*3.5)), interpolation=cv2.INTER_NEAREST)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
    im = cv2.dilate(im, kernel, iterations=1)
    text = pytesseract.image_to_string(im)
    cv2.imshow('', im)
    return f"{text} {s} {time()-t0}"

def parse_data2(dat):
    points = np.zeros((len(dat), 4), dtype=np.int64)
    for i in range(len(dat)):
        pos, vel, _ = dat[i].split('>')
        x0, y0 = map(int, pos.split('<')[1].split(', '))
        x1, y1 = map(int, vel.split('<')[1].split(', '))
        points[i, :] = [x0, y0, x1, y1]
    return points

def part_2(data):
    data = parse_data2(data)
    s = [[-999999, -999999],[999999, 999999]]
    t = 0
    while True:
        p = (np.argmin(data[:, :2], axis=0), np.argmax(data[:, :2], axis=0))
        tmax = data[p[1][0],0]
        tmix = data[p[0][0],0]
        tmay = data[p[1][1],1]
        tmiy = data[p[0][1],1]
        if tmax-tmix < s[1][0]-s[0][0] and tmay-tmiy < s[1][1]-s[0][1]:
            t += 1
            s[1][0] = tmax
            s[0][0] = tmix
            s[1][1] = tmay
            s[0][1] = tmiy
            data[:, :2] += data[:, 2:]
        else:
            t -= 1
            data[:, :2] -= data[:, 2:]
            break
    im = np.zeros((s[1][1]-s[0][1]+11, s[1][0]-s[0][0]+11), dtype=np.uint8)
    for lp in data:
        print(lp)
        im[lp[1]-s[0][1]+5, lp[0]-s[0][0]+5] = 255
    im = cv2.resize(im, (int(im.shape[1]*3.5), int(im.shape[0]*3.5)), interpolation=cv2.INTER_NEAREST)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
    im = cv2.dilate(im, kernel, iterations=1)
    text = pytesseract.image_to_string(im)
    cv2.imshow('', im)
    return f"{text} {s} {time()-t1}"

t0=time()
print(part_1(data))
t1=time()
print(part_2(data))
cv2.waitKey()
