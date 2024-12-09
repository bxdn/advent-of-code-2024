inpt = list(map(int, list(open('in.txt').read())))
i, j = 0, len(inpt) - 1
total, count = 0, 0
idl, idr = 0, len(inpt) // 2
calc_subtotal = lambda j, k, n: round(.5 * j * (-(k ** 2) + k + n ** 2 + n))
while i <= j:
    if i % 2 == 0:
        total += calc_subtotal(idl, count, count + inpt[i] - 1)
        count += inpt[i]
        i += 1
        idl += 1
    elif inpt[i] > inpt[j]:
        total += calc_subtotal(idr, count, count + inpt[j] - 1)
        count += inpt[j]
        inpt[i] -= inpt[j]
        j -= 2
        idr -= 1
    else:
        total += calc_subtotal(idr, count, count + inpt[i] - 1)
        count += inpt[i]
        inpt[j] -= inpt[i]
        i += 1
print(total)
