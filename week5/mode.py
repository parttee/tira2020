class Mode:
    def __init__(self):
        self.nums = {0: 0}
        self.mode = 0

    def add(self, x):
        if self.nums.get(x) is None:
            self.nums[x] = 0
        self.nums[x] += 1
        if (self.nums[x] > self.nums[self.mode]) or (self.nums[x] == self.nums[self.mode] and x < self.mode):
            self.mode = x
        return self.mode


if __name__ == "__main__":
    m = Mode()
    print(m.add(1))  # 1
    print(m.add(2))  # 1
    print(m.add(2))  # 2
    print(m.add(1))  # 1
    print(m.add(3))  # 1
    print(m.add(3))  # 1
    print(m.add(3))  # 3
