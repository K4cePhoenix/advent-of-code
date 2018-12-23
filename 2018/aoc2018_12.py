import timeit
import re

t0 = timeit.default_timer()

with open('./2018/input/aoc2018_12.txt', 'r') as f:
    data = f.read().split('\n')

def parse_data(dat):
    init_str = re.findall(r"((?<=state:.)\S+)", dat[0])
    spreads = list()
    leads = list()
    for l in dat[2:]:
        pattern = r"(\S+(?=.=>))"
        spread = re.findall(pattern, l)
        spreads.append(spread)
        pattern = r"((?<==>.)\S)"
        lead = re.findall(pattern, l)
        leads.append(lead)
    initial_state = list()
    for _ in range(3):
        initial_state.append('.')
    for c in init_str[0]:
        initial_state.append(c)
    for _ in range(3):
        initial_state.append('.')
    return initial_state, spreads, leads

def gen_next(state, spreadsheet, resultsheet, t):
    tmp = state
    states = list()
    states.append(state)
    for i in range(t):
        new_state = list()
        new_state.append('.')
        new_state.append('.')
        for j in range(2, len(state)-2):
            plant_neighbourhood = state[j-2], state[j-1], state[j], state[j+1], state[j+2]
            for k in range(len(spreadsheet)):
                if ''.join(plant_neighbourhood) == spreadsheet[k][0]:
                    new_state.append(resultsheet[k][0])
                    break
        new_state.append('.')
        new_state.append('.')
        new_state.append('.')
        states.append(new_state)
        state = states[-1]
    return states

def gen_next2(state, spreadsheet, resultsheet, t):
    states = list()
    states.append(state)
    k = 0
    for i in range(t):
        new_state = list()
        new_state.append('.')
        new_state.append('.')
        for j in range(2, len(state)-2):
            plant_neighbourhood = state[j-2], state[j-1], state[j], state[j+1], state[j+2]
            for k in range(len(spreadsheet)):
                if ''.join(plant_neighbourhood) == spreadsheet[k][0]:
                    new_state.append(resultsheet[k][0])
                    break
        new_state.append('.')
        new_state.append('.')
        new_state.append('.')
        total = 0
        if new_state == states[-1]:
            for c in range(len(new_state[2:])):
                if new_state[c] == '#':
                    total += c
            print(total)
            return None
        if i%1000 == 0:
            print(i, '/', t, ' - ', timeit.default_timer()-t1)
        states.append(new_state)
        state = states[-1]

def part_1(data):
    initial_state, spread_rules, spread_results = parse_data(data)
    repeats = 20
    states = gen_next(initial_state, spread_rules, spread_results, repeats)
    total = 0
    for state in states:
        print(''.join(state))
    for i in range(len(states[-1])):
        if states[-1][i] == '#':
            total += i-3
    return total

def part_2(data):
    initial_state, spread_rules, spread_results = parse_data(data)
    repeats = 5000000000
    # state, k = gen_next2(initial_state, spread_rules, spread_results, repeats)
    gen_next2(initial_state, spread_rules, spread_results, repeats)
    total = 0
    for i in range(len(state)):
        if state[i] == '#':
            total += i+k-3
    return total

print(part_1(data))
t1=timeit.default_timer()
print(part_2(data))
print(t1-t0, timeit.default_timer()-t1)
