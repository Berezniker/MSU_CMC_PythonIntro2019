def BinPow(a, n, foo):
    if n == 1:
        return a
    elif n % 2 == 1:
        return foo(a, BinPow(a, n - 1, foo))
    else:
        b = BinPow(a, n / 2, foo)
        return foo(b, b)
