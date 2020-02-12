class DivStr(str):
    protected = ['__class__', '__new__', '__getattribute__',
                 '__getattr__', '__repr__', '__str__' ]
    for name, obj in str.__dict__.items():
        if callable(obj) and name not in protected:
            cmd = f'def {name}(self, *args):\n'\
                  f'    ret = str.{name}(self, *args)\n'\
                  f'    return DivStr(ret) if isinstance(ret, str) else ret'
            exec(cmd)

    def __truediv__(self, val):
        return DivStr(self[:len(self) // val])
