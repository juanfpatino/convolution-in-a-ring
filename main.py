from Term import Term


def q3(f, g, n, customN):
    Fx = parse(f)
    Gx = parse(g)

    if not customN:
        if Fx[0].degree > Gx[0].degree:
            n = Fx[0].degree + 1
        else:
            n = Gx[0].degree + 1

    fx = fillInZeroes(Fx, n)
    gx = fillInZeroes(Gx, n)

    fx.reverse()
    gx.reverse()
    cx = []

    for i in range(0, n):  # convolution is a summation, doesn't matter if we start at i = 0
        sum = 0
        for j in range(0, n):
            for k in range(0, n):
                if (j + k) % n == i:
                    aj = fx[j]
                    bk = gx[k]
                    sum += aj.arity * bk.arity
        cx.append(Term(sum, i))

    result = ""
    firstDone = False
    for cr in range(0, len(cx)):
        c = len(cx) - cr - 1
        ci = cx[c]
        # zero case, ignore
        if firstDone:
            if ci.arity == 0:
                continue
            if ci.arity > 0:
                result = result + " + "
                result = result + str(ci)
            else:
                result = result + " - "
                result = result + str(ci).split("-")[1]
        else:  # ignore '+' sign if first term
            if ci.arity == 0:  # 0
                continue
            else:
                firstDone = True
            if ci.arity < 0:  # negative
                result = "- " + str(ci).split("-")[1]
            else: # positive (ignore sign)
                result = str(ci)
    print(result)


def fillInZeroes(Fx, n):
    fx = []
    traverseIdx = 0
    lastDegree = n
    while lastDegree > 0:
        try:
            x = Fx[traverseIdx]
        except:
            fx.append(Term(0, lastDegree - 1))
            lastDegree -= 1
            continue
        if x.degree != lastDegree - 1:
            fx.append(Term(0, lastDegree - 1))
        else:
            fx.append(x)
            traverseIdx += 1
        lastDegree -= 1
    return fx


def parse(fx):
    terms = []
    sign = 1
    for i in fx.split(" "):  # parse
        if i == "+":
            sign = 1
            continue
        elif i == "-":
            sign = -1
            continue
        if "x" not in i:  # constant
            terms.append(Term(sign * int(i), 0))
            break
        if "^" not in i:  # degree of 1
            split = i.split("x")
            arity = split[0]
            if arity == "":
                arity = "1"
            terms.append(Term(sign * int(arity), 1))
        else:
            split = i.split("x^")
            arity = split[0]
            if arity == "":
                arity = "1"
            terms.append(Term(sign * int(arity), int(split[1])))
    return terms


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    q4bProbablyWrong = False
    if q4bProbablyWrong:
        q3("13x^6 + 12x^5 + 31x^4 + 22x^3 + 8x^2 + 15x + 11", "x^3 - x^2 - 1", 37, True)

    debug = False
    if debug:
        q3("x^2 + 1", "x", 0, False)
    else:
        fromClass = input("Example from class? (y/n)")
        if fromClass == "y":
            f = "x^2 + 7x + 9"
            g = "3x^2 + 2x + 5"
        else:
            f = input("Give fx in the form shown on hw6")
            g = input("Give gx in the form shown on hw6")
        q3(f, g, 0, False)
