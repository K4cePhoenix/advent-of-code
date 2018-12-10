import numpy as np
from time import time
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

def parse_data(dat):
    points = list()
    for l in dat:
        pos, vel, _ = l.split('>')
        x0, y0 = map(int, pos.split('<')[1].split(', '))
        x1, y1 = map(int, vel.split('<')[1].split(', '))
        points.append(LightPoint(x0, y0, x1, y1))
    return points

def part_1(data):
    data = parse_data(data)
    s = 0
    tmp_x = tmp_y = 999999
    while True:
        x_diff = max(lp.position.x for lp in data) - min(lp.position.x for lp in data)
        y_diff = max(lp.position.y for lp in data) - min(lp.position.y for lp in data)
        if x_diff > tmp_x and y_diff > tmp_y:
            s -= 1
            for lp in data:
                lp.move(-1)
            sx = max(lp.position.x for lp in data)
            sy = max(lp.position.y for lp in data)
            mx = min(lp.position.x for lp in data)
            my = min(lp.position.y for lp in data)
            break
        tmp_x, tmp_y = x_diff, y_diff
        s += 1
        for lp in data:
            lp.move()
    im = np.zeros((sy+11-my, sx+11-mx))
    for lp in data:
        im[lp.position.y-my+5, lp.position.x-mx+5] = 255
    im2 = cv2.resize(im, (int(im.shape[1]*3.5), int(im.shape[0]*3.5)), interpolation=cv2.INTER_NEAREST)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
    im2 = cv2.dilate(im2, kernel, iterations=1)
    text = pytesseract.image_to_string(im2)
    return text, s, time()-t0

t0=time()
print(part_1(data))
