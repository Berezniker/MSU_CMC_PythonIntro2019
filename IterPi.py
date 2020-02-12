from itertools import count, cycle

def pigen():
    pi = 0
    for n, sign in zip(count(start=1, step=2), cycle([1, -1])):
        pi += 4 * sign / n
        yield pi
