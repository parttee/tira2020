from decimal import Decimal
# from collections import deque


def count(n):
    if n % 2 == 0:
        return n

    r = n // 2

    oddSum = int(Decimal(r / 2) * (2 * 3 + (r - 1) * 2))

    return oddSum - r


# def generate(n):
#     t = deque([i for i in range(1, n + 1)])

#     def piip(tb, c):
#         a = tb.popleft()
#         b = tb.popleft()
#         tb.append(b)
#         tb.append(a)
#         # print(tb)
#         if tb == t:
#             return c
#         else:
#             c += 1
#             return piip(tb, c)

#     return piip(t.copy(), 1)


if __name__ == "__main__":
    print(count(2))  # 2
    print(count(5))  # 6
    print(count(8))  # 6
    print(count(27))  # 182
    print(count(31))  # 240
    print(count(572589547))  # 240

    # print("--------")
    # for i in range(3, 51, 2):
    #     print(i, "\t", generate(i))
