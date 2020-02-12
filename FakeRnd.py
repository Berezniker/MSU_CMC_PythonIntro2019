n_calls_randint = 1

def randint(a, b):
    global n_calls_randint
    n_calls_randint = (n_calls_randint + 1) % 2
    return b if n_calls_randint % 2 else a


prev_randrange_args = []
offset = None

def randrange(a, b=None, d=1, ignore=None):
    global prev_randrange_args, offset
    if b is None:
        a, b = 0, a
    if [a, b, d] != prev_randrange_args:
        prev_randrange_args = [a, b, d]
        offset = 0
    else:
        offset = (offset + d) % (b - a)
    return a + offset
