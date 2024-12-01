from re import findall

# Get input
content = open('in.txt').read()

# Finds all instances of the pattern 'mul(<int1>,<int2>)' and captures the numbers into groups
matches = findall(r'mul\((\d+),(\d+)\)', content)

# Finds the product for a match
calculate_product = lambda nums: int(nums[0]) * int(nums[1])

# Calculates the products
products = map(calculate_product, matches)

# Sums the products
total = sum(products)

print(total)