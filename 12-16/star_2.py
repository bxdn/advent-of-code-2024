import heapq

def find_start():
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if val == 'S':
                return (0, x, y, 0, None)

def handle_node(price, x, y, offset, prev):
    k = x, y, offset
    if price > total_price:
        return price
    if grid[y][x] == '#':
        return total_price
    if k in visited:
        if price == visited[k][0]:
            visited[k][1].add(prev)
        return total_price
    visited[k] = (price, {prev} if prev else {})
    if grid[y][x] == 'E':
        end_keys.add(k)
        return price
    x_offset, y_offset = offsets[offset]
    heapq.heappush(pq,(price + 1, x + x_offset, y + y_offset, offset, k))
    heapq.heappush(pq,(price + 1000, x, y, 3 if not offset else offset - 1, k))
    heapq.heappush(pq,(price + 1000, x, y, (offset + 1) % 4, k))
    return total_price
            
offsets = (1, 0), (0, 1), (-1, 0), (0, -1)

grid = [list(row) for row in open('in.txt').read().splitlines()]
pq = [find_start()]

visited = {}
total_price = float('inf')
next_total_price = float('inf')
end_keys = set()
while next_total_price <= total_price:
    total_price, next_total_price = next_total_price, handle_node(*heapq.heappop(pq))
    
all_best_spaces = set()
stack = list(end_keys)
while stack:
    next_key = stack.pop()
    all_best_spaces.add(next_key[:2])
    for k in visited[next_key][1]:
        stack.append(k)

print(len(all_best_spaces))
