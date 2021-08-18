import time
import sys

start_time = time.time()

apu = []
taulu = []


def sort(t):
    global apu, taulu
    taulu = t
    n = len(taulu)
    apu = [0] * n
    jarjesta(0, n - 1)
    return taulu


def jarjesta(a, b):
    if a == b:
        return
    k = (a+b) // 2
    jarjesta(a, k)
    jarjesta(k+1, b)
    lomita(a, k, k+1, b)


def lomita(a1, b1, a2, b2):
    a = a1
    b = b2
    for i in range(a, b + 1):
        if a2 > b2 or (a1 <= b1 and taulu[a1] <= taulu[a2]):
            apu[i] = taulu[a1]
            a1 += 1
        else:
            apu[i] = taulu[a2]
            a2 += 1
    for i in range(a, b + 1):
        taulu[i] = apu[i]


if __name__ == "__main__":
    # print(sort([2, 32, 4, 64, 3, 74, 5, 12, 8, 19]))
    # print(sort([5, 1, 2, 9, 7, 5, 4, 2]))
    # print("--- %s seconds ---" % (time.time() - start_time))
    sort([2, 3, 4, 6, 3, 4, 5, 2, 8, 9] * 100)
    print("--- %s seconds ---" % (time.time() - start_time))
    sort([2, 3, 4, 6, 3, 4, 5, 2, 8, 9] * 1000)
    print("--- %s seconds ---" % (time.time() - start_time))
    sort([2, 3, 4, 6, 3, 4, 5, 2, 8, 9] * 10000)
    print("--- %s seconds ---" % (time.time() - start_time))
