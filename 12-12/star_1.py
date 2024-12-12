lines = open('in.txt').read().splitlines()
num_lines, row_length = len(lines), len(lines[1])
is_cell = lambda coords: 0 <= coords[1] < num_lines and 0 <= coords[0] < row_length

offsets = (1, 0), (-1, 0), (0, 1), (0, -1)

get_neighbor = lambda coords, offset: (coords[0] + offset[0], coords[1] + offset[1])

def get_region(coords, char, region, visited):
    x, y = coords
    if coords in visited or not is_cell(coords) or lines[y][x] != char:
        return
    visited.add(coords)
    region.append(coords)
    for offset in offsets:
        get_region(get_neighbor(coords, offset), char, region, visited)


def get_regions():
    regions = []
    visited = set()
    for y, line in enumerate(lines):
        for x, val in enumerate(line):
            coords = x, y
            if coords not in visited:
                region = []
                get_region(coords, val, region, visited)
                regions.append(region)
    return regions

def get_perimeter(region):
    perimeter = 0
    char = lines[region[0][1]][region[0][0]]
    for coords in region:
        for offset in offsets:
            neighbor = get_neighbor(coords, offset)
            neighbor_x, neighbor_y = neighbor
            if not is_cell(neighbor) or lines[neighbor_y][neighbor_x] != char:
                perimeter += 1
    return perimeter


total = 0
for region in get_regions():
    total += get_perimeter(region) * len(region)

print(total)
