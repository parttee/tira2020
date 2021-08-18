class HashTable:
    def __init__(self):
        self.table = [0] * (10 ** 5)
        self.a = 7
        self.n = len(self.table)

    def add(self, s):
        h = self.hash(s)
        print(s, h)
        self.table[h] = s

    def hash(self, s):
        hashSum = 0
        n = len(s)
        for i in range(n):
            c = s[i]
            o = ord(c)
            hashSum += o * self.a ** (n - (i + 1))
        return hashSum % self.n


if __name__ == "__main__":
    ht = HashTable()
    ht.add("testi")  #
    ht.add("apina")  #
    ht.add("banaani")  #
    ht.add("cembalo")  #
