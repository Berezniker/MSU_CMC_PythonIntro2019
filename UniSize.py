def sizer(clas):
    def wrapper(*args, **kwargs):

        class NonDataDescriptor:
            def __get__(self, obj, clas):
                if hasattr(obj, '__len__'):
                    return len(obj)
                else:
                    return abs(int(obj))

        clas.size = NonDataDescriptor()
        return clas(*args, **kwargs)
    return wrapper
