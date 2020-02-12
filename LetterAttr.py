class LetterAttr:
    name_dict = dict()

    def __getattr__(self, name):
        if name not in self.name_dict:
            self.name_dict[name] = name
        return self.name_dict[name]

    def __setattr__(self, name, new_name):
        if name in self.name_dict:
            self.name_dict[name] = ''.join(c for c in new_name if c in set(self.name_dict[name]))
        else:
            self.name_dict[name] = ''.join(c for c in new_name if c in set(name))
