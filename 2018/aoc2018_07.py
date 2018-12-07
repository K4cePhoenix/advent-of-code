import numpy as np
import cv2
import itertools
from collections import OrderedDict
from string import ascii_uppercase

with open('./input/aoc2018_07.txt', 'r') as f:
    data = f.read().split('\n')

def parse_data(dat):
    parsed = OrderedDict()
    for c in ascii_uppercase:
        parsed[c] = ''
    for line in dat:
        tmp = line.split(" must be finished before step ")
        req = tmp[0].split(' ')[-1]
        act = tmp[1].split(' ')[0]
        parsed[act] += req
    return parsed

def assemble(dat, order):
    for key in dat.keys():
        if dat[key] == '' and key not in order:
            order += key
            for k2 in dat.keys():
                dat[k2] = dat[k2].replace(key, '')
            return dat, order
    return dat, order

class Worker():
    def __init__(self, mt):
        self.task = ''
        self.time = 0
        self.idle = True
        self.min_time = mt

    def asign_task(self, task):
        self.idle = False
        self.task = task
        self.time = ord(task) - (ord('A')-1) + self.min_time

    def work(self, dat, rem):
        self.time -= self.time > 0
        if self.time == 0:
            self.idle = True
            rem = rem.replace(self.task, '')
            for k2 in dat.keys():
                dat[k2] = dat[k2].replace(self.task, '')
        return dat, rem

def asign_worker(dat, worker, asigned, avail):
    for key in dat.keys():
        if dat[key] == '' and key in avail and key not in asigned:
            worker.asign_task(key)
            avail = avail.replace(key, '')
            return dat, worker, avail
    return dat, worker, avail

def check_req(dat, rem):
    a = ''
    for key in dat:
        if dat[key] == '' and key in rem:
            a += key
    return a

def part_1(data):
    parsel = parse_data(data)
    new_order = ''
    while True:
        old_order = new_order
        parsel, new_order = assemble(parsel, old_order)
        if new_order == old_order:
            return new_order

def part_2(data, mt, wn):
    parsel = parse_data(data)
    total_worktime = 0
    remaining = ascii_uppercase
    available = ''
    workers = list()
    for i in range(wn):
        w = Worker(mt)
        workers.append(w)
    while True:
        available = check_req(parsel, remaining)
        for i, worker in enumerate(workers):
            asigned = [w.task for w in workers]
            if worker.idle:
                parsel, worker, available = asign_worker(parsel, worker, asigned, available)
            parsel, remaining = worker.work(parsel, remaining)
        total_worktime += 1
        if not remaining and all(w.idle for w in workers):
            return total_worktime

MIN_TIME = 60
WORKER_NUM = 5

print(part_1(data))
print(part_2(data, MIN_TIME, WORKER_NUM))
