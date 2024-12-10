lines = [list(map(int, line)) for line in open('in.txt').read().splitlines()]
num_lines, row_length = len(lines), len(lines[1])
is_cell = lambda x, y: 0 <= y < num_lines and 0 <= x < row_length

memos = [[None for _ in range(row_length)] for _ in range(num_lines)]
offsets = (1, 0), (0, 1), (-1, 0), (0, -1)
def calc_trailheads(x, y):
    if lines[y][x] == 9:
        return {(x, y)}
    if memos[y][x] is None:
        val = lines[y][x]
        end_points = set()
        for offset_x, offset_y in offsets:
            new_x, new_y = x + offset_x, y + offset_y
            if is_cell(new_x, new_y) and val == lines[new_y][new_x] - 1:
                end_points |= calc_trailheads(new_x, new_y)
        memos[y][x] = end_points
    return memos[y][x]

total = 0
for y, row in enumerate(lines):
    for x, val in enumerate(row):
        if not val:
            total += len(calc_trailheads(x, y))

print(total)

    