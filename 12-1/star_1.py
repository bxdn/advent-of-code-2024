with open('input.txt') as infile: lines = infile.readlines()
l1, l2 = (sorted(map(int, l)) for l in zip(*(line.split() for line in lines)))
print(sum(map(lambda i: abs(l1[i] - l2[i]), range(len(l1)))))