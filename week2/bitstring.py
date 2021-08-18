def opposite(c):
    if c == "1":
        return "0"
    else:
        return "1"


def changes(s, i):
    change = {}

    prev = i

    if(i != s[0]):
        change[0] = i

    for n in range(1, len(s)):
        c = s[n]
        if c == prev:
            change[n] = opposite(c)
            prev = change[n]
        else:
            prev = c

    return change


def calculate(s):
    if s == "":
        return 0

    return min(len(changes(s, "1")), len(changes(s, "0")))


if __name__ == "__main__":
    print(calculate("1010"))  # 0
    print(calculate("1111"))  # 2
    print(calculate("10010001"))  # 3
