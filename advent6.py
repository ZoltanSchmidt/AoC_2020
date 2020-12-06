

if __name__ == '__main__':
    with open("advent6.txt") as f:
        text = f.read()

    groups = text.split('\n\n')

    # part1
    answers = [ len(set(''.join(group.split('\n')))) for group in groups ]
    print(sum(answers))

    # part2
    answers = [ len(set.intersection(*[set(line) for line in group.split('\n')])) for group in groups ]
    print(sum(answers))


    # part2 long
    # counter = 0
    # group = groups[0].split('\n')
    # for group in groups:
    #     for ind, line in enumerate(group.split('\n')):
    #         if not ind:
    #             shared_ans = set(line)
    #         shared_ans = shared_ans.intersection(set(line))
    #     counter += len(shared_ans)
    # print(counter)


