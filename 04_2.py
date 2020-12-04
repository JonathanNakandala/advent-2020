import binascii


def replace_new_lines(line):
    return line.replace("\n", " ")


def process_passport(passport):
    sections = passport.split(" ")
    dictionary = {}
    for section in sections:
        data = section.split(":")
        dictionary[data[0]] = data[1]

    return dictionary


def chk_byr(data):
    data = int(data)
    if 1920 <= data <= 2002:
        return True
    return False


def chk_iyr(data):
    data = int(data)
    if 2010 <= data <= 2020:
        return True
    return False


def chk_eyr(data):
    data = int(data)
    if 2020 <= data <= 2030:
        return True
    return False


def chk_hgt(data):
    unit = data[-2:]
    value = int("".join(filter(lambda x: x.isdigit(), data)))
    if unit == "cm":
        if 150 <= value <= 193:
            return True
    if unit == "in":
        if 59 <= value <= 76:
            return True
    return False


def parse_hex(code):
    return binascii.unhexlify(code)


def chk_hcl(data):
    if not data.startswith("#"):
        return False
    if not len(data) == 7:
        return False
    try:
        parse_hex(data[1:])
    except:
        return False
    else:
        return True
    return False


def chk_ecl(data):
    eye_colours = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if data in eye_colours:
        return True
    return False


def chk_pid(data):
    if len(data) == 9:
        return True
    return False


def validate_fields(data):
    if (
        chk_byr(data["byr"])
        and chk_iyr(data["iyr"])
        and chk_eyr(data["eyr"])
        and chk_hgt(data["hgt"])
        and chk_hcl(data["hcl"])
        and chk_ecl(data["ecl"])
        and chk_pid(data["pid"])
    ):
        return True
    return False


def check_fields(data):
    if {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"} <= data.keys():
        is_valid = validate_fields(data)
        if is_valid:
            return True
    return False


data_file = open("data/data_04.txt", "r")
data_string = data_file.read()
data_file.close()

data_array = data_string.split("\n\n")

passports = list(map(replace_new_lines, data_array))

valid_count = 0
for passport in passports:

    passport_dict = process_passport(passport)

    is_valid = check_fields(passport_dict)
    if is_valid:
        valid_count += 1

print(f"Total Passports: {len(passports)} Valid Passports: {valid_count}")