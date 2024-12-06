offsets = (0,-1), (1,0), (0,1), (-1, 0)
lines = open('in.txt').readlines()
num_lines, row_length = len(lines), len(lines[1])
is_cell = lambda x, y: 0 <= y < num_lines and 0 <= x < row_length
guard_pos = None
for y, line in enumerate(lines):
    x = line.find('^')
    if x > 0:
        guard_pos = (x, y)
        break

visited = set()
current_offset = 0
while is_cell(*guard_pos):
    visited.add(guard_pos)
    offset_x, offset_y = offsets[current_offset]
    x, y = guard_pos
    next_x, next_y = offset_x + x, offset_y + y
    if is_cell(next_x, next_y) and lines[next_y][next_x] == '#':
        current_offset = (current_offset + 1) % 4
    else:
        guard_pos = next_x, next_y
print(len(visited))