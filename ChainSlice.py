from itertools import chain, islice

def chainslice(start, stop, *sequence):
    yield from islice(chain(*sequence), start, stop)
