def getKey(x):
    return str(x[0]) + "," + str(x[1])


def count(s):
    stepMap = {}
    xy = (0, 0)

    stepMap[getKey(xy)] = 1

    for c in s:
        if c == "L":
            xy = (xy[0] - 1, xy[1])
        elif c == "R":
            xy = (xy[0] + 1, xy[1])
        elif c == "U":
            xy = (xy[0], xy[1] - 1)
        elif c == "D":
            xy = (xy[0], xy[1] + 1)

        h = getKey(xy)

        if h not in stepMap:
            stepMap[h] = 0
        stepMap[h] += 1

    return len(stepMap)


print(count("LL"))  # 3
print(count("UUDLRR"))  # 5
print(count("UDUDUDU"))  # 2
