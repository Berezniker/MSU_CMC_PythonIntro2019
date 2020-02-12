from math import log

eps = 1e-8
num = int(input())

# num = n ^ p => p = log(num) / log(n)
#             => p = 1 / log_num_(n)

for n in range(2, num):
    power = 1 / log(n, num)
    if power - int(power) < eps:
        print('YES')
        break
else:
    print('NO')
