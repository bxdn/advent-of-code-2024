grid, moves = open('in.txt').read().split('\n\n')
grid = [list(row) for row in grid.splitlines()]
moves = ''.join(moves.splitlines())

offsets = {
    'v': (0, 1),
    '^': (0, -1),
    '>': (1, 0),
    '<': (-1, 0)
}

def process_grid():
    new_grid = []
    for row in grid:
        new_grid.append([])
        for val in row:
            if val == 'O':
                new_grid[-1].extend(['[', ']'])
            elif val == '@':
                new_grid[-1].extend(['@', '.'])
            else:
                new_grid[-1].extend([val, val])
    return new_grid


def find_robot():
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if val == '@':
                return x, y

def is_possible(x, y, offset_x, offset_y):
    next_x, next_y = x + offset_x, y + offset_y
    is_horizontal = bool(offset_x)
    if grid[next_y][next_x] == '.':
        return True
    if grid[next_y][next_x] == ']':
        return is_possible(next_x, next_y, offset_x, offset_y) and (is_horizontal or is_possible(next_x - 1, next_y, offset_x, offset_y))
    elif grid[next_y][next_x] == '[':
        return is_possible(next_x, next_y, offset_x, offset_y) and (is_horizontal or is_possible(next_x + 1, next_y, offset_x, offset_y))
    elif grid[next_y][next_x] == '#':
        return False
    
def propagate_move(x, y, offset_x, offset_y, moved):
    if (x, y) in moved:
        return
    next_x, next_y = x + offset_x, y + offset_y
    is_horizontal = bool(offset_x)
    if grid[next_y][next_x] == '@':
        propagate_move(next_x, next_y, offset_x, offset_y, moved)
    elif grid[next_y][next_x] == ']':
        propagate_move(next_x, next_y, offset_x, offset_y, moved)
        if not is_horizontal:
            propagate_move(next_x - 1, next_y, offset_x, offset_y, moved)
    elif grid[next_y][next_x] == '[':
        propagate_move(next_x, next_y, offset_x, offset_y, moved)
        if not is_horizontal:
            propagate_move(next_x + 1, next_y, offset_x, offset_y, moved)
    grid[next_y][next_x] = grid[y][x]
    grid[y][x] = '.'
    moved.add((x, y))


grid = process_grid()
robot = find_robot()
for move in moves:
    offset = offsets[move]
    x, y = robot
    offset_x, offset_y = offset
    is_horizontal = bool(offset_x)
    if is_possible(x, y, offset_x, offset_y):
        propagate_move(x, y, offset_x, offset_y, set())
        grid[y][x] = '.'
        robot = (x + offset_x, y + offset_y)

total = 0
for y, row in enumerate(grid):
    for x, val in enumerate(row):
        if val == '[':
            total += 100 * y + x

print(total)