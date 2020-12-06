import math


def mapping(maps, rigth, down):
    counter = 0
    for ind, line in enumerate(maps):
        if not ind % down and ind > 0:
            if line[int((ind / down)) * rigth] == '#':
                counter += 1
    return counter


if __name__ == '__main__':
    with open("advent3.txt") as f:
        Lines = f.readlines()

    height = len(Lines)
    width = len(Lines[0].strip())

    map_ratio = math.ceil(height / width * 7) + 1

    fullmap = [line.strip() * map_ratio for line in Lines]

    print(mapping(fullmap, 1, 1) * mapping(fullmap, 3, 1) * mapping(fullmap, 5, 1) * mapping(fullmap, 7, 1) * mapping(fullmap, 1, 2))

