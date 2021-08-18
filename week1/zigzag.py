def create(n):
    res = []
    for i in range(1, n + 1):
        if ((i % 2) == 0):
            res.append(i)
        else:
            res.insert(0, i)
    return res


if __name__ == "__main__":
    print(create(1))  # [1]
    print(create(2))  # [1,2]
    print(create(3))  # [3,1,2]
    print(create(4))  # [3,1,2,4]
    print(create(5))  # [5,3,1,2,4]
