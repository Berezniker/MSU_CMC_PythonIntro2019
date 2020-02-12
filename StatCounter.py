def statcounter():
    stat = {}
    func = yield stat
    while True:
        def counter(func):
            def wrapper(*args, **kwargs):
                stat[func] = stat.setdefault(func, 0) + 1
                return func(*args, **kwargs)
            return wrapper
        func = yield counter(func)
