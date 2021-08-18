from heapq import heappush, heappop


class QuickAdd:
    def __init__(self):
        self.list = []

    def add(self, k, x):
        heappush(self.list, (x, k))

    def remove(self, k):
        s = 0

        while len(self.list) and k > 0:
            mn = heappop(self.list)
            x = mn[0]
            xk = mn[1]
            if xk == k:
                return s + xk * x
            if k < xk:
                self.add(xk - k, x)
                return s + k * x
            s += xk * x
            k -= xk
        return s


if __name__ == "__main__":
    q = QuickAdd()
    q.add(5, 3)
    print(q.remove(2))  # 6
    q.add(8, 1)
    print(q.remove(4))  # 4
    print(q.remove(7))  # 13
    q.add(10**9, 123)
    print(q.remove(10**9))  # 123000000000

    q2 = QuickAdd()
    tasks = ['add 10 10', 'remove 7', 'add 7 5', 'remove 2', 'add 2 7',
             'add 7 7', 'add 6 1', 'remove 4', 'remove 10', 'add 5 10']
    ret = []
    for t in tasks:
        parts = t.split(' ')
        cmd = getattr(q2, parts[0])
        if len(parts) == 2:
            ret.append(cmd(int(parts[1])))
        else:
            cmd(int(parts[1]), int(parts[2]))

    print(ret)  # [70, 10, 4, 48]
    print("vs. correct [70, 10, 4, 48]")
