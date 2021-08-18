

def count(s):
    subsets = {}

    size = len(s)

    for i in range(size):
        for i2 in range(i + 1, size + 1):
            subsets[s[i: i2]] = 1

    # print(subsets)

    return len(subsets)


if __name__ == "__main__":
    print(count("aaa"))  # 3
    print(count("abc"))  # 6
    print(count("saippuakauppias"))  # 110
