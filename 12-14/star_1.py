def determine_quad(x, y):
    if x < verical_divide:
        if y < horizontal_divide:
            return 0
        elif y > horizontal_divide:
            return 3
    elif x > verical_divide:
        if y < horizontal_divide:
            return 1
        elif y > horizontal_divide:
            return 2

lines = open('in.txt').read().splitlines()
robots = []
width, height = 101, 103
for line in lines:
    p, v = line.split()
    px, py = p.split(',')
    vx, vy = v.split(',')
    robots.append(((int(px[2:]), int(py)), (int(vx[2:]), int(vy))))

moved_robots = []
quads = [0, 0, 0, 0]
verical_divide, horizontal_divide = width // 2, height // 2
for p, v in robots:
    px, py = p
    vx, vy = v
    new_px, new_py = (px + vx * 100) % 101, (py + vy * 100) % 103
    quad = determine_quad(new_px, new_py)
    if quad is not None:
        quads[quad] += 1
print(quads[0] * quads[1] * quads[2] * quads[3])