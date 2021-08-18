
def count(s):
    n = len(s)
    cnt = 0

    lastSeen = {}
    allowed = []
    subset = ""
    subsets = []

    counter = 0

    for i in range(n):
        v = s[i]
        lastSeen[v] = i
        has = v in allowed
        bothSet = len(allowed) == 2

        if not has and not bothSet:
            allowed.append(v)
            has = True
        if has:
            subset += v
        else:
            prev = s[i - 1]
            pos = 0

            if prev == allowed[0]:
                pos = lastSeen[allowed[1]]
            elif prev == allowed[1]:
                pos = lastSeen[allowed[0]]

            subsets.append(subset)
            subset = s[pos + 1: i + 1]

            allowed = [prev, v]
            # print("alw", allowed, subset, v, allowed)

            if(i == n - 1):
                subsets.append(subset)

            counter = 0

        if has and bothSet and i == n - 1:
            subsets.append(subset)

        if i > 0:
            prev = s[i - 1]
            if prev != v:
                counter = len(subset) - 1

        cnt += counter
    print(subsets)

    return cnt


if __name__ == "__main__":
    # print(count("aaaa"))  # 0
    print(count("abab"))  # 6
    print(count("aabacba"))  # 8
    print(count("ababcba"))  # 8
    print(count("babbbabbba"))  # 39
    # print(count2("babbbabbba"))  # 39
    # print(count("yahsqqozlfropz"))  # 14
    # print(count("aaabaabaaabbbaaabababbaaaabbaabaaabaabbaaaabaabaaabbbaaabababbaaaabbaabaaabaabbabababbaaaabbaabaaaba" * 500))  # 8
