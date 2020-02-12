col, row = [int(num) for num in input().split(',')]

i, j, x_dir, y_dir = 0, 0, 0, 1
# direction: (0, 1) -- '->', (1, 0) -- 'v', (0, -1) -- '<-', (-1, 0) -- '^'

spiral = [[None] * col for _ in range(row)]
for num in range(row * col):
    spiral[i][j] = num % 10
    if i + x_dir < 0 or i + x_dir >= row or \
       j + y_dir < 0 or j + y_dir >= col or \
       spiral[i + x_dir][j + y_dir] is not None:
           x_dir, y_dir = y_dir, -x_dir  # change direction
    i, j = i + x_dir, j + y_dir

for str_row in spiral:
    print(*str_row)
