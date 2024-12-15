grid, moves = open('in.txt').read().split('\n\n')
grid = [list(row) for row in grid.splitlines()]
moves = ''.join(moves.splitlines())

offsets = {
    'v': (0, 1),
    '^': (0, -1),
    '>': (1, 0),
    '<': (-1, 0)
}

def find_robot():
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if val == '@':
                return x, y
            
def find_first_empty(x, y, offset_x, offset_y):
    while grid[y][x] != '.':
        if grid[y][x] == '#':
            return None
        x, y = x + offset_x, y + offset_y
    return x, y
            
robot = find_robot()
for move in moves:
    offset = offsets[move]
    x, y = robot
    offset_x, offset_y = offset
    first_empty = find_first_empty(x, y, offset_x, offset_y)
    if first_empty is not None:
        adj_x, adj_y = x + offset_x, y + offset_y
        if first_empty != (adj_x, adj_y):
            empty_x, empty_y = first_empty
            grid[empty_y][empty_x] = 'O'
        grid[adj_y][adj_x] = '@'
        grid[y][x] = '.'
        robot = adj_x, adj_y

total = 0
for y, row in enumerate(grid):
    for x, val in enumerate(row):
        if val == 'O':
            total += 100 * y + x

for row in grid:
    print(''.join(row))
print(total)