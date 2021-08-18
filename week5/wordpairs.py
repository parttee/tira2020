def count(t):
    n = len(t)

    sets = {}

    for i in range(n):
        v = set(t[i])
        k = ''.join(sorted([c for c in v]))
        if k not in sets:
            sets[k] = 0
        sets[k] += 1

    c = 0

    for k in sets:
        if sets[k] > 1:
            c += sets[k] * (sets[k] - 1) // 2

    return c


if __name__ == "__main__":
    print(count(["A", "AA", "AAA"]))  # 3
    print(count(["A", "B", "C"]))  # 0
    print(count(["KALA", "ALA", "LAKKA"]))  # 1
    print(count(['CA', 'CCACA', 'CCCB', 'C', 'CCCB']))  # 2
    print(count(['CBCCC', 'BB', 'BBC', 'CB', 'B',
                 'ACCC', 'BBC', 'CAB', 'ABAAB', 'BCBAC']))  # 8
    # print(count(['AAA', 'AA', 'AAAAAA', 'AAAAAA', 'AAAA', 'AAAAA', 'AAAAAA', 'AAA', 'AAAAAAA', 'AAAA', 'AAAAA', 'AAA', 'AAAAA', 'AAAA', 'AAAAAAAAAA', 'AAA', 'AAAA', 'AAAA', 'AAAAAA', 'AAAAAA', 'AA', 'AAAAA', 'A', 'AAAAA', 'AAAAAAA', 'AAAAAAAA', 'AAAAA', 'AAAAAAAA', 'AAAAAAAAA', 'AAAAAAA', 'AA', 'AAA', 'AAAAAA', 'A', 'AA', 'AAAAAA', 'A', 'AA', 'AAAAAA', 'AAA', 'AA', 'AAAA', 'AAAAAAAAAA', 'AAAAAAAAAA', 'AAAAAAA', 'AAAAAAAAA', 'AA', 'AAAAAAA', 'AAAAAAAAAA', 'AAAAAAAAAA', 'AAAAAAAAAA', 'AAA', 'AAAA', 'A',
    #              'AAAAAAA', 'AAAAAAAAAA', 'A', 'AAA', 'AAA', 'AAAAAAAA', 'A', 'A', 'AAAAAAA', 'AAAAAAA', 'AAAA', 'AAA', 'AAAAAAAAA', 'AAAAAAAA', 'AAA', 'AAAAA', 'AAAAAAAAAA', 'AAAAAA', 'AAAAA', 'AAAAA', 'AAAAAAA', 'AA', 'AAAAAAA', 'AAAAAAA', 'AAAAAAAA', 'AAAAAAAA', 'AA', 'AAA', 'AAAAAAA', 'AAAAAAAA', 'AAAAAAA', 'A', 'AAAAA', 'AAAA', 'A', 'AAA', 'A', 'AAAA', 'AAAAAAA', 'AAAAAAA', 'AAAAAAAAA', 'AAA', 'AAAAAAA', 'AAAAAAAAAA', 'AAA', 'AAA', 'AAAAAA', 'AAAAAAA', 'AAAAAA', 'A', 'AAAAAA', 'AAAAA', 'AAAA', 'AA', 'AAAAAAAA'] * 20))  # 1
