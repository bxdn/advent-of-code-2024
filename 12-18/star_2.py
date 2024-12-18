from collections import deque

def handle_node(price, *coords):
    x, y = coords
    if not grid[y + 1][x + 1] or coords in visited:
        return None
    visited.add(coords)
    if x == 70 and y == 70:
        return price
    for offset in offsets:
        x_offset, y_offset = offset
        q.appendleft((price + 1, x + x_offset, y + y_offset))
            
offsets = (1, 0), (0, 1), (-1, 0), (0, -1)

bad_memories = open('in.txt').read().splitlines()
convert_line = lambda s: tuple(map(int, s.split(',')))
bad_memories = list(map(convert_line, bad_memories))
first_bad_memories = set(bad_memories[:1024])

get_value_at_coords = lambda x, y: (x, y) not in first_bad_memories and 0 <= y <= 70 and 0 <= x <= 70
grid = [[get_value_at_coords(x, y) for x in range(-1, 72)] for y in range(-1, 72)]

for i in range(1024, len(bad_memories)):
    bad_memory_x, bad_memory_y = bad_memories[i]
    grid[bad_memory_y + 1][bad_memory_x + 1] = False
    q = deque([(0, 0, 0)])
    visited = set()
    total_price = None
    while q and not total_price:
        total_price = handle_node(*q.pop())
    if not total_price:
        print(f'{bad_memory_x},{bad_memory_y}')
        break