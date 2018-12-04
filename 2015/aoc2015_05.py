
f = open('./input/aoc2015_05.txt', 'r')

data = f.readlines()

VOWELS = 'aeiou'
FORBIDDEN = ['ab', 'cd', 'pq', 'xy']

def part_1(dat):
    nice_strings = 0
    for string in data:
        vowel_counter = 0
        twice = False
        verboten = False
        for v in VOWELS:
            vowel_counter += string.count(v)
        for v in FORBIDDEN:
            if v in string:
                verboten = True
        for i in range(len(string)-1):
            if string[i] == string[i+1]:
                twice = True
        if vowel_counter >= 3 and twice and not verboten:
            nice_strings += 1
    return nice_strings

def part_2(dat):
    nice_strings = 0
    for string in dat:
        string = string.strip()
        pair = False
        twice = False
        even_pairs = set()
        odd_pairs = set()
        for i in range(len(string)):
            if i % 2 == 0 and i < len(string)-1:
                even_pairs.add(string[i:i+2])
            if i % 2 == 1 and i < len(string)-1:
                odd_pairs.add(string[i:i+2])
            if i < len(string)-2:
                if string[i] == string[i+2]:
                    twice = True
        if len(even_pairs) == len(string)/2 and len(odd_pairs) == (len(string)-2)/2:
            pass
        else:
            pair = True
        if pair and twice:
            nice_strings += 1
    return nice_strings

print(part_1(data))
print(part_2(data))
