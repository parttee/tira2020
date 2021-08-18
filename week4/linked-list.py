import time
import sys


class LinkedList:
    def __init__(self, n):
        self.start = None
        self.end = None

    def add(self, x):
        n = Node(x)
        if self.start == None:
            self.start = n
        if self.end != None:
            self.end.next = n
        self.end = n

    def popFirst(self):
        if self.start == None:
            return
        if self.start.next == None:
            self.start = None
            self.end = None
        else:
            self.start = self.start.next


class Node:
    def __init__(self, x):
        self.next = None
        self.value = x


def testLst(lst):
    if lst.start == None:
        return []

    nd = lst.start
    l = [nd.value]

    while nd.next != None:
        l.append(nd.next.value)
        nd = nd.next

    return l


if __name__ == "__main__":
    n = 10 ** 5

    start_time = time.time()

    l = LinkedList(n)
    for i in range(1, n + 1):
        l.add(i)

    print("--- %s seconds ---" % (time.time() - start_time))
    # print(len(testLst(l)))

    start_time = time.time()

    for i in range(1, n + 1):
        l.popFirst()
        # print(l.start.value if l.start != None else None)

    print("--- %s seconds ---" % (time.time() - start_time))
    # print(len(testLst(l)))
