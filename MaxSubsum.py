max_sum = num = int(input())
cur_sum = 0
while num != 0:
    if max_sum < 0 and num < 0:
        # случай, когда все числа последоваельности отрицательные
        max_sum = max(num, max_sum)
    else:
        cur_sum = max(cur_sum + num, 0)
        max_sum = max(max_sum, cur_sum)
    num = int(input())

print(max_sum)
