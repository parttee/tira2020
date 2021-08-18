def check(n):
    numbers = [int(d) for d in str(n)]
    return sum(numbers) % 7 == 0


if __name__ == "__main__":
    print(check(14))  # False
    print(check(16))  # True
    print(check(123))  # False
    print(check(777))  # True
    print(check(9999999))  # True
