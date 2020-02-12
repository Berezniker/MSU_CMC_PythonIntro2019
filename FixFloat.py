def fix(n):

    def n_round(func):

        def wrapper(*args, **kwargs):
            round_args = tuple()
            for arg in args:
                if isinstance(arg, float):
                    arg = round(arg, n)
                round_args += (arg,)
            for key, arg in kwargs.items():
                if isinstance(arg, float):
                    kwargs[key] = round(arg, n)
            func_return = func(*round_args, **kwargs)
            if isinstance(func_return, float):
                func_return = round(func_return, n)
            return func_return

        return wrapper

    return n_round
