import itertools
def generate_seating_plan():
    passenger_list = []
    y = 1
    while y < 127:
        x = 0
        while x < 8:
            passenger_list.append({"row": y, "column": x, "id": calculate_id(y, x)})
            x +=1
        y +=1
    return passenger_list
def calculate_row(data):
    data = data.replace("F", "0").replace("B", "1")
    number = int(data, 2)
    return number

def calculate_column(data):
    data = data.replace("L", "0").replace("R", "1")
    number = int(data, 2)
    return number

def calculate_id(row, column):
    return (row * 8) + column

data_file = open("data/data_05.txt", "r")
data_string = data_file.read()
data_file.close()
tickets = data_string.split("\n")

seating_plan = generate_seating_plan()

#print(passenger_list)

largest_id = 0
passenger_list = []

for ticket in tickets:
    row_data = ticket[:7]
    column_data = ticket[-3:]

    row_number = calculate_row(row_data)


    column_number = calculate_column(column_data)

    seat_id = calculate_id(row_number, column_number)
    
    if seat_id >= largest_id:
        largest_id = seat_id

    position = {"row": row_number, "column": column_number, "id": seat_id}
    if position in seating_plan:
        seating_plan.remove(position)
    
    passenger_list.append({"row": row_number, "column": column_number, "id": seat_id})


candidates = []
for seat in seating_plan:
    plus = next((item for item in seating_plan if item["id"] == seat["id"] + 2 ), None)
    if plus:
        candidates.append(plus)

print(len(candidates))

for candidate in candidates:
    if candidate in seating_plan:
        seating_plan.remove(candidate)


print(seating_plan)

