data_file = open("data/data_03.txt", "r")
lines = data_file.readlines()

world_map = []
for line in lines:
    line = line.strip()
    row_array = []
    for point in line:
        row_array.append(point)
    world_map.append(row_array)


x = 0
y = 0
tree_count = 0
for row in world_map:

    position_data = world_map[y][x]
    if position_data == "#":
        tree_count = tree_count + 1
    if x >= 28:
        x = x + 3 - 31
    else:
        x = x + 3
    y = y + 1

print(tree_count)