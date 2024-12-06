offsets = (0,-1), (1,0), (0,1), (-1, 0)
lines = open('in.txt').readlines()
num_lines, row_length = len(lines), len(lines[1])
is_cell = lambda x, y: 0 <= y < num_lines and 0 <= x < row_length
initial_guard_pos = None
for y, line in enumerate(lines):
    x = line.find('^')
    if x > 0:
        initial_guard_pos = (x, y)
        break

def get_all_visited():
    visited = set()
    current_offset = 0
    guard_pos = initial_guard_pos
    while is_cell(*guard_pos):
        visited.add(guard_pos)
        offset_x, offset_y = offsets[current_offset]
        x, y = guard_pos
        next_x, next_y = offset_x + x, offset_y + y
        if is_cell(next_x, next_y) and lines[next_y][next_x] == '#':
            current_offset = (current_offset + 1) % 4
        else:
            guard_pos = next_x, next_y
    return visited

total = 0
for placed_blocker in get_all_visited():
    visited = set()
    guard_pos = initial_guard_pos
    current_offset = 0
    looped = False
    while is_cell(*guard_pos):
        if (*guard_pos, current_offset) in visited:
            looped = True
            break
        visited.add((*guard_pos, current_offset))
        offset_x, offset_y = offsets[current_offset]
        x, y = guard_pos
        next_x, next_y = offset_x + x, offset_y + y
        if is_cell(next_x, next_y) and (lines[next_y][next_x] == '#' or (next_x, next_y) == placed_blocker):
            current_offset = (current_offset + 1) % 4
        else:
            guard_pos = next_x, next_y
    total += looped
print(total)