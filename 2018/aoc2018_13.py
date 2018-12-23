import timeit
import numpy as np
from matplotlib import pyplot as plt

t0 = timeit.default_timer()

with open('./2018/input/aoc2018_13.txt', 'r') as f:
    data = f.read().split('\n')

class Cart():
    def __init__(self, x, y, direction, id_):
        self.x = x
        self.y = y
        self.dir = direction
        self._dir_change = -1
        self.id = id_

    def move(self):
        if self.dir == 3:
            self.y -= 1
        elif self.dir == 2:
            self.x += 1
        elif self.dir == 1:
            self.y += 1
        elif self.dir == 0:
            self.x -= 1
        return self

    def update_dir_intersect(self):
        self.dir = (self.dir + self._dir_change) % 4
        self._dir_change = (self._dir_change % 2) - 1

    def update_dir_curve(self, change_):
        self.dir = (self.dir + change_) % 4

def parse_data(dat):
    parsed = np.zeros((len(dat[0]),len(dat)), np.int8)
    carts = list()
    id_ = 0
    for i in range(len(dat)):
        for j in range(len(dat[0])):
            if dat[i][j] in ['+']:
                parsed[i, j] = 4
            elif dat[i][j] == '\\':
                parsed[i, j] = 3
            elif dat[i][j] == '/':
                parsed[i, j] = 2
            elif dat[i][j] in ['|', '-']:
                parsed[i, j] = 1
            elif dat[i][j] in ['<', '>', 'v', '^']:
                if dat[i][j] == '^':
                    carts.append(Cart(i, j, 0, id_))
                elif dat[i][j] == '>':
                    carts.append(Cart(i, j, 1, id_))
                elif dat[i][j] == 'v':
                    carts.append(Cart(i, j, 2, id_))
                elif dat[i][j] == '<':
                    carts.append(Cart(i, j, 3, id_))
                parsed[i, j] = 1
                id_ += 1
    return parsed, carts

def move_carts(map_, carts):
    cart_map = np.zeros_like(map_)
    for cart in carts:
        cart_map[cart.x, cart.y] = cart.id
    cart_order = np.where(cart_map > 0)
    print(cart_map[cart_order])
    for i in range(cart_order[0].shape[0]):
        for cart in carts:
            if cart_map[cart_order[0][i], cart_order[0][i]] == cart.id:
                cart.move()
                if map_[cart.x, cart.y] == 4:
                    cart.update_dir_intersect()
                elif map_[cart.x, cart.y] == 3 and cart.dir % 2 == 0:
                    cart.update_dir_curve(-1)
                elif map_[cart.x, cart.y] == 3 and cart.dir % 2 == 1:
                    cart.update_dir_curve(1)
                elif map_[cart.x, cart.y] == 2 and cart.dir % 2 == 0:
                    cart.update_dir_curve(1)
                elif map_[cart.x, cart.y] == 2 and cart.dir % 2 == 1:
                    cart.update_dir_curve(-1)
                for cart2 in carts:
                    if cart.id != cart2.id and cart.x == cart2.x and cart.y == cart2.y:
                        map_[cart.x, cart.y] = -1
                        return map_, carts
    return map_, carts

def part_1(data):
    map_tracks, carts = parse_data(data)
    i = 0
    while True:
        i += 1
        map_tracks, carts = move_carts(map_tracks, carts)
        if -1 in map_tracks:
            x, y = np.where(map_tracks == -1)
            return (x[0], y[0])

def part_2(data):
    pass

print(part_1(data))
t1=timeit.default_timer()
print(part_2(data))
print(t1-t0, timeit.default_timer()-t1)
