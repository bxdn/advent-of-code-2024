# Determines if the line is safe.
def is_safe(line):
    deltas = set(line[i] - line[i - 1] for i in range(1, len(line)))
    return set(deltas) <= {1, 2, 3} or set(deltas) <= {-1, -2, -3}

# Gets the lines from the file
lines = open('in.txt').readlines()

# Splits the numbers and casts them to ints
split_lines = map(str.split, lines)
cast_line = lambda line: list(map(int, line))
casted_lines = map(cast_line, split_lines)

# Find which lines are safe
results = map(is_safe, casted_lines)

# Print the number of lines that are safe
print(sum(results))