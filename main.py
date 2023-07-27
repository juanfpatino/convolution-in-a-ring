import os
import platform
import random

from Term import Term

# todo docstrings and commenting for public github repo

def q3(f, g):
    if f == "ignore":
        return

    Fx = parse(f)
    Gx = parse(g)

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
            else:  # positive (ignore sign)
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


def randomPoly():
    # term array representing the polynomial
    y = []
    # degree of this polynomial
    degree = random.randint(1, 99)
    # 0th term, generate 75% of the time
    if random.randint(0, 4) > 0:
        y.append(Term(random.randint(-9999, 9999), 0))

    # create an array of terms up to the degree
    for i in range(1, degree):
        if random.randint(0, 4) > 1:
            y.append(Term(random.randint(-9999, 9999), i))

    if len(y) == 0:
        return randomPoly()  # recursively ensure length is not zero

    y.reverse()
    return y


def unParse(fArr, gArr):
    return [unparseIndividual(str(fArr[0]), fArr), unparseIndividual(str(gArr[0]), gArr)]


def unparseIndividual(f, fArr):
    i = 0
    for t in fArr:
        if i == 0:
            i = 1
            continue
        if str(t) == "0":
            continue
        op = " + "
        if t.arity < 0:
            op = " "
        f = f + op + str(t)

        i = i + 1
    return f


def printDebugPretty(size):
    line = ""
    for i in range(size):
        line = line + "-"
    print(line)


def loop(ii, clear):
    for i in range(int(ii)):
        funcs = unParse(randomPoly(), randomPoly())
        printDebugPretty(22)
        print("Convolution of\nf =", funcs[0], "\ng =", funcs[1], "\n\n")
        q3(funcs[0], funcs[1])
        printDebugPretty(22)
        if clear:
            cmd = 'clear'  # mac/linux
            if platform.system() == "Windows":
                cmd = 'cls'
            os.system(cmd)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    debug = False
    if debug:
        q3("x^2 + 1", "x")
    else:
        fromClass = input("Example from class? (y/n)")
        if fromClass == "y":
            f = "x^2 + 7x + 9"
            g = "3x^2 + 2x + 5"
        else:
            randomGen = input("Random generator loop? (y/n)")
            if randomGen == "y":
                i = input("How many iterations")
                clear = input("clear screen after each? (y/n)")
                if clear == "y":
                    loop(i, True)
                else:
                    loop(i, False)
                f = "ignore"
                g = ""
            else:
                f = input("Give fx in the form shown on hw6")
                g = input("Give gx in the form shown on hw6")
        q3(f, g)
