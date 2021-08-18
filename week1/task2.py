import time
start_time = time.time()

n = 1000
rangeN = n + 1
count = 0

a = [0] * rangeN

for i in range(2, rangeN):
    if a[i] == 0:
        count += 1
        for j in range(2*i, rangeN, i):
            a[j] = 1

print(count)

print("--- %s seconds ---" % (time.time() - start_time))
