import math

def tribonacci(ind):
    # Start indexing from a later point
    n = ind+4
    signature = [0,0,1]
    res = signature[:n]
    for i in range(n - 3): res.append(sum(res[-3:]))
    return res[n-1]

def get_sections(diff_arr):

    sections = []
    curr_ind = 0
    while True:
        border = curr_ind + diff_arr[curr_ind:].index(3)
        sections.insert(0,diff_arr[curr_ind+1:border])
        if border == len(diff_arr)-1:
            return sections
        try:
            curr_ind = border + 1 + diff_arr[border+1:].index(1)
        except:
            return sections

if __name__ == '__main__':
    with open("advent10.txt") as f:
        text = f.read()

    jolts = [int(line) for line in  text.split('\n')]

    # device built-in joltage rating
    jolts.append(max(jolts)+3)

    jolts.sort()
    subtract_jolts = [0] + jolts[:-1]
    jolt_diffs = [j1 - j2 for (j1, j2) in zip(jolts, subtract_jolts)]

    # Part1
    print(jolt_diffs.count(1)*jolt_diffs.count(3))
    # Part2
    sections = get_sections(jolt_diffs)
    print(math.prod([tribonacci(len(sect)) for sect in sections]))