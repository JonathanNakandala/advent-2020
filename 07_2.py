def clean_contains(string):
    string = string.strip().replace(" bags", "").replace(" bag", "")
    return string


def count_up_bags(rules, bag, count, match_list):
    matching_rules = []
    for container in rules:
        if not (container["container"] == bag):
            names = [i["bag"] for i in container["contains"]]
            if bag in names:
                count += 1
                matching_rules.append(container)
                match_list.append(container["container"])
    for match in matching_rules:
        count, match_list = count_up_bags(rules, match["container"], count, match_list)
    return count, match_list


def count_bag_permutations(rules, bag):
    _, matching_rules = count_up_bags(rules, bag, 0, [])
    count = len(list(set(matching_rules)))
    print(count)

def count_down_bags(rules, bag, count):
    rule = next(rule for rule in rules if rule["container"] == bag)
    for contain in rule['contains']:
        for i in range(contain['number']):
            count += 1
            count = count_down_bags(rules, contain['bag'], count)
            
    return count
data_file = open("data/data_07.txt", "r")
data_string = data_file.read()
data_file.close()


rules = data_string.split("\n")

rule_list = []
for rule in rules:
    container = rule.split("contain")[0].replace(" bags", "").strip()
    contains = rule.split("contain")[1].strip().replace(".", "").split(",")
    contains = list(map(clean_contains, contains))
    contains_data = []
    for content in contains:
        splitted_content = content.split(" ", 1)
        if splitted_content[0] == "no":
            pass
        else:
            content_data = {"number": int(splitted_content[0]), "bag": splitted_content[1]}
            contains_data.append(content_data)

    rule_dict = {"container": container, "contains": contains_data}
    rule_list.append(rule_dict)


count_bag_permutations(rule_list, "shiny gold")

total = count_down_bags(rule_list, "shiny gold", 0)

print(total)