def gcdRecur(a, b):
    if b == 0:
        return a
    else:
        return gcdRecur(b, a%b)

print(gcdRecur(6, 12))