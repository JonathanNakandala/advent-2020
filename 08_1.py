import linecache


def file_len():
    with open("data/data_08.txt") as f:
        for i, _ in enumerate(f):
            pass
    return i + 1


def get_line(line):
    return linecache.getline("data/data_08.txt", line).strip()


def process_line(data, accumulator, line_number):
    data = data.split(" ")
    data[1] = int(data[1])
    if data[0] == "acc":
        #print(data)
        line_number += 1
        accumulator += data[1]
        return accumulator, line_number
    if data[0] == "jmp":
        #print(data)
        line_number += data[1]
        return accumulator, line_number
    if data[0] == "nop":
        #print(data)
        line_number += 1
        return accumulator, line_number

total_lines = file_len()

line_number = 1
accumulator = 0



repeat = False
lines_visited = []
while repeat == False and line_number < total_lines:
    
    lines_visited.append(line_number)
    if len(lines_visited) == len(set(lines_visited)):
        line_data = get_line(line_number)
        accumulator, line_number = process_line(line_data, accumulator, line_number)
        #print(f"Total: {accumulator} Line: {line_number}")
    
    else:
        repeat = True
        print(f"Total: {accumulator} Line: {line_number}")


