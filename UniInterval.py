intervals = [ *eval(input()) ]
n = len(intervals)

intervals_sort = []
for begin, end in intervals:
    intervals_sort.append((begin, 0))
    intervals_sort.append((end, 1))

intervals_sort.sort()

result = 0
c = 0
for i in range(n * 2):
    if c and i:
        result += intervals_sort[i][0] - intervals_sort[i-1][0]
    if intervals_sort[i][1]:
        c += 1
    else:
        c -= 1

print(result)
