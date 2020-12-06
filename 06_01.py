def replace_new_lines(line):
    return line.replace("\n", " ")


data_file = open("data/data_06.txt", "r")
data_string = data_file.read()
data_file.close()


data_array = data_string.split("\n\n")
questions = list(map(replace_new_lines, data_array))

answer_count = 0
for group in questions:
    answers = "".join(group)
    answers = answers.replace(" ", "")
    unique_answers = set()
    for answer in answers:
        unique_answers.add(answer)

    answer_count += len(unique_answers)

print(answer_count)