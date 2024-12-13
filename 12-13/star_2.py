machines = open('in.txt').read().split('\n\n')

def convert_machine(machine):
    machine = machine.splitlines()
    b1 = machine[0].split()
    b1 = int(b1[2][2:-1]), int(b1[3][2:])
    b2 = machine[1].split()
    b2 = int(b2[2][2:-1]), int(b2[3][2:])
    p = machine[2].split()
    p = 10000000000000 + int(p[1][2:-1]), 10000000000000 + int(p[2][2:])
    return b1, b2, p

total = 0
for machine in machines:
    b1, b2, p = convert_machine(machine)
    b1_x, b1_y = b1
    b2_x, b2_y = b2
    p_x, p_y = p
    b1p = (p_x * b2_y - p_y * b2_x) / (b1_x * b2_y - b1_y * b2_x)
    b2p = (p_y * b1_x - p_x * b1_y) / (b1_x * b2_y - b1_y * b2_x)
    if abs(b1p - round(b1p)) < 1e-5 and abs(b2p - round(b2p)) < 1e-5:
        total += 3 * round(b1p) + round(b2p)

print(total)
