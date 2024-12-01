from typing import Counter


lines = open('in.txt').read().split('\n')
num_lines = len(lines)
row_length = len(lines[0])

is_cell = lambda x, y: 0 <= y < num_lines and 0 <= x < row_length

offsets = [(-1,-1), (-1, 1), (1, 1), (1, -1)]

center_counts = Counter()

def follow_through(x, y, offset_x, offset_y):
    to_check = 'MAS'
    for i, char in enumerate(to_check):
        cell_x, cell_y = x + offset_x * i, y + offset_y * i
        if not is_cell(cell_x, cell_y) or lines[cell_y][cell_x] != char:
            return False
    center_counts[(x + offset_x, y + offset_y)] += 1

for y in range(num_lines):
    for x in range(row_length):
        for offset_x, offset_y in offsets:
            follow_through(x, y, offset_x, offset_y)

is_xmas_center = lambda count: count == 2
xmas_centers = list(filter(is_xmas_center, center_counts.values()))
total = len(xmas_centers)

print(total)