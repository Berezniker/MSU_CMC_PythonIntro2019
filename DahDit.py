class morse:
    buf = ""
    dot = 'di'
    e_dot = 'dit'
    dash = 'dah'
    sep1 = ' '
    sep2 = ','
    end = '.'

    def __init__(self, cmd=''):
        if cmd:
            if ' ' in cmd:
                cs = cmd.split()
            else:
                cs = list(cmd)
                self.sep1 = ''
                self.sep2 = ' '
                self.end = ''
            self.dot = self.e_dot = cs[0]
            if len(cs) == 2:
                self.dash = cs[1]
            else:
                self.e_dot = cs[1]
                self.dash = cs[2]
                if len(cs) == 4:
                    self.end = cs[3]
                elif cmd[-1] == ' ':
                    self.end = ''


    def __str__(self):
        if not self.buf:
            return self.end
        if self.buf[-1] == '+': 
            self.buf = self.buf[:-1] + self.e_dot
        if self.buf[-1] == '-':
            self.buf = self.buf[:-1] + self.dash
        self.buf = self.buf.replace('+~', self.e_dot + self.sep2 + self.sep1)
        self.buf = self.buf.replace('-~', self.dash + self.sep2 + self.sep1)
        self.buf = self.buf.replace('+', self.dot + self.sep1)
        self.buf = self.buf.replace('-', self.dash + self.sep1)
        return self.buf + self.end

    def __invert__(self):
        self.buf = '~' + self.buf
        return self

    def __pos__(self):
        self.buf = '+' + self.buf
        return self

    def __neg__(self):
        self.buf = '-' + self.buf
        return self
