from collections import defaultdict

less_thans = defaultdict(list)

content = open('in.txt').read()

mappings_str, lists_str = content.split('\n\n')

mappings = mappings_str.split('\n')
lists = lists_str.split('\n')

for mapping_row in mappings:
    less, greater = mapping_row.split('|')
    less_thans[less].append(greater)

def determine_value(row):
    row = row.split(',')
    for i in range(len(row) - 1):
        item = row[i]
        if row[i + 1] not in less_thans[item]:
            return 0
    return int(row[len(row)//2])


print(sum(map(determine_value, lists)))
