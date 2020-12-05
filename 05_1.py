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

largest_id = 0
for ticket in tickets:
    row_data = ticket[:7]
    column_data = ticket[-3:]

    row_number = calculate_row(row_data)


    column_number = calculate_column(column_data)

    seat_id = calculate_id(row_number, column_number)
    
    if seat_id >= largest_id:
        largest_id = seat_id
    #print(f"row {row_number}, column {column_number}, seat ID {seat_id}")

print(largest_id)