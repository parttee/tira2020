from heapq import heappush, heappop
# from randomlist import randomList


def find(t, k):
    t = sorted(t)
    n = len(t)

    dist = []

    for i in range(n - 1):
        heappush(dist, (t[i + 1] - t[i], i, 1))

    r = -1
    x = 0

    while x < k:
        item = heappop(dist)
        r = item[0]
        i = item[1]
        a = item[2] + 1
        if i + a < n:
            heappush(dist, (t[i + a] - t[i], i, a))
        x += 1

    return r


if __name__ == "__main__":
    t = [4, 1, 5, 2]
    print(find(t, 1))  # 1
    print(find(t, 2))  # 1
    print(find(t, 3))  # 2
    print(find(t, 4))  # 3
    print(find(t, 5))  # 3
    print(find(t, 6))  # 4
    print(find([1, 2, 5, 4, 11, 8, 9, 10], 6))  # 4

    # print(find(randomList, 600))

    # b = [147487986, 69772727, 45401717, 725761082, 291387352, 639529965, 637522586, 326914237, 198591016, 498273805, 670256298, 90413566, 150362709, 8000355, 852676066, 999166228, 348192346, 404495799, 687391899, 931891536, 424307133, 203161169, 106998233, 954414389,
    #      58719652, 372263790, 700796532, 737548980, 853963507, 227559398, 101797622, 703717376, 222931026, 943412794, 122203888, 225996105, 855506214, 805112952, 722106493, 119880200, 682568074, 612074522, 957285709, 603378442, 719923806, 176933049, 346104798]
    # print(find(randomList, 22))
