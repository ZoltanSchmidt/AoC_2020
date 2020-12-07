import re


    # part1
def rec_search1(r_table, in_bag, searchbag):
    if not r_table[in_bag]:
        return False
    elif searchbag in r_table[in_bag]:
        return True
    else:
        for bag in r_table[in_bag]:
            if rec_search1(r_table, bag, searchbag):
                return True
        return False

    # part2
def getbags(r_table, in_bag):
    counter = 0
    if not r_table[in_bag][0]:
        return 0
    else:
        for bag, count in zip(r_table[in_bag][0],r_table[in_bag][1]):
            counter += int(count) * (1 + getbags(r_table,bag))
        return counter


if __name__ == '__main__':
    with open("advent7.txt") as f:
        text = f.read()

    rules = text.split('\n')
    # part1
    rule_table = dict()
    # part2
    rule_table_numbered = dict()

    searched_bag_name = 'shiny gold bag'
    pattern1 = r'[a-z]+\s[a-z]+\sbag'
    pattern2 = r'[0-9]'

    for rule in rules:
        name_match = re.findall(pattern1, rule)
        count_match = re.findall(pattern2, rule)
        item = name_match.pop(0)
        if count_match:
            # part1
            rule_table[item] = (name_match)
            # part2
            rule_table_numbered[item] = (name_match, count_match)
        else:
            # part1
            rule_table[item] = ([])
            # part2
            rule_table_numbered[item] = ([], [])

    # part1
    ok_bags = [bag for bag in rule_table.keys() if rec_search1(rule_table, bag, searched_bag_name)]
    print(len(ok_bags))

    # part2
    print(getbags(rule_table_numbered,searched_bag_name))