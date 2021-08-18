import time
import sys
from collections import deque


def testPop(item, n):
    for i in range(1, n + 1):
        item.append(i)
    while len(item):
        item.pop()


def testPopFirst(item, n):
    for i in range(1, n + 1):
        item.append(i)
    while len(item):
        item.pop(0)


def testPopLeft(item, n):
    for i in range(1, n + 1):
        item.append(i)
    while len(item):
        item.popleft()


if __name__ == "__main__":
    n = 10 ** 5
    print("List")
    start_time = time.time()
    testPop([], n)
    print("--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    testPopFirst([], n)
    print("--- %s seconds ---" % (time.time() - start_time))
    print("Deque")
    start_time = time.time()
    testPop(deque([]), n)
    print("--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    testPopLeft(deque([]), n)
    print("--- %s seconds ---" % (time.time() - start_time))
