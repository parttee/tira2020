import sys


def f(n):
    r = 1
    for i in range(1, n + 1):
        r *= i
    return r


def ncr(n, k):
    # n!/(k! * (n-k)!)
    return f(n) // (f(k) * f(n - k))


if __name__ == "__main__":
    print(ncr(int(sys.argv[1]), int(sys.argv[2])))
