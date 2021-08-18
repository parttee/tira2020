from collections import deque


class FlipList:
    def __init__(self):
        self.q = deque([])
        self.q2 = deque([])
        self.cur = 'q'
        self.cur2 = 'q2'

    def push_last(self, x):
        q = getattr(self, self.cur)
        q2 = getattr(self, self.cur2)
        q.append(x)
        q2.appendleft(x)

    def push_first(self, x):
        q = getattr(self, self.cur)
        q2 = getattr(self, self.cur2)
        q.appendleft(x)
        q2.append(x)

    def pop_last(self):
        q = getattr(self, self.cur)
        q2 = getattr(self, self.cur2)
        v = q.pop()
        q2.popleft()
        return v

    def pop_first(self):
        q = getattr(self, self.cur)
        q2 = getattr(self, self.cur2)
        v = q.popleft()
        q2.pop()
        return v

    def flip(self):
        oc = self.cur
        self.cur = self.cur2
        self.cur2 = oc


if __name__ == "__main__":
    f = FlipList()
    f.push_last(1)
    f.push_last(2)
    f.push_last(3)
    print(f.pop_first())  # 1
    f.flip()
    print(f.pop_first())  # 3

    # f = FlipList()
    # f.push_first(3)
    # f.push_last(4)
    # f.push_first(5)
    # print(f.pop_last())
    # print(f.pop_last())  # 3
