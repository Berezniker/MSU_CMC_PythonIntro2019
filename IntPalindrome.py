temp = num = int(input())

if num % 10 == 0 and num != 0:
    print('NO')
else:
    num_reverse = 0

    while temp != 0:
        num_reverse = num_reverse * 10 + temp % 10
        temp //= 10

    if num == num_reverse:
        print('YES')
    else:
        print('NO')
