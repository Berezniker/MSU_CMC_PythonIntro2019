from math import *

function = input()
left_border, right_border = eval(input())

eps = 1e-6
x = right_border
f_right = eval(function)

while abs(left_border - right_border) > eps:
    x = (left_border + right_border) / 2
    f_mid = eval(function)
    if f_mid == 0:
        break
    elif (f_right * f_mid < 0):
        left_border = x
    else:
        right_border = x
        f_right = f_mid

print((left_border + right_border) / 2)
