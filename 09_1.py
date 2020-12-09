import itertools


def get_data():

    with open("data/data_09.txt") as data_file:
        data_string = data_file.read()
    data_array = data_string.split("\n")
    data_array = list(map(lambda x: int(x), data_array))
    return data_array


def fetch_preamble(start, length):
    with open("data/data_09.txt") as f:
        iteration = itertools.islice(f, start, start + length)
        list_output = list(map(lambda x: str.rstrip(x), [item for item in iteration]))
    return list_output


def check_sums(preamble, number):
    solution = []
    for i, value1 in enumerate(preamble):
        for value2 in preamble[i:]:
            total = int(value1) + int(value2)
            if total == number:
                solution.append(number)
    if len(solution) == 0:
        return False
    else:
        return True


data_set = get_data()
total = len(data_set)
preamble_length = 25

remaining_data = data_set[preamble_length:]

for counter, value in enumerate(remaining_data):
    preamble = fetch_preamble(counter, preamble_length)
    result = check_sums(preamble, value)
    if not result:
        print(f"Value {value} has failed!!!")