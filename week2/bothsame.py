def count(s):
    size = len(s)
    cnt = 0

    d = {}

    for i in "abcdefghijklmnopqrstuvwxyz":
        d[i] = 0

    for i in range(size):
        d[s[i]] += 1

    for i in d:
        cnt += int((d[i] / 2) * (1 + d[i]))

    return cnt


if __name__ == "__main__":
    print(count("aaa"))  # 6
    print(count("abcd"))  # 4
    print(count("ababca"))  # 10
