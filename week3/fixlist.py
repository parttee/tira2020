def changes(t):
    n = len(t)

    changes = 0

    for i in range(1, n):
        prev = t[i - 1]
        v = t[i]
        d = max(prev - v, 0)
        if v < prev:
            changes += d
        prev = v + d
        t[i] = prev

    return changes


if __name__ == "__main__":
    print(changes([3, 2, 5, 1, 7]))  # 5
    print(changes([1, 2, 3, 4, 5]))  # 0
    print(changes([3, 3, 1, 4, 2]))  # 4
    print(changes([7, 1, 2, 5, 3, 6, 3]))  # 22
