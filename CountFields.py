def fcounter(obj, *args):
    cm, cf, om, of = [], [], [], []
    for m in dir(obj):
        if m[0] != '_':
            (cm if callable(getattr(obj, m)) else cf).append(m)

    ex = obj(*args)
    for m in dir(ex):
        if m[0] != '_':
            if callable(getattr(ex, m)):
                if m not in cm:
                    om.append(m)
            elif m not in cf:
                of.append(m)

    cm, cf, om, of = (sorted(l) for l in [cm, cf, om, of])
    return cm, cf, om, of
