def turtle(coord, direction):
    while True:
        cmd = yield coord
        if cmd == 'f':
            if direction == 0:
                coord = (coord[0] + 1, coord[1])
            elif direction == 1:
                coord = (coord[0], coord[1] + 1)
            elif direction == 2:
                coord = (coord[0] - 1, coord[1])
            elif direction == 3:
                coord = (coord[0], coord[1] - 1)
        elif cmd == 'l':
            direction = (direction + 1) % 4
        elif cmd == 'r':
            direction = (direction - 1) % 4
