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
        point1, point2 = pair
        deltas = list(map(subtract, point1, point2))
        anti1 = tuple(map(subtract, point2, deltas))
        anti2 = tuple(map(add, point1, deltas))
        if is_cell(*anti1):
            antinodes.add(anti1)
        if is_cell(*anti2):
            antinodes.add(anti2)
print(len(antinodes))
