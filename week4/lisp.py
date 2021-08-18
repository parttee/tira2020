def eval(s):
    # print('eval\t', s)
    fst = s[0]
    n = len(s)

    if fst == '(':
        blc = 0
        brc = 0
        ix = 0
        c = 0
        sx = 1

        while (ix < n):
            if s[ix] == '(':
                blc += 1
            elif s[ix] == ')':
                brc += 1

            # print(blc, brc, ix)
            if brc == blc and blc != 0 and brc != 0:
                # print("Täs\t",
                #       "%" + s[sx: ix] + "%", '\t', "##" + s + "##")
                c += eval(s[sx: ix])
                brc = 0
                blc = 0
                sx = ix + 3

            ix += 1

        return c

    if fst == '+' or fst == '*':
        ix = 1
        nxt = s[ix]
        args = []
        prev = fst

        while nxt != ')' and ix < n:
            if nxt.isnumeric():
                if prev == ' ' or len(args) == 0:
                    args.append(nxt)
                else:
                    args[-1] += nxt
            elif nxt == '(':
                # lstIx = n - 1
                # while s[lstIx] != ')':
                #     lstIx -= 1
                g = getGroup(s[ix:])
                if g != None:
                    args.append(eval(s[ix + g[0]: ix + g[1]]))
                ix += g[1]
                # ix = lstIx
            prev = nxt
            if(ix == n-1):
                break
            ix += 1
            nxt = s[ix]

        # print("args\t", fst, args)

        if fst == '*':
            r = int(args[0])
            for i in range(1, len(args)):
                r *= int(args[i])
            return r
        else:
            r = 0
            for v in args:
                r += int(v)

            return r


def getGroup(s):
    n = len(s)
    blc = 0
    brc = 0
    ix = 0
    sx = 1

    while (ix < n):
        if s[ix] == '(':
            blc += 1
        elif s[ix] == ')':
            brc += 1

        # print(blc, brc, ix)
        if brc == blc and blc != 0 and brc != 0:
            return (sx, ix)

        ix += 1

    return None


if __name__ == "__main__":
    print(eval("(+ 1 2 3 4 5)"))  # 15
    print(eval("(+ 1 (+ 2 3) 4 5)"))  # 15
    print(eval("(+ 5 (* 3 2) 7)"))  # 18
    print(eval("(* (+ (+ 1 2) 3) (+ (* 4 5) 6 2))"))  # 168
