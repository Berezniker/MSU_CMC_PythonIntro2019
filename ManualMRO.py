def ccheck(*classes):
    from itertools import permutations

    for comb in permutations(classes):
        try:
            class Checked(*comb): pass
            return Checked
        except TypeError:
            pass

    class Checked(object): pass
    return Checked
