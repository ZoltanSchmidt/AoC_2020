import re


def validate(document, patterns):
    doc = document + ' '
    for pattern in patterns:
        if not re.findall(pattern, doc):
            return False
    return True


if __name__ == '__main__':
    with open("advent4.txt") as f:
        text = f.read()

    papers = text.split('\n\n')

    # part1
    patterns1 = [r"byr:", r"iyr:", r"eyr:", r"hgt:", r"hcl:", r"ecl:", r"pid:"]
    valid1 = [paper for paper in papers if validate(paper, patterns1)]
    print(len(valid1))

    # part2
    patterns2 = [r"byr:(19[2-9][0-9]|200[0-2])\s",
                 r"iyr:(201[0-9]|2020)\s",
                 r"eyr:(202[0-9]|2030)\s",
                 r"hgt:(((59)|(6[0-9])|(7[0-6]))in)|(1(([5-8][0-9])|(9[0-3]))cm)+",
                 r"hcl:#[0-9a-f]{6}\s",
                 r"ecl:(amb|blu|brn|gry|grn|hzl|oth)\s",
                 r"pid:[0-9]{9}\s"]

    valid2 = [paper for paper in papers if validate(paper, patterns2)]
    print(len(valid2))
