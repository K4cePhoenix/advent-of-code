import hashlib

f = open('./input/aoc2015_04.txt', 'r')

data = f.readlines()

def check_hash(_hash, num_of_zeros):
    if _hash.hexdigest()[:num_of_zeros] == '0'*num_of_zeros:
        return True

def part_1(dat):
    i = 0
    while True:
        i += 1
        md5 = hashlib.md5(f"{dat[0]}{i}".encode('utf-8'))
        if check_hash(md5, 5):
            return i

def part_2(dat):
    i = 0
    while True:
        i += 1
        md5 = hashlib.md5(f"{dat[0]}{i}".encode('utf-8'))
        if check_hash(md5, 6):
            return i

print(part_1(data))
print(part_2(data))
