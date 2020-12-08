import linecache
import copy

def file_len():
    with open("data/data_08.txt") as f:
        for i, _ in enumerate(f):
            pass
    return i + 1


def get_line(data, line):
    return data[line]


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


def swap_instruction(instruction):
    instruction = instruction.split(" ")
    if instruction[0] == "acc":
        return " ".join(instruction)
    if instruction[0] == "jmp":
        instruction[0] = "nop"
        return " ".join(instruction)
    if instruction[0] == "nop":
        instruction[0] = "jmp"
        return " ".join(instruction)


def check_for_repeat(instruction_list):
    line_number = 0
    previous_line = 0
    accumulator = 0
    repeat = False
    lines_visited = []
    while repeat == False and line_number < total_lines:
        
        lines_visited.append(line_number)
        if len(lines_visited) == len(set(lines_visited)):
            line_data = get_line(instruction_list, line_number)
            previous_line = line_number
            accumulator, line_number = process_line(line_data, accumulator, line_number)
            #print(f"Total: {accumulator} Line: {line_number}")
        
        else:
            repeat = True
            #print(f"Repeated : Total: {accumulator} Line: {line_number} Previous Line: {previous_line}")
            return (False, accumulator, line_number,  lines_visited)

    if repeat == False:
        #print(f"Finished Total: {accumulator} Line: {line_number} Previous Line: {previous_line}")
        return (True, accumulator, line_number,  lines_visited)




data_file = open("data/data_08.txt", "r")
data_string = data_file.read()
data_file.close()
data_array = data_string.split("\n")
total_lines = len(data_array)

no_repeat = False

change_position = 0

working_array = copy.deepcopy(data_array)

while not no_repeat:
    no_repeat, acc, line, line_vis = check_for_repeat(working_array)
    
    if no_repeat == False:
        working_array = copy.deepcopy(data_array)
        working_array[change_position] = swap_instruction(data_array[change_position])
        if change_position < total_lines:
            change_position +=1

print(f"Line Number: {change_position}")
print(f"Instruction from: {data_array[change_position-1]} Instruction to: {working_array[change_position-1]}")
print(f"Accumulator: {acc}")