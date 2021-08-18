# from heapq import heappush, heappop


# def _heappush(heap, item):
#     heap.append(item)
#     return __siftdown(heap, 0, len(heap)-1)


# def __siftdown(heap, startpos, pos):
#     newitem = heap[pos]
#     c = 0
#     while pos > startpos:
#         parentpos = (pos - 1) >> 1
#         parent = heap[parentpos]
#         if newitem < parent:
#             heap[pos] = parent
#             c += 1
#             pos = parentpos
#             continue
#         break

#     heap[pos] = newitem
#     return c


# def _count(n):
#     c = 0
#     h = [] * n
#     for i in range(1, n + 1):
#         c += _heappush(h, -1 * i)
#     return c


def count(n):
    mx = 2
    step = 1
    c = 0
    times = 1

    while times < n:
        nextMx = mx * 2

        if nextMx <= n:
            c += mx * step
            step += 1
            times += mx
            mx = 2 * mx
        else:
            c += (n - times) * step
            break

    return c


if __name__ == "__main__":
    # for i in range(1, 101):
    #     c = _count(i)
    #     print(str(i) + " -> " + str(c), ' - ', c - i)
    print(count(2))  # 1
    print(count(3))  # 2
    print(count(4))  # 4
    # print(count(7))  # 10
    print(count(8))  # 13
    print(count(9))  # 16
    print(count(10))  # 19
    print(count(123))  # 618
    print(count(999999999))  # 27926258178

# 2 * 1, 4 * 2, 8 * 3, 16 * 4, 32 * 5, 64 * 6
# 1 -> 0
# 2 -> 1
# 3 -> 2
# 4 -> 4
# 5 -> 6
# 6 -> 8
# 7 -> 10
# 8 -> 13
# 9 -> 16
# 10 -> 19
# 11 -> 22
# 12 -> 25
# 13 -> 28
