import math
from decimal import Decimal


def count(n):
    if n < 6:
        return 0
    if n == 6:
        return 1

    m = n % 6
    c = 0

    if m == 0:
        m = 6
        c = 1

    r = math.ceil((n - 6) / 6)

    return int(Decimal(r / 2) * (2 * m + (r - 1) * 6) + c)


def count2(n):
    x = []

    for a in range(1, n + 1):
        for b in range(1, n + 1):
            for c in range(1, n + 1):
                v = sorted([a, b, c])
                if a + b + c == n and b != a and c != b and c != a and not v in x:
                    x.append(v)

    # print(x)

    return len(x)


if __name__ == "__main__":
    print(count(8))
    print(count(10))
    print(count(13))
    print(count(30))  # 61
    print(count(1337))  # 148296
    print(count(993786079))  # 82300897070956481
