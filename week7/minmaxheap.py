from heapq import heappush, heappop


def minheap(n):
    q = []
    for i in range(1, n + 1):
        heappush(q, i)

    return q


def maxheap(n):
    q = []
    for i in range(1, n + 1):
        heappush(q, -1 * i)

    return q


if __name__ == "__main__":
    m = minheap(10)
    print(m)
    heappop(m)
    heappop(m)
    heappop(m)
    print(m)

    mx = maxheap(10)
    print(mx)
    heappop(mx)
    heappop(mx)
    heappop(mx)
    print(mx)
