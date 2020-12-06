
def search (nums):
    for firstnum in nums:
        for secondnum in nums:
            if ( sum - (firstnum + secondnum)) in nums:
                print(firstnum*secondnum*(sum - (firstnum + secondnum)))
                return

if __name__ == '__main__':
    sum = 2020

    with open("advent1.txt") as f:
        Lines = f.readlines()
    nums = [int(line) for line in Lines]

    # first part
    for num in nums:
        if ( sum - num) in nums:
            print(num*(sum - num))
            break
    # second part
    search(nums)
