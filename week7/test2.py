

def f(n):
    r = 1
    for i in range(1, n + 1):
        r *= i
    return r


def ncr(n, k):
    # n!/(k! * (n-k)!)
    return f(n) // (f(k) * f(n - k))


def sizeLeft(n, powers):
    # print("n", n, powers)
    p = powers[n]
    mx = 2 ** p
    print("n, p, mx", n, p, mx)
    half = mx // 2
    lst = n - (mx - 1)

    if (lst >= half):
        return mx - 1
    else:
        return mx - 1 - (half - lst)


def countHeap(n, powers):
    if (n <= 1):
        return 1

    size = sizeLeft(n, powers)
    print("left", n, size)
    nk = ncr(n - 1, size)
    c = countHeap(size, powers)

    # print("l c nk", size, c, nk)

    return nk * c * countHeap(n - 1 - size, powers)


def count(n):
    powers = {}
    left = {}
    x = 0
    levelSize = 1
    maxLevel = 0
    allSize = 1

    while x <= n:
        if x > allSize:
            levelSize *= 2
            maxLevel += 1
            allSize += levelSize
        powers[x] = maxLevel
        x += 1

    for i in range(n + 1):
        left[i] = sizeLeft(i, powers)

    print("left", left, powers)

    return countHeap(n, powers)


if __name__ == "__main__":
    # print(count(2))  # 1
    # print(count(3))  # 2
    # print(count(4))  # 3
    # print(count(5))  # 8
    print(count(8))  # 8
    # print(count(10))  # 3360
    # print(count(25))  #
