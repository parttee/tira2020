def getKey(item):
    return item[1]


def get(t):
    n = len(t)

    arr = [(i, t[i]) for i in range(n)]

    arr = sorted(arr, key=getKey)

    return [i[0] for i in arr]


if __name__ == "__main__":
    print(get([1, 2, 4, 3]))  # [0,1,3,2]
    print(get([4, 2, 1, 3]))  # [2,1,3,0]
    print(get([6, 2, 8, 5, 3]))  # [1,4,3,0,2]
