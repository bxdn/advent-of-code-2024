from collections import Counter

nums = open('in.txt').read().split()
counts = Counter(nums)
for i in range(75):
    new_counts = Counter()
    for num in counts:
        count = counts[num]
        if num == '0':
            new_counts['1'] += count
        elif not len(num) & 1:
            new_length = len(num)//2
            new_counts[str(int(num[:new_length]))] += count
            new_counts[str(int(num[new_length:]))] += count
        else:
            new_counts[str(int(num) * 2024)] += count
    counts = new_counts
print(sum(counts.values()))
