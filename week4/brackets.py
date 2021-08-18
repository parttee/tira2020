from collections import deque


def count(s):
    q = deque()

    i = 0
    for c in s:
        if len(q) == 0 or q[-1] == ')' or c == '(':
            q.append(c)
        elif q[-1] == '(' and c == ')':
            q.pop()
        i += 1

    return len(q)


if __name__ == "__main__":
    print(count("(()())"))  # 0
    print(count("))))))"))  # 6
    print(count("((())("))  # 2
    print(count("(()()"))  # 1
    print(count(")("))  # 2
    print(count(")()()"))  # 1
    print(count(")()()("))  # 2
    print(count("()" * 1000))  # 0
    print(count("((" * 1000 + "))" * 1000))  # 0
