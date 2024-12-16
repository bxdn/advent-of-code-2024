import heapq

def find_start():
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if val == 'S':
                return (0, x, y, 0)
            
def handle_node(price, x, y, offset):
    k = x, y, offset
    if grid[y][x] == '#' or k in visited:
        return None
    visited.add(k)
    if grid[y][x] == 'E':
        return price
    x_offset, y_offset = offsets[offset]
    heapq.heappush(pq,(price + 1, x + x_offset, y + y_offset, offset))
    heapq.heappush(pq,(price + 1000, x, y, 3 if not offset else offset - 1))
    heapq.heappush(pq,(price + 1000, x, y, (offset + 1) % 4))
            
offsets = (1, 0), (0, 1), (-1, 0), (0, -1)

grid = [list(row) for row in open('in.txt').read().splitlines()]
pq = [find_start()]

visited = set()
total_price = None
end_keys = set()
while pq and not total_price:
    total_price = handle_node(*heapq.heappop(pq))

print(total_price)
