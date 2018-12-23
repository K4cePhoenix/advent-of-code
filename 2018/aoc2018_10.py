from time import time
from matplotlib import pyplot as plt
import numpy as np
import re
import sys

try:
    import pytesseract
    import cv2
    imports = True
except:
    imports = False


with open(sys.argv[1], 'r') as f:
    data = f.read().split('\n')

def parse_data(dat):
    # 255 = black, # 180= dark gray, 127 = gray, 60 = light gray, 0 = white(background) etc.
    decode = {
        '!': 15,
        'S': 30,
        'M': 45,
        'X': 255,
        'E': 75,
        ')': 90,
        'I': 105,
        '/': 120,
        'C': 135,
        '-': 150,
        'O': 165,
        '+': 180,
        'H': 195,
        'T': 210,
        'R': 225,
        'Y': 240,
        'A': 250,
        '(': 60
    }    
    points = np.zeros((len(dat), 5), dtype=np.int64)
    pattern = r'(-?\d+|(?<=symbol=)\S)'
    if len(re.findall(pattern, dat[0])) == 4:
        for i in range(len(dat)):
            x0, y0, x1, y1 = re.findall(pattern, dat[i])
            val = 255
            points[i, :] = [x0, y0, x1, y1, val]
    elif len(re.findall(pattern, dat[0])) == 5:
        for i in range(len(dat)):
            x0, y0, x1, y1, val = re.findall(pattern, dat[i])
            val = decode[val]
            points[i, :] = [x0, y0, x1, y1, val]
    return points

def get_solution(data):
    data = parse_data(data)
    s = [[-999999, -999999],[999999, 999999]]
    t = 0
    while True:
        p = (np.argmin(data[:, :2], axis=0), np.argmax(data[:, :2], axis=0))
        ((tmix, tmiy), (tmax, tmay)) = ((data[p[0][0],0], data[p[0][1],1]), (data[p[1][0],0], data[p[1][1],1]))
        if tmax-tmix < s[1][0]-s[0][0] and tmay-tmiy < s[1][1]-s[0][1]:
            t += 1
            s = [[tmix, tmiy], [tmax, tmay]]
            data[:, :2] += data[:, 2:4]
        else:
            t -= 1
            data[:, :2] -= data[:, 2:4]
            break
    t1=time()
    im = np.ones((s[1][1]-s[0][1]+11, s[1][0]-s[0][0]+11), dtype=np.uint8)*255
    for lp in data:
        im[lp[1]-s[0][1]+5, lp[0]-s[0][0]+5] = 255 - lp[4]
    plt.plot(im, cmap='gray', interpolation='nearest')
    if imports:
        im2 = cv2.resize(np.invert(im), (int(im.shape[1]*3.5), int(im.shape[0]*3.5)), interpolation=cv2.INTER_NEAREST)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
        im2 = cv2.dilate(im2, kernel, iterations=1)
        text = pytesseract.image_to_string(im2)
        msg = f"Message:          {text}\nTheoretical wait: {t}\nTotal Runtime:    {time()-t0}\nLight movements:  {t1-t0}\nOpenCV + OCR:     {time()-t1}"
    else: msg = f"Theoretical wait: {t}\nTotal Runtime:    {time()-t0}"
    return msg

t0=time()
print(get_solution(data))
plt.show()
