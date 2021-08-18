import time
start_time = time.time()

n = 1000
count = 0
for i in range(2, n + 1):
    prime = True
    for j in range(2, i - 1):
        if i % j == 0:
            prime = False
            break
    if(prime):
        count += 1

print(count)

print("--- %s seconds ---" % (time.time() - start_time))
