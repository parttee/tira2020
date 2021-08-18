import time
import sys

start_time = time.time()


def sort(taulu):
    n = len(taulu)
    for i in range(1, n-1):
        j = i-1
        while j >= 0 and taulu[j] > taulu[j+1]:
            # swap(taulu[j], taulu[j+1])
            tmp = taulu[j]
            taulu[j] = taulu[j+1]
            taulu[j+1] = tmp
            j -= 1

    return taulu


if __name__ == "__main__":
    sort([2, 3, 4, 6, 3, 4, 5, 2, 8, 9] * 100)
    print("--- %s seconds ---" % (time.time() - start_time))
    sort([2, 3, 4, 6, 3, 4, 5, 2, 8, 9] * 1000)
    print("--- %s seconds ---" % (time.time() - start_time))
    sort([2, 3, 4, 6, 3, 4, 5, 2, 8, 9] * 10000)
    print("--- %s seconds ---" % (time.time() - start_time))
