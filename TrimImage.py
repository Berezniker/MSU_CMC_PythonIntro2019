picture = []
x_max = y_max = float('-inf')
x_min = y_min = float('inf')

new_item = input().split(' ')
while not all(elem == '0' for elem in new_item):
    new_item[:-1] = [int(i) for i in new_item[:-1]]
    if new_item[2] != 0 and new_item[3] != 0:
        x_max = max(x_max, new_item[0], new_item[0] + new_item[2])
        y_max = max(y_max, new_item[1], new_item[1] + new_item[3])
        x_min = min(x_min, new_item[0], new_item[0] + new_item[2])
        y_min = min(y_min, new_item[1], new_item[1] + new_item[3])
        if new_item[2] < 0:
            new_item[0] += new_item[2]
            new_item[2] = abs(new_item[2])
        if new_item[3] < 0:
            new_item[1] += new_item[3]
            new_item[3] = abs(new_item[3])
        picture.append(new_item)
    new_item = input().split(' ')

for pic in picture:
    pic[0] -= x_min
    pic[1] -= y_min

size = (x_max - x_min, y_max - y_min)
pano = ['.' * size[0] for _ in range(size[1])]

for *pic, smbl in picture:
    for i in range(pic[3]): 
        pano[pic[1] + i] = pano[pic[1] + i][:pic[0]] + \
                           smbl * pic[2] + \
                           pano[pic[1] + i][pic[0] + pic[2]:]

for i in pano:
    print(*i, sep='')
