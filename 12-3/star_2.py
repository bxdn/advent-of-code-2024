from re import findall

# Get input
content = open('in.txt').read()

# Finds all instances of the pattern 'mul(<int1>,<int2>)' and captures the numbers into groups
product_matches = findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", content)

# Loops through mul, do, and don't instances, adding only products that aren't following don't() instructions
total = 0
adding = True
for a, b, do, dont in product_matches:
    if do or dont:
        adding = bool(do)
    else:
        total += int(a) * int(b) * adding

# Print the total
print(total)