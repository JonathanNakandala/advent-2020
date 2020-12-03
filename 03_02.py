from functools import reduce

data_file = open("data/data_03.txt", "r")
lines = data_file.readlines()

world_map = []
for line in lines:
    line = line.strip()
    row_array = []
    for point in line:
        row_array.append(point)
    world_map.append(row_array)


def calculate_tree_count(right, down):

    x = 0
    y = 0
    tree_count = 0
    while y < len(world_map):
        position_data = world_map[y][x]
        if position_data == "#":
            tree_count = tree_count + 1

        x = (x + right) % 31
        y = y + down
    return tree_count


totals = []
totals.append(calculate_tree_count(1, 1))
totals.append(calculate_tree_count(3, 1))
totals.append(calculate_tree_count(5, 1))
totals.append(calculate_tree_count(7, 1))
totals.append(calculate_tree_count(1, 2))

multiplied_together = reduce(lambda x, y: x * y, totals)
print(multiplied_together)