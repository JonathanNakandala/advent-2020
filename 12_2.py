import math
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

def rotate(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.
    """
    angle = math.radians(angle)
    ox = origin['x']
    oy = origin['y']
    px = point['x']
    py = point['y']

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return {"x": qx, "y": qy}

def rotation(coordinates, instruction, waypoint):
    print("----")
    print(f"Waypoint: {waypoint}")
    print(f"Current Ship Position: {coordinates}")
    waypoint_position = {"x": coordinates['x']+ waypoint['x'], "y": coordinates['y'] + waypoint['y']}
    print(f"Waypoint position: {waypoint_position}")

    print(f"Instruction: {instruction}")
    if instruction["action"] == "R":
        waypoint_position = rotate(coordinates, waypoint_position, -instruction['value'])
    elif instruction["action"] == "L":
        waypoint_position = rotate(coordinates, waypoint_position, instruction['value'])
    
    waypoint = {"x":  waypoint_position['x'] - coordinates['x'], "y": waypoint_position['y'] - coordinates['y']}
    print(f"New relative waypoint position: {waypoint}")
    return waypoint



def move_to_waypoint(instruction, coordinates, waypoint):
    multiplier = instruction['value']
    print(f"The Multiplier: {multiplier}")
    print(waypoint)
    new_ship_location = {"x": coordinates['x'] + waypoint["x"]*multiplier, "y": coordinates['y'] + waypoint["y"]*multiplier }
    return new_ship_location

def process_instruction(coordinates, direction, instruction, waypoint):

    if instruction["action"] == "F":
        instruction["action"] = direction
        coordinates = move_to_waypoint(instruction, coordinates, waypoint)
        return coordinates, direction, waypoint

    if instruction["action"] == "L" or instruction["action"] == "R":
        waypoint = rotation(coordinates, instruction, waypoint)
        return coordinates, direction, waypoint

    waypoint = new_movement(waypoint, instruction)
    return coordinates, direction, waypoint



data = format_data(load_data())


coordinates = {"x": 0, "y": 0}
waypoint = {"x": 10, "y": 1}
direction = "E"


for instruction in data:
    coordinates, direction, waypoint = process_instruction(coordinates, direction, instruction, waypoint)
    print(f"Calculated: {coordinates}")

manhaton = abs(coordinates['x']) + abs(coordinates['y'])
print(manhaton)
print(coordinates)