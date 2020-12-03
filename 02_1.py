def check_password(min, max, letter, password):
    
    letter_count = password.count(letter)
    if min <= letter_count <= max:
        return 1
    return 0

data_file = open("data/data_02.txt", "r")
lines = data_file.readlines()

valid_passwords = 0

for line in lines:
    split_space = line.split(" ")

    bounds = split_space[0].split("-")
    min =  int(bounds[0])
    max = int(bounds[1])

    letter = split_space[1].split(":")[0]

    password = split_space[2]
    validity = check_password(min, max, letter, password)
    valid_passwords = valid_passwords + validity

print(valid_passwords)

