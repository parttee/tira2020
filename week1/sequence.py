def generate(n):
    lst = ['1']

    i = 0
    while i < min(n, 30):
        prev = list(lst[i])
        counts = [[]]
        si = 0
        pk = prev[0]
        for k in prev:
            if pk != k:
                counts.append([])
                si += 1
            counts[si].append(k)
            pk = k
        nxt = ''
        for group in counts:
            nxt += str(len(group)) + group[0]
        lst.append(nxt)
        i += 1

    return str(lst[n - 1])


if __name__ == "__main__":
    print(generate(1))  # 1
    print(generate(2))  # 11
    print(generate(3))  # 21
    print(generate(4))  # 1211
    print(generate(5))  # 111221
