import string
import random

if __name__ == "__main__":
    n = 10 ** 6

    hashes = {}

    for i in range(n):
        s = ''.join(random.choices(
            string.ascii_lowercase, k=20))
        h = hash(s)
        if h not in hashes:
            hashes[h] = 0
        hashes[h] += 1

    print("length", len(hashes))

    if(len(hashes) < n):
        for v in hashes:
            if hashes[v] != 1:
                print(hashes[v], v)
