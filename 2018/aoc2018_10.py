from time import time
import numpy as np
import pytesseract
import cv2

with open('./2018/input/aoc2018_10.txt', 'r') as f:
    data = f.read().split('\n')

def parse_data(dat):
    points = np.zeros((len(dat), 4), dtype=np.int64)
    for i in range(len(dat)):
        pos, vel, _ = dat[i].split('>')
        x0, y0 = map(int, pos.split('<')[1].split(', '))
        x1, y1 = map(int, vel.split('<')[1].split(', '))
        points[i, :] = [x0, y0, x1, y1]
    return points

def get_solution(data):
    data = parse_data(data)
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
        im[lp[1]-s[0][1]+5, lp[0]-s[0][0]+5] = 255
    im = cv2.resize(im, (int(im.shape[1]*3.5), int(im.shape[0]*3.5)), interpolation=cv2.INTER_NEAREST)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
    im = cv2.dilate(im, kernel, iterations=1)
    text = pytesseract.image_to_string(im)
    cv2.imshow('', im)
    return f"{text} {t} {time()-t0}"

t0=time()
print(get_solution(data))
cv2.waitKey()
