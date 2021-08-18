from collections import deque


def solve(n, k):
    q = deque([i for i in range(1, n + 1)])

    for _ in range(k):
        fst = q.popleft()
        snd = q.popleft()
        q.append(snd)
        q.append(fst)

    return q[0]


if __name__ == "__main__":
    print(solve(4, 3))  # 4
    print(solve(12, 5))  # 11
    print(solve(99, 555))  # 11
