from heapq import heappush, heappop


def smallest(n):
    q = [1]
    for _ in range(n):
        x = heappop(q)
        heappush(q, x * 2)
        heappush(q, x * 3)

    return q[0]


if __name__ == "__main__":
    print(smallest(1))  # 2
    print(smallest(5))  # 6
    print(smallest(123))  # 288
    print(smallest(55555))  # 663552
