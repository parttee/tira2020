from collections import deque


def solve(s):
    # print("str\t", s)
    s = list(s)
    n = len(s)

    d = {"A": 0, "B": 0, "C": 0}
    lst = {"A": {}, "B": {}, "C": {}}
    cnt = 0

    for i in range(n):
        c = s[i]
        d[c] += 1

    correct = ""
    for c in d:
        amount = (d[c])
        correct += (c * amount)

    for i in range(n):
        cur = s[i]
        cor = correct[i]
        if cor != cur:
            if lst[cor].get(cur) == None:
                lst[cor][cur] = deque([])
            lst[cor][cur].append(i)

    for i in range(n):
        cur = s[i]
        cor = correct[i]
        if cor != cur:
            val = lst[cur].get(cor)
            if val is not None and len(val) > 0:
                index = lst[cur][cor].popleft()
                s[i] = cor
                s[index] = cur
                cnt += 1
            else:
                for c in "ABC":
                    val = lst[cur].get(c)
                    if val is not None and len(val) > 0:
                        index = lst[cur][c].popleft()
                        s[i] = cor
                        s[index] = cur
                        cnt += 1
                        break

    # print(lst)
    # print(s)

    return cnt


if __name__ == "__main__":
    print(solve("CCAABB"))  # 4
    # print(solve("CBACBA"))  # 3
    # print(solve("AAAA"))  # 0
    # print(solve("BBCBBCCCACBBA"))  # 6
    # print(solve("CBBACBAACABAAAABBAACCCAABAABCACACBCCBCCABCCACACCBACBBAABBCACBCBACAAACBC"))  # 23
    # print(solve("ACCCCCCABACBCBBCCBBBBCBCCBCACACABCAAABBBCBBCAACCABABACBBBAACCCCBABABBBABB"))  # 28


# """
# CCAABB      561234
# ------
# ACCABB      156234
# ACBACB
# ABBACC
# AABBCC

# """

# """
# CCBBAAAABB
# ------
# ACCABB
# ACBACB
# ABBACC
# AABBCC

# """
