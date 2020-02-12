dungeon_map = {} 
link = input().split()
while len(link) == 2:
    dungeon_map.setdefault(link[0], set()).add(link[1])
    dungeon_map.setdefault(link[1], set()).add(link[0])
    link = input().split()
_in = link[0]
_out = input()

run = {_in}
all_exits = set()
while run:
    new_way = set()
    for entry in run:
        new_way.update(dungeon_map[entry])
    all_exits.update(run)
    run = new_way - all_exits

if _out in all_exits:
    print('YES')
else:
    print('NO')
