cmd = input()
env = dict()

while cmd and (cmd != '.'):
    try:
        if cmd[0] != '#':
            cc = cmd.count('=')
            if cc == 0:
                print(eval(cmd, env))
            elif cc == 1:
                ident = cmd.split('=')[0]
                if not ident.isidentifier():
                    raise SyntaxError(f"invalid identifier '{ident}'")
                env[ident] = eval(cmd.split('=')[1], env)
            else:
                raise SyntaxError(f"invalid assignment '{cmd}'")
    except Exception as e:
        print(e)
    cmd = input()
