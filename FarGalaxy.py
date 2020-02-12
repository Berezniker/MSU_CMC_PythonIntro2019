def dist(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2)**0.5

line = input()
galaxy_map = []
max_distance = (0, None, None)
while ' ' in line:
    line = line.split()
    coord = [float(i) for i in line[:-1]]
    galaxy_name = line[-1]
    for g_name, g_coord in galaxy_map:
        distance = dist(g_coord, coord)
        if max_distance[0] < distance:
            max_distance = (distance, g_name, galaxy_name)
    galaxy_map.append((galaxy_name, coord))
    line = input()

print(*sorted(max_distance[1:]))
