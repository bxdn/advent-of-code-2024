from collections import Counter
with open('input.txt') as infile: lines = infile.readlines()
l1, l2 = (map(int, l) for l in zip(*[line.split() for line in lines]))
list_2_counts = Counter()
for num in l2: list_2_counts[num] += 1
print(sum(num * list_2_counts[num] for num in l1))