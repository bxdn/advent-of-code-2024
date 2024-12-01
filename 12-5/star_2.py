from collections import defaultdict
from functools import cmp_to_key

less_thans = defaultdict(list)

content = open('in.txt').read()

mappings_str, lists_str = content.split('\n\n')

mappings = mappings_str.split('\n')
lists = lists_str.split('\n')

for mapping_row in mappings:
    less, greater = mapping_row.split('|')
    less_thans[less].append(greater)

cmp = lambda a, b: 1 if b not in less_thans[a] else -1

def determine_value(row):
    row = row.split(',')
    for i in range(len(row) - 1):
        item = row[i]
        if row[i + 1] not in less_thans[item]:
            row = sorted(row, key=cmp_to_key(cmp))
            return int(row[len(row)//2])
    return 0


print(sum(map(determine_value, lists)))
