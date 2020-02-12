object_list = eval(input())

miracle_conveyor = []
for obj in object_list:
    if type(obj) is tuple:
        for elem in obj:
            miracle_conveyor.append(elem)
    elif type(obj) is int:
        index = int(obj)
        if index > len(miracle_conveyor):
            break  # нельзя снять [index] объектов с конвейера
        print(tuple(miracle_conveyor[:index]))
        del miracle_conveyor[:index]
# в последовательности нет больше команд
