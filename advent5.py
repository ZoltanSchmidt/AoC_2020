if __name__ == '__main__':
    with open("advent5.txt") as f:
        text = f.read()
    seats = text.split('\n')
    largest = 0
    ID_list = []

    for seat in seats:
        seat = seat.replace('F','0').replace('B', '1').replace('L','0').replace('R', '1')
        seat_id = int(seat,2)
        # Part 1
        largest = max(seat_id,largest)
        # PArt 2
        ID_list.append(seat_id)
        
    # Part 1
    print(largest)

    # Part 2
    ID_list.sort()
    # Create full seat list and search for the difference
    All = list(range(ID_list[0],ID_list[-1]+1))
    print(set(All).difference(set(ID_list)))