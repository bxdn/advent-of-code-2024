from collections import defaultdict
from itertools import combinations

lines = [line[:-1] for line in open('in.txt').readlines()]
num_lines, row_length = len(lines), len(lines[1])

is_cell = lambda x, y: 0 <= y < num_lines and 0 <= x < row_length
add = lambda a, b: a + b
subtract = lambda a, b: a - b

def get_signals():
    locations = defaultdict(list)
    for y in range(num_lines):
        for x in range(row_length):
            val = lines[y][x]
            if val != '.':
                locations[val].append((x, y))
    return locations

antinodes = set()
signals = get_signals()
for pos_list in signals.values():
    for pair in combinations(pos_list, 2):
        deltas = list(map(subtract, *pair))
        anti1, anti2 = pair
        while is_cell(*anti1):
            antinodes.add(anti1)
            anti1 = tuple(map(add, anti1, deltas))
        while is_cell(*anti2):
            antinodes.add(anti2)
            anti2 = tuple(map(subtract, anti2, deltas))
print(len(antinodes))
