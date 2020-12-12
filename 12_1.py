def load_data() -> list:
    with open("data/data_12.txt") as data_file:
        data_string = data_file.read()
    data_array = data_string.split("\n")
    return data_array


def format_data(data):
    output = []
    for datum in data:
        action = datum[0]
        value = int(datum[1:])
        output.append({"action": action, "value": value})

    return output


def new_movement(coordinates, instruction):
    if instruction["action"] == "N":
        coordinates["y"] += instruction["value"]
    if instruction["action"] == "S":
        coordinates["y"] -= instruction["value"]
    if instruction["action"] == "E":
        coordinates["x"] += instruction["value"]
    if instruction["action"] == "W":
        coordinates["x"] -= instruction["value"]

    return coordinates


def rotation(direction, instruction):
    print("----")
    print(f"Current Direction: {direction}")
    print(f"Instruction: {instruction}")
    heading_dict = {"N": 0, "E": 90, "S": 180, "W": 270}
    heading = heading_dict[direction]
    print(f"Current Heading: {heading}")
    if instruction["action"] == "L":
        heading -= instruction["value"]
    elif instruction["action"] == "R":
        heading += instruction["value"]
    print(f"New Heading: {heading}")
    if heading >= 360:
        heading -= 360
    elif heading < 0:
        heading += 360
    direction = next((k for k in heading_dict if heading_dict[k] == heading), None)
    if direction == None:
        print(f"THE HEADING IS NONE")
    return direction



def process_instruction(coordinates, direction, instruction):

    if instruction["action"] == "F":
        instruction["action"] = direction
        coordinates = new_movement(coordinates, instruction)
        return coordinates, direction

    if instruction["action"] == "L" or instruction["action"] == "R":
        direction = rotation(direction, instruction)
        return coordinates, direction

    coordinates = new_movement(coordinates, instruction)
    return coordinates, direction



data = format_data(load_data())


coordinates = {"x": 0, "y": 0}

direction = "E"


for instruction in data:
    coordinates, direction = process_instruction(coordinates, direction, instruction)


manhaton = abs(coordinates['x']) + abs(coordinates['y'])
print(manhaton)