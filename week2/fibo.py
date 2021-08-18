import time
import sys

start_time = time.time()

c = 0


def fibo(n):
    global c
    c += 1
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)


if __name__ == "__main__":
    print(fibo(int(sys.argv[1])), "#", c)

print("--- %s seconds ---" % (time.time() - start_time))
