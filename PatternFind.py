string = input()
template = input()

template_split = []
offset = 0
for line in template.split('@'):
    if line != '':
        template_split.append((offset, line))
        offset += len(line)
    offset += 1

if len(template_split) == 0:
    indx = 0
elif len(template) > len(string):
    indx = -1
else:
    offset = len(template)
    for i in range(len(string) - len(template) + 1):
        for l, line in template_split:
            if string[i + l: i + l + len(line)] != line:
                break
        else:
            indx = i
            break
    else:
        indx = -1

print(indx)
