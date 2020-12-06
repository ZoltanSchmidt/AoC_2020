import re


def search1(lines):
    counter = 0
    for line in lines:
        ranges = re.findall(r'[\d]+', line)
        minimum, maximum = [int(item) for item in ranges]
        first_half, psw = line.split(': ')
        letter = first_half[-1]
        if psw.count(letter) in range(minimum, maximum + 1):
            counter += 1
    return counter


def search2(lines):
    counter = 0
    for line in lines:
        positions = re.findall(r'[\d]+', line)
        pos1, pos2 = [(int(item) - 1) for item in positions]

        first_half, psw = line.split(': ')
        letter = first_half[-1]
        if max(pos1, pos2) <= len(psw) - 1:
            if (psw[pos1] != psw[pos2]) and letter in [psw[pos1], psw[pos2]]:
                counter += 1
    return counter


if __name__ == '__main__':
    with open("advent2.txt") as f:
        Lines = f.readlines()
    # part1
    print(search1(Lines))
    # part2
    print(search2(Lines))
