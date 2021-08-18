

def f(n):
    r = 1
    for i in range(1, n + 1):
        r *= i
    return r


def ncr(n, k):
    # n!/(k! * (n-k)!)
    return f(n) // (f(k) * f(n - k))


def countHeap(n, left):
    if (n <= 1):
        return 1

    l = left[n]
    # print("left", n, l)
    c = countHeap(l, left)
    nk = ncr(n - 1, l)

    # print("l c nk", l, c, nk)

    return c * nk * countHeap(n - 1 - l, left)


def count(n):
    left = {}
    levelSize = 1
    maxLevel = 0
    allSize = 1

    for x in range(n + 1):
        if x > allSize:
            levelSize *= 2
            maxLevel += 1
            allSize += levelSize

        half = levelSize // 2
        last = x - (levelSize - 1)

        if (last < half):
            left[x] = levelSize - 1 - (half - last)
        else:
            left[x] = levelSize - 1

    return countHeap(n, left)


if __name__ == "__main__":
    print(count(2))  # 1
    print(count(3))  # 2
    print(count(4))  # 3
    print(count(5))  # 8
    print(count(8))  # 210
    print(count(10))  # 3360
    print(count(25))  # 25732281217843200
