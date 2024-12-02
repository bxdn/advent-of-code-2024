# Get lines of data from file
lines = open('in.txt').readlines()

# Get each line as a pair of number strings
pairs = map(str.split, lines)

# Get each column as a collection of number strings
columns = zip(*pairs)

# Get each column as a sorted collection of integers
sort_ints = lambda l: sorted(map(int, l))
sorted_int_columns = map(sort_ints, columns)

# Get the distance collections
find_distance = lambda a, b: abs(a-b)
distances = map(find_distance, *sorted_int_columns)

# Prints the total of the distances
total_distance = sum(distances)
print(total_distance)