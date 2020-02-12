def moar(a, b, n):
    return sum([1 for i in a if i % n == 0]) > \
           sum([1 for i in b if i % n == 0])
    