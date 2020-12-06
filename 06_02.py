from collections import Counter


def replace_new_lines(line):
    return line.replace("\n", " ")


data_file = open("data/data_06.txt", "r")
data_string = data_file.read()
data_file.close()


data_array = data_string.split("\n\n")
questions = list(map(replace_new_lines, data_array))

answer_count = 0
for group in questions:
    group = group.split(" ")
    group_count = len(group)

    answers_counter = Counter()
    for answer in group:
        answer_letter_counter = Counter()
        for letter in answer:

            answer_letter_counter += Counter(letter)
        answers_counter += answer_letter_counter

    answers_in_all = {k: v for k, v in answers_counter.items() if v == group_count}

    answer_count += len(answers_in_all)

print(answer_count)