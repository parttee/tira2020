import sys


def count(t):
    mx = 0
    mn = sys.maxsize

    n = len(t)

    maxSteps = [0] * n
    minSteps = [0] * n

    for i in range(n - 1, -1, -1):
        v = t[i]
        if v < mn:
            mn = v
        minSteps[i] = mn

    for i in range(n):
        v = t[i]
        if v > mx:
            mx = v
        maxSteps[i] = mx

    cnt = 0

    for i in range(1, n):
        v = t[i]
        if maxSteps[i - 1] < minSteps[i]:
            cnt += 1

    return cnt


# Esimerkiksi listassa [2,1,2,5,7,6,9] tapoja on 3:
# [2,1,2] ja [5,7,6,9]
# [2,1,2,5] ja [7,6,9]
# [2,1,2,5,7,6] ja [9]

if __name__ == "__main__":
    print(count([5, 6, 6, 7, 8, 10, 3]))  # 0
    print(count([2, 1, 2, 6, 3, 4, 9, 12]))  # 3
    print(count([1, 2, 3, 4, 5]))  # 4
    print(count([2, 2, 2, 2]))  # 0
    print(count([2, 2, 4, 9, 6]))  # 2
    print(count([5, 4, 3, 2, 1]))  # 0
    print(count([2, 1, 2, 5, 7, 6, 9]))  # 3
    print(count([1, 499999999, 500000000, 500000000, 1000000000]))  # 3
