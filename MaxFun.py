from math import *

def maxfun(sequence, *functions):
    return functions[max([(n, sum([foo(i) for i in sequence]))
                          for n, foo in enumerate(functions)][::-1],
                         key=lambda x: x[1])[0]]
