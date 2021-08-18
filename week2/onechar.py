
def substrCount(s):
    size = len(s)

    cnt = 0

    for i in range(size):
        cnt += len(s[0: i + 1])

    return cnt


def count(s):
    size = min(len(s), 100000)

    cnt = 0

    subset = ""
    prev = s[0]

    for i in range(size):
        if(prev == s[i]):
            subset += s[i]
        else:
            cnt += substrCount(subset)
            subset = s[i]
        if(i == size - 1):
            cnt += substrCount(subset)
        prev = s[i]

    return cnt


if __name__ == "__main__":
    print(count("aaa"))  # 6
    print(count("abbbcaa"))  # 11
    print(count("abcde"))  # 5
