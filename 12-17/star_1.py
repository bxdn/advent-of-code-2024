def adv(operand):
    registers[0] //= 2 ** combos[operand]()
def bxl(operand):
    registers[1] ^= operand
def bst(operand):
    registers[1] = combos[operand]() % 8
def jnz(operand):
    if not registers[0]:
        return
    global instruction_number
    instruction_number = operand - 2
def bxc(_):
    registers[1] ^= registers[2]
def out(operand):
    output.append(str(combos[operand]() % 8))
def bdv(operand):
    registers[1] = registers[0] // 2 ** combos[operand]()
def cdv(operand):
    registers[2] = registers[0] // 2 ** combos[operand]()
instruction_mappings = {
    0: adv,
    1: bxl,
    2: bst,
    3: jnz,
    4: bxc,
    5: out,
    6: bdv,
    7: cdv
}
combos = {
    0: lambda: 0,
    1: lambda: 1,
    2: lambda: 2,
    3: lambda: 3,
    4: lambda: registers[0],
    5: lambda: registers[1],
    6: lambda: registers[2],
    7: lambda: print('SHOULD NOT GET HERE!'),
}

registers, instructions = open('in.txt').read().split('\n\n')
instructions = [int(instruction) for instruction in instructions.split()[-1].split(',')]
registers = [int(register.split()[-1]) for register in registers.splitlines()]

output = []
instruction_number = 0
while instruction_number < len(instructions):
    instruction, operand = instructions[instruction_number], instructions[instruction_number + 1]
    instruction_mappings[instruction](operand)
    instruction_number += 2

print(','.join(output))