from fractions import Fraction
from math import ceil

class sausage:
    size = Fraction(12)

    def __init__(self, farce='pork!', piece=1):
        self.farce = farce
        self.size *= Fraction(piece)
        
    def __str__(self):
        if self.size < 1:
            return '/|\n||\n||\n||\n\\|'
        n = ceil(12 / len(self.farce))
        len_sausage = ceil(int(self.size) / 12)
        su = f"/{'-'*12}\\" * len_sausage
        sm = ('|' + f"{self.farce * n}"[:12] + '|') * len_sausage
        sd = f"\\{'-'*12}/" * len_sausage
        if int(self.size) % 12 != 0:
            n_slice = 12 - int(self.size) % 12 + 1
            su = su[:-n_slice] + '|'
            sm = sm[:-n_slice] + '|'
            sd = sd[:-n_slice] + '|'
        sm = f'{sm}\n' * 3

        return f"{su}\n{sm}{sd}"

    def __mul__(self, val):
        return sausage(self.farce, (self.size * Fraction(val)) / 12)

    def __rmul__(self, val):
        return sausage(self.farce, (self.size * Fraction(val)) / 12)

    def __truediv__(self, val):
        return sausage(self.farce, (self.size / Fraction(val)) / 12)

    def __add__(self, other_sausage):
        return sausage(self.farce, (self.size + other_sausage.size) / 12)

    def __sub__(self, other_sausage):
        return sausage(self.farce, (self.size - other_sausage.size) / 12)
    
    def __bool__(self):
        return self.size > 0
