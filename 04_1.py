def replace_new_lines(line):
    return line.replace("\n", " ")


def process_passport(passport):
    sections = passport.split(" ")

    # print(sections)
    dictionary = {}
    for section in sections:
        data = section.split(":")
        # print(data)
        dictionary[data[0]] = data[1]

    return dictionary


def check_fields(data):
    if {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"} <= data.keys():
        return True
    return False


data_file = open("data/data_04.txt", "r")
data_string = data_file.read()
data_file.close()


data_array = data_string.split("\n\n")


passports = list(map(replace_new_lines, data_array))

# print(len(passports))
valid_count = 0
for passport in passports:

    passport_dict = process_passport(passport)

    is_valid = check_fields(passport_dict)
    if is_valid:
        valid_count += 1

print(f"Total Passports: {len(passports)} Valid Passports: {valid_count}")