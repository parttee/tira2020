from collections import deque

# FAIL!


def count(s):
    n = len(s)
    cnt = 0

    d = {"A": 0, "B": 0, "C": 0}
    dc = {"A": {}, "B": {}, "C": {}}
    # d = {}
    m = [None] * n

    offset = {}

    for i in range(n):
        v = s[i]
        if m[i] == None:
            m[i] = {"A": 0, "B": 0, "C": 0}
            if i > 0:
                m[i]["A"] += m[i - 1]["A"]
                m[i]["B"] += m[i - 1]["B"]
                m[i]["C"] += m[i - 1]["C"]
        m[i][v] += 1
        if not v in offset:
            offset[v] = i
        # dc[v][i] = True

    maxO = max(offset.values())
    # CBACBA
    # CBACBACBA
    # CCBABACBA

    """
    ABCABCBBC (5)
    A   1 1 1 2 2 2 2 2 2 
    B   0 1 1 1 2 2 3 4 4 
    C   0 0 1 1 1 2 2 2 3


    CCAABB (1)
    C   1 2 2 2 2 2
    A   0 0 1 2 2 2
    B   0 0 0 0 1 2

    AABABCBCC (2)
    A   1 2 2 3 3 3 3 3 3
    B   0 0 1 1 2 2 4 3 3
    C   0 0 0 0 0 1 1 2 3

    AAABBBCCC (1)
    A   123 333 333
    B   000 123 333
    C   000 000 123

    ABCABC BBCABC ABC (14)
    A   111 222 222 333 444   36
    B   011 122 344 455 566   49
    C   001 112 223 334 445   35


    CBABCC (2) niin kertymät olisivat
    C   111 123
    B   011 222
    A   001 111

            1 0 1 0


    CBACBA (5)
    C   111 222
    B   011 122
    A   001 112

        CBA CBA
    """

    # offset = {"A": None, "B": None, "C": None}

    counter = {"A": 0, "B": 0, "C": 0}
    prev = {"A": 0, "B": 0, "C": 0}

    for i in range(n):
        v = s[i]

        # dc[v] += 1
        d[v] += 1

        if i < maxO:
            continue

        # if d["A"] == d["B"] == d["C"] and i == n - 1:
        #     cnt += 1

        for c in "ABC":
            if not c in offset:
                continue
            o = offset[c]
            if (i + 1 - o) % 3 == 0:
                # print("paaa", c, v, i, d[c], m[i - 2][c])
                if d[c] == m[i - 2][c] != m[i - 3][c]:
                    print("peinr", c, i)
                    counter[c] += 1

        # if add:
        #     counter[v] += 1

    print("counter", counter)

    for c in counter:
        cnt += int((counter[c] / 2) * (1 + counter[c]))

    return cnt


def scount(s):
    print("slow", s)
    n = len(s)
    c = 0

    for i in range(n):
        for i2 in range(i + 1, n + 1):
            st = s[i: i2]
            pim = {"A": 0, "B": 0, "C": 0}
            for i3 in st:
                pim[i3] += 1
            if pim["A"] == pim["B"] == pim["C"]:
                c += 1
                print(st)

    return c


if __name__ == "__main__":
    # print(count("CCAABB"))  # 1
    # print(count("BAACCBBBBCBABCBCBBCBACABBACBCAAAACAABBCBABACCBCBAABCBCBAABBAABACCBABABCCACACCBACBCCACBABACCBABCCBCABBCBAABABBBBACBAAABAABCCCBAABCBCCCCCCABCBCCABCBABBACBACAABCAABCCCAABAACBABBCACCBBCACBCCBBABBABCCCCBCABCCAAABBACBABCABBAACCBCACAACABBBBAAABBACABCBCBBACCACCBBCCCBACCBACACABCBACAABAABCBCCCACCACAACCBCABCCBBCACBAAAACCBCCBBBCAAAABCBCACBCCCABBCBCBACCBAAACCCACBAACABCBCACCCABACCACBBBABACBCBBABACABCCCACBCCCBACACCAABBACBABACCBAAAABACBBBABCBACBCBBBACABCBACBCAABBBACACBBBCABCCACBBCABAAAAAABBCCCCBABCAABCCBAACCBCACBAABAAAABCAABBACBBBAACCCCACBACACACABBCCBBAACCAACCBCBAABAACBBABAAACABCCCBCACABAABABBAABBCBBBBACBBBABBCBACCBBAABABCBAACABBCBABACCBABAAABACBBBCBCACCBBCACCABACACCCABBAABBCCACBCCBCCAACBBABBABCABAACBCCAAACAABABACBAACBCCBACACBACBACACBBABAACCAACCBBAABCCABCBABBBCABBABCBBBCBBABCAABCACCCBCAACCAAAACBAAACCAACABCABBCBAACCCABBBCCACAAACABBAACAABACABCCACCCBBAABBBABCBCACAAACBBBBBCAAABBCCCCAACABAACCBCCABBBBBAACACCBBCACBBCBCBCACCAABCABCCBBCCABACBCACAABCCCAABCACABBCCAAACCBBBACBCAAAAACACCBCCCBAACCCBABACCBCCBBCACAABA" * 5))  # 5
    print(count("CBACBA"))  # 5
    # print(count("AAABBC"))  # 0
    print(count("AAABBBCCC"))  # 1
    # print(scount("AABABCBCC"))  # 2
    print(count("CBABCC"))  # 2
    # print(scount("ABCABCBBC"))  # 5
    print(count("ABCABCBBCABCABC"))  # 14
    # print(scount("ABCABCBBC"))  # 5
    # print(count("BCACBBCCA"))  # 5
    # print(count("ABCBCABBC"))  # 4
    # print(count("ABCBCACBB"))  # 4
    # print(count("BCACBBCCA"))  # 2
