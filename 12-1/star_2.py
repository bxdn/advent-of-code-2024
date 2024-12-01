from collections import Counter

# Get lines of data from file
lines = open('in.txt').readlines()

# Get each line as a pair of number strings
pairs = map(str.split, lines)

# Get each column as a collection of number strings
columns = zip(*pairs)

# Convert the columns to integers
cast_column = lambda l: map(int, l)
column1, column2 = map(cast_column, columns)

# Get the number of times each number occurred in column 2
column_2_counts = Counter(column2)

# Calculate the products of the number in column 1 by how many instances of that number are in column 2
calculate_product = lambda num: num * column_2_counts[num]
products = map(calculate_product, column1)

# Print the total of the products
total = sum(products)
print(total)