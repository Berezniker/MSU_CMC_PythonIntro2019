def nonify(func):

    def wrapper(*args, **kwargs):
        return_value = func(*args, **kwargs)
        return return_value if return_value else None

    return wrapper
