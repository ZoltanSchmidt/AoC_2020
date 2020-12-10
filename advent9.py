

def find_wrong(preamble,numbers):
    for ind, num in enumerate(numbers):
        valid=False
        for preamb in preamble:
            if num - preamb in preamble and num != preamb:
                valid = True
                break
        if not valid:
            return num
        else:
            preamble.pop(0)
            preamble.append(num)


def find_weakness(full_num_list,searched_sum):
    list_of_sum = []
    for ind, num in enumerate(full_num_list):
        list_of_sum.clear()
        list_of_sum.append(num)
        for sum_item in full_num_list[ind+1:]:
           list_of_sum.append(sum_item)
           if sum(list_of_sum) == searched_sum:
               return min(list_of_sum)+max(list_of_sum)
           elif sum(list_of_sum) > searched_sum:
                break


if __name__ == '__main__':
    with open("advent9.txt") as f:
        text = f.read()

    full_list = [int(line) for line in  text.split('\n')]

    preamble_length = 25
    preamble_list,number_list = full_list[:preamble_length],full_list[preamble_length:]

    # part1
    wrong = find_wrong(preamble_list,number_list)
    print(wrong)

    # part2
    print(find_weakness(full_list,wrong))
