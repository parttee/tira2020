import sys


def count(t):
    t = sorted(t)
    n = len(t)

    if n <= 1:
        return n

    vals = []
    cur = [t[0]]

    for i in range(1, n):
        v = t[i]
        if v - cur[-1] == 1:
            cur.append(v)
        else:
            vals.append(cur)
            cur = [v]
        if(i == n - 1):
            vals.append(cur)

    return len(vals)


if __name__ == "__main__":
    print(count([4, 1, 5, 3]))  # 2
    print(count([4, 2, 1, 3]))  # 1
    print(count([5, 2, 7, 6, 3, 9]))  # 3
