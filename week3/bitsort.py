def solve(s):
    n = len(s)
    c = 0
    wz = 0

    for i in range(n - 1, -1, -1):
        v = s[i]
        if v == "0":
            wz += 1
        else:
            c += wz

    return c


if __name__ == "__main__":
    print(solve("000100"))  # 2
    print(solve("111000"))  # 9
    print(solve("101010"))  # 6

# 101010
# ------
# 101001
# 011001
# 010101
# 001101
# 001011
# 000111
