battlefield = [input()]
battlefield.append(input())
while battlefield[-1][0] != '-':
    battlefield.append(input())

row = len(battlefield)
col = len(battlefield[0])
number_of_ships = 0
for i in range(1, row - 1):
    for j in range(1, col - 1):
        if battlefield[i][j] == '#' and \
           battlefield[i - 1][j] != '#' and \
           battlefield[i][j - 1] != '#':
               number_of_ships += 1

print(number_of_ships)
