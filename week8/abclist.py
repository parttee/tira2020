def create(n):
    l = list("ABC")

    for i in range(1, n):
        for j in "ABC":
            l[]

    return l


if __name__ == "__main__":
    print(create(1))  # [A,B,C]
    print(create(2))  # [AA,AB,AC,BA,BB,BC,CA,CB,CC]
    print(len(create(5)))  # 243
