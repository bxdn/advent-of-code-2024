def found_tree(grid):
    for line in grid:
        consecutive = 0
        for b in line:
            consecutive = consecutive + 1 if b else 0
            if consecutive >= 10:
                return True
    return False

lines = open('in.txt').read().splitlines()
robots = []
width, height = 101, 103
for line in lines:
    p, v = line.split()
    px, py = p.split(',')
    vx, vy = v.split(',')
    robots.append(((int(px[2:]), int(py)), (int(vx[2:]), int(vy))))

i = 0
while True:
    grid = [[False for _ in range(width)] for _ in range(height)]
    moved_robots = []
    for p, v in robots:
        px, py = p
        vx, vy = v
        grid[py][px] = True
        new_px, new_py = (px + vx) % 101, (py + vy) % 103
        moved_robots.append(((new_px, new_py), v))
    thresh = 10
    robots = moved_robots
    if found_tree(grid):
        break
    i += 1
print(i)