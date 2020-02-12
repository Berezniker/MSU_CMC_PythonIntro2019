def checkhash(seq, foo, mod):
    val = {}
    for i in seq:
        key = foo(i) % mod
        val.setdefault(foo(i) % mod, 0)
        val[key] += 1
    l = list(val.values())
    return (max(l), min(l))
