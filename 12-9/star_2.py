inpt = list(map(int, list(open('in.txt').read())))
inpt = [(i // 2 if i % 2 == 0 else -1, num) for i, num in enumerate(inpt)]
inpt.append((-1, 0))
i = len(inpt) - 2
while i > 1:
    j = 1
    while j < i:
        _, blanks = inpt[j]
        id, file_size = inpt[i]
        if blanks >= file_size:
            if i == j + 1:
                inpt[j] = (-1, inpt[j][1] + inpt[i + 1][1])
            else:
                inpt[i-1] = (-1, inpt[i-1][1] + file_size + inpt[i+1][1])
                inpt[j] = (-1, blanks - file_size)
            del inpt[i]
            del inpt[i]
            inpt.insert(j, (id, file_size))
            inpt.insert(j, (-1, 0))
            i += 2
            break
        j += 2
    i -= 2
calc_subtotal = lambda j, k, n: round(.5 * j * (-(k ** 2) + k + n ** 2 + n))
total, count = 0, 0

for i in range(len(inpt)):
    id, num = inpt[i]
    if i % 2 == 0:
        total += calc_subtotal(id, count, count + num - 1)
    count += num

print(total)
