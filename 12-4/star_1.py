lines = open('in.txt').read().split('\n')
num_lines = len(lines)
row_length = len(lines[0])

is_cell = lambda x, y: 0 <= y < num_lines and 0 <= x < row_length
offsets = [(x, y) for x in range(-1, 2) for y in range(-1, 2) if x != 0 or y != 0]

def follow_through(x, y, offset_x, offset_y):
    to_check = 'XMAS'
    for i, char in enumerate(to_check):
        cell_x, cell_y = x + offset_x * i, y + offset_y * i
        if not is_cell(cell_x, cell_y) or lines[cell_y][cell_x] != char:
            return False
    return True

total = 0
for y in range(num_lines):
    for x in range(row_length):
        for offset_x, offset_y in offsets:
            total += follow_through(x, y, offset_x, offset_y)

print(total)