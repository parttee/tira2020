from collections import deque


def count(t, k):
    n = len(t)

    s = {}
    q = deque(t[: k])
    uq = 0
    for v in q:
        if not v in s:
            s[v] = 0
            uq += 1
        s[v] += 1

    b = [uq]

    for i in range(k, n):
        v = t[i]
        f = q.popleft()
        q.append(v)
        s[f] -= 1
        if s[f] == 0:
            del s[f]
        if not v in s:
            s[v] = 0
        s[v] += 1
        b.append(len(s))

    return b


if __name__ == "__main__":
    print(count([1, 1, 2, 2], 2))  # [1,2,1]
    # print(count([1, 1, 1, 1], 4))  # [1]
    print(count([1, 2, 3, 2, 2, 2], 3))  # [3,2,2,1]
    # print(count([1, 2, 3, 2, 2, 2, 4, 5, 7, 7]*(10 ** 4), 1000))
